#!/usr/bin/env node

const { runQuery } = require('@stackql/pgwire-lite');
const fs = require('fs');
const path = require('path');

// Get current directory
const baseDir = path.resolve(path.dirname(process.argv[1]), '..');

// Default connection settings
const defaultOptions = {
  user: 'stackql',
  database: 'stackql',
  host: 'localhost',
  port: 5444,
  debug: false,
};

// Parse command line arguments
const args = process.argv.slice(2);
let provider = null;
let port = 5444;
let verbose = false;
let outputFormat = 'json';
let timeoutMs = 60000; // Default timeout: 60 seconds

for (let i = 0; i < args.length; i++) {
  if (args[i].startsWith('--')) {
    switch (args[i]) {
      case '--port':
        port = parseInt(args[++i], 10);
        break;
      case '--verbose':
        verbose = true;
        break;
      case '--format':
        outputFormat = args[++i];
        if (!['json', 'csv', 'markdown'].includes(outputFormat)) {
          console.error(`Error: Invalid output format "${outputFormat}". Must be json, csv, or markdown.`);
          process.exit(1);
        }
        break;
      case '--timeout':
        timeoutMs = parseInt(args[++i], 10);
        break;
      case '--help':
        console.log(`
Usage: test-meta-routes.js <provider> [OPTIONS]

Test all metadata routes for a StackQL provider.

Arguments:
  provider                  Name of the provider to test

Options:
  --port PORT               Server port (default: 5444)
  --verbose                 Enable verbose output
  --format FORMAT           Output format: json, csv, markdown (default: json)
  --timeout MILLISECONDS    Query timeout in milliseconds (default: 60000)
  --help                    Display this help message
        `);
        process.exit(0);
        break;
      default:
        console.error(`Error: Unknown option "${args[i]}"`);
        process.exit(1);
    }
  } else if (!provider) {
    provider = args[i];
  }
}

// Check that provider was specified
if (!provider) {
  console.error('Error: Provider name must be specified');
  console.error('Usage: test-meta-routes.js <provider> [OPTIONS]');
  process.exit(1);
}

// Set up connection options
const connectionOptions = {
  ...defaultOptions,
  port,
  // Set query timeout
  statement_timeout: timeoutMs,
};

// Get start time
const startTime = new Date();

const results = {
  provider,
  totalServices: 0,
  totalResources: 0,
  totalMethods: 0,
  selectableMethods: 0,
  nonSelectableResourceCount: 0,
  nonSelectableResources: [],
};

/**
 * Run a query and handle errors
 * @param {string} query - SQL query to run
 * @param {string} description - Description for logging
 * @returns {Promise<Array>} - Query results
 */
async function executeQuery(query, description) {
  if (verbose) {
    console.log(`Running: ${query}`);
  } else {
    process.stdout.write(`${description}... `);
  }
  
  try {
    const result = await runQuery(connectionOptions, query);
    
    if (!verbose) {
      if (result.data && result.data.length) {
        console.log(`✅ (${result.data.length} rows)`);
      } else {
        console.log('✅');
      }
    } else {
      console.info(result.data);
    }
    
    return result.data;
  } catch (error) {
    if (!verbose) {
      console.log('❌');
    }
    
    results.errors.push({
      query,
      description,
      error: error.message,
      timestamp: new Date().toISOString()
    });
    
    results.summary.errors++;
    
    if (error.message.includes('the last operation didn\'t produce a result')) {
      return [];
    }
    
    if (error.message.includes('SELECT not supported for this resource')) {
      if (verbose) {
        console.warn(`  Warning: Resource is not selectable`);
      }
      return null;
    }
    
    console.error(`Error executing ${description}: ${error.message}`);
    return [];
  }
}

/**
 * Test all provider meta routes
 */
