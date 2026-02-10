#!/usr/bin/env node

import { providerdev } from '@stackql/provider-utils';

async function generateProvider() {
  // Get command line arguments
  const args = process.argv.slice(2);
  const getArg = (flag) => {
    const index = args.indexOf(flag);
    return index !== -1 ? args[index + 1] : null;
  };

  const providerName = getArg('--provider-name');
  const inputDir = getArg('--input-dir');
  const outputDir = getArg('--output-dir');
  const configPath = getArg('--config-path');
  const servers = getArg('--servers');
  const providerConfig = getArg('--provider-config');
  const skipFiles = getArg('--skip-files')?.split(',') || [];
  const overwrite = args.includes('--overwrite');
  const verbose = args.includes('--verbose');

  if (!providerName || !inputDir || !outputDir || !configPath) {
    console.error('Error: Missing required arguments');
    console.error('Usage: node generate-provider.mjs --provider-name NAME --input-dir DIR --output-dir DIR --config-path PATH [--servers JSON] [--provider-config JSON] [--skip-files LIST] [--overwrite] [--verbose]');
    process.exit(1);
  }

  try {
    console.log(`Generating StackQL provider extensions for: ${providerName}`);
    console.log(`Input directory: ${inputDir}`);
    console.log(`Output directory: ${outputDir}`);
    console.log(`Config path: ${configPath}`);
    
    if (servers) {
      console.log(`Custom servers configuration provided`);
    }
    
    if (providerConfig) {
      console.log(`Custom provider configuration provided`);
    }
    
    if (skipFiles.length > 0) {
      console.log(`Skipping files: ${skipFiles.join(', ')}`);
    }

    const result = await providerdev.generate({
      inputDir,
      outputDir,
      configPath,
      providerId: providerName,
      servers,
      providerConfig,
      skipFiles,
      overwrite,
      verbose
    });
    
    console.log('Provider generation completed successfully:', result);
  } catch (error) {
    console.error('Error generating provider extensions:', error);
    process.exit(1);
  }
}

generateProvider();