async function testMetaRoutes() {
  try {
    console.log(`\n🔍 Testing meta routes for provider: ${provider}\n`);
    
    // SHOW PROVIDERS to verify provider exists
    const registryQuery = "SHOW PROVIDERS";
    const providers = await executeQuery(registryQuery, "Checking registry providers");
    
    const providerExists = providers && providers.some(p => p.name === provider);
    if (!providerExists) {
      console.error(`Error: Provider '${provider}' not found in registry`);
      if (providers && providers.length > 0) {
        console.log("Available providers:");
        providers.forEach(p => console.log(`  - ${p.name}`));
      }
      process.exit(1);
    }

    // SHOW SERVICES IN <provider>
    const servicesQuery = `SHOW SERVICES IN ${provider}`;
    const services = await executeQuery(servicesQuery, "Getting services");
    
    if (!services || services.length === 0) {
      console.error(`Error: No services found for provider '${provider}'`);
      process.exit(1);
    }
    
    console.log(`\nFound ${services.length} services in ${provider}`);
    results.totalServices += services.length;

    // for each service
    for (const service of services) {
      const serviceName = service.name;
      console.log(`\n📊 Processing service: ${serviceName}`);
      
      // SHOW RESOURCES IN <provider>.<service>
      const resourcesQuery = `SHOW RESOURCES IN ${provider}.${serviceName}`;
      const resources = await executeQuery(resourcesQuery, `Getting resources for ${serviceName}`);
     
      if (!resources || resources.length === 0) {
        console.error(`Error: No resources found for ${provider}.${serviceName}`);
        process.exit(1);
      }
      
      console.log(`Found ${resources.length} resources in ${serviceName}`);
      results.totalResources += resources.length;
      
      // for each resource
      for (const resource of resources) {
        const resourceName = resource.name;
        console.log(`\n  🔹 Testing resource: ${resourceName}`);
        
        const resourceFQRN = `${provider}.${serviceName}.${resourceName}`;
        const resourceData = {
          name: resourceName,
          service: serviceName,
          selectable: false,
          sqlVerbs: {}
        };

        // SHOW EXTENDED METHODS IN <provider>.<service>.<resource>
        const methodsQuery = `SHOW EXTENDED METHODS IN ${resourceFQRN}`;
        const methods = await executeQuery(methodsQuery, `  Getting methods for ${resourceName}`);
        if (!methods || methods.length === 0) {
          console.error(`Error: Resource ${resourceName} has no methods`);
          process.exit(1);
        } else {
          console.log(`Found ${methods.length} methods for ${resourceName}`);
        }

        results.totalMethods += methods.length;

        for (const method of methods) {
          const methodName = method.MethodName;
          const sqlVerb = method.SQLVerb || 'exec';
          
          if(sqlVerb.toLowerCase() === 'select') {
            results.selectableMethods++;
            resourceData.selectable = true;
          }
          
          // Initialize the array if it doesn't exist yet
          if(!resourceData.sqlVerbs[sqlVerb]) {
            resourceData.sqlVerbs[sqlVerb] = [];
          }
          
          // Convert comma-delimited list to an array of trimmed values
          let requiredParamsArray = [];
          if (method.RequiredParams) {
            requiredParamsArray = method.RequiredParams
              .split(',')
              .map(param => param.trim())
              .filter(param => param.length > 0);
          }
          
          // Push the method info to the array with the parsed required params
          resourceData.sqlVerbs[sqlVerb].push({
            methodName,
            requiredParams: requiredParamsArray
          });
        }

        // non exec methods must have unique signatures within a resource 
        // in other words no two methods mapped to the same sqlVerb should have the exact same set of required params, order is not important
        // if this condition is detected, log it and exit the program immediately
        let hasSelect = false;
        for (const [verb, methods] of Object.entries(resourceData.sqlVerbs)) {
          if (verb.toLowerCase() === 'select') {
            hasSelect = true;
          }
          if (verb.toLowerCase() === 'exec') {
            continue;
          }
          const seenSignatures = new Set();
          for (const method of methods) {
            const signature = JSON.stringify(method.requiredParams);
            if (seenSignatures.has(signature)) {
              console.error(`Error: Duplicate method signature found for ${verb} in ${resourceData.service}.${resourceName}:`, method);
              process.exit(1);
            }
            seenSignatures.add(signature);
          }
        }

        if (!hasSelect) {
          results.nonSelectableResourceCount++;
          results.nonSelectableResources.push(`${resourceData.service}.${resourceName}`);
        }

        // Try DESCRIBE EXTENDED if available
        if(resourceData.selectable) {
          try {
            const describeExtendedQuery = `DESCRIBE EXTENDED ${resourceFQRN}`;
            const extendedColumns = await executeQuery(describeExtendedQuery, `  Describing extended ${resourceName}`);

            if (extendedColumns !== null && extendedColumns.length > 0) {
              console.log(`Found ${extendedColumns.length} extended columns for ${resourceName}`);
            } else {
              console.error(`ERROR: No columns found for ${resourceName}`);
              process.exit(1);
            }
          } catch (error) {
            console.error(`Error describing extended ${resourceName}:`, error.message);
            process.exit(1);
          }
        }

      }
    }
    
    // Calculate execution time
    const endTime = new Date();
    const executionTime = (endTime - startTime) / 1000; // in seconds
    results.executionTime = executionTime;
    
    // Output summary
    console.log("\n📋 Test Summary:");
    console.info(results);

    // Save results to file
    // const resultsDir = path.join(baseDir, 'test-results');
    // if (!fs.existsSync(resultsDir)) {
    //   fs.mkdirSync(resultsDir, { recursive: true });
    // }
    
    // const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    
    // if (outputFormat === 'json') {
    //   const resultsFile = path.join(resultsDir, `${provider}-meta-test-${timestamp}.json`);
    //   fs.writeFileSync(resultsFile, JSON.stringify(results, null, 2));
    //   console.log(`\nDetailed results saved to: ${resultsFile}`);
    // } 
    // else if (outputFormat === 'csv') {
    //   // Generate CSV files
      
    //   // Main summary CSV
    //   const summaryFile = path.join(resultsDir, `${provider}-meta-test-summary-${timestamp}.csv`);
    //   const summaryCSV = [
    //     'Provider,Timestamp,Services,Resources,Methods,Selectable,Insertable,Updatable,Deletable,Executable,Errors,ExecutionTime',
    //     `${provider},${results.timestamp},${results.summary.totalServices},${results.summary.totalResources},${results.summary.totalMethods},${results.summary.selectableMethods},${results.summary.insertableMethods},${results.summary.updatableMethods},${results.summary.deletableMethods},${results.summary.executableMethods},${results.summary.errors},${results.executionTime}`
    //   ].join('\n');
    //   fs.writeFileSync(summaryFile, summaryCSV);
      
    //   // Services CSV
    //   const servicesFile = path.join(resultsDir, `${provider}-meta-test-services-${timestamp}.csv`);
    //   const servicesCSV = [
    //     'Service,Title,ResourceCount',
    //     ...results.services.map(s => `${s.name},${s.title || ''},${s.resourceCount || 0}`)
    //   ].join('\n');
    //   fs.writeFileSync(servicesFile, servicesCSV);
      
    //   // Resources CSV
    //   const resourcesFile = path.join(resultsDir, `${provider}-meta-test-resources-${timestamp}.csv`);
    //   const resourcesCSV = [
    //     'Service,Resource,FQRN,Selectable,ColumnCount,MethodCount',
    //     ...results.resources.map(r => `${r.service},${r.name},${r.fqrn},${r.selectable},${r.columnCount || 0},${r.methodCount || 0}`)
    //   ].join('\n');
    //   fs.writeFileSync(resourcesFile, resourcesCSV);
      
    //   // Methods CSV
    //   const methodsFile = path.join(resultsDir, `${provider}-meta-test-methods-${timestamp}.csv`);
    //   const methodsCSV = [
    //     'Service,Resource,Method,SQLVerb,FQRN',
    //     ...results.methods.map(m => `${m.service},${m.resource},${m.name},${m.sqlVerb},${m.fqrn}`)
    //   ].join('\n');
    //   fs.writeFileSync(methodsFile, methodsCSV);
      
    //   console.log(`\nDetailed results saved to CSV files in: ${resultsDir}`);
    // }
    // else if (outputFormat === 'markdown') {
    //   const mdFile = path.join(resultsDir, `${provider}-meta-test-${timestamp}.md`);
      
    //   const markdownContent = [
    //     `# StackQL Provider Test Results: ${provider}`,
    //     '',
    //     `Test run: ${results.timestamp}`,
    //     '',
    //     '## Summary',
    //     '',
    //     '| Metric | Count |',
    //     '|--------|-------|',
    //     `| Services | ${results.summary.totalServices} |`,
    //     `| Resources | ${results.summary.totalResources} |`,
    //     `| Methods | ${results.summary.totalMethods} |`,
    //     `| Errors | ${results.summary.errors} |`,
    //     `| Execution Time | ${results.executionTime.toFixed(2)} seconds |`,
    //     '',
    //     '### Methods by SQL Verb',
    //     '',
    //     '| Verb | Count |',
    //     '|------|-------|',
    //     ...Object.entries(results.verbs).map(([verb, count]) => `| ${verb.toUpperCase()} | ${count} |`),
    //     '',
    //     '## Services',
    //     '',
    //     '| Service | Resources |',
    //     '|---------|-----------|',
    //     ...results.services.map(s => `| ${s.name} | ${s.resourceCount || 0} |`),
    //     '',
    //     '## Resources with Most Methods',
    //     '',
    //     '| Resource | Service | Methods | Selectable |',
    //     '|----------|---------|---------|------------|',
    //     ...results.resources
    //       .sort((a, b) => (b.methodCount || 0) - (a.methodCount || 0))
    //       .slice(0, 20)
    //       .map(r => `| ${r.name} | ${r.service} | ${r.methodCount || 0} | ${r.selectable ? '✓' : '✗'} |`),
    //     '',
    //     '## Errors',
    //     '',
    //     results.errors.length > 0 
    //       ? [
    //           '| Query | Error |',
    //           '|-------|-------|',
    //           ...results.errors.map(e => `| \`${e.query}\` | ${e.error} |`)
    //         ].join('\n')
    //       : 'No errors encountered during testing.',
    //   ].join('\n');
      
    //   fs.writeFileSync(mdFile, markdownContent);
    //   console.log(`\nDetailed results saved to: ${mdFile}`);
    // }
    
  } catch (error) {
    console.error('Error in meta routes test:', error);
    process.exit(1);
  }
}

// Run the tests
testMetaRoutes();