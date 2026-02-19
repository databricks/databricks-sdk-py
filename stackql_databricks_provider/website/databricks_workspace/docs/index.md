---
title: databricks_workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/stackql-databricks-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Manage clusters, jobs, notebooks, MLflow and other Databricks workspace resources.

:::info

For Databricks account operations use the [__`databricks_account`__](https://databricks-account-provider.stackql.io/) provider.

:::

:::info[Provider Summary]

total services: __26__
total resources: __278__

:::

See also:    [[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)   

* * *   

## Installation 

```bash 
REGISTRY PULL databricks_workspace; 
```  

## Authentication  

To use the `databricks_workspace` provider, you can authenticate using one of the following methods:

### OAuth2 (Service Principal) [Default]

Set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

### Personal Access Token (Bearer)

Alternatively, set <CopyableCode code="DATABRICKS_TOKEN" /> to a Databricks personal access token (see <a href="https://docs.databricks.com/en/dev-tools/auth/pat.html">Databricks personal access tokens</a>), then supply the auth config when starting the shell:
```bash
export DATABRICKS_TOKEN=xxx

# Linux/Mac
AUTH='{ "databricks_workspace": { "type": "bearer", "credentialsenvvar": "DATABRICKS_TOKEN" }}'
./stackql shell --auth="${AUTH}"
```
```powershell
# PowerShell
$Auth = "{ 'databricks_workspace': { 'type': 'bearer', 'credentialsenvvar': 'DATABRICKS_TOKEN' }}"
stackql.exe shell --auth=$Auth
```

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/agentbricks/">agentbricks</a><br />
<a href="/services/apps/">apps</a><br />
<a href="/services/catalog/">catalog</a><br />
<a href="/services/cleanrooms/">cleanrooms</a><br />
<a href="/services/compute/">compute</a><br />
<a href="/services/dashboards/">dashboards</a><br />
<a href="/services/database/">database</a><br />
<a href="/services/dataquality/">dataquality</a><br />
<a href="/services/files/">files</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/iamv2/">iamv2</a><br />
<a href="/services/jobs/">jobs</a><br />
<a href="/services/marketplace/">marketplace</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/ml/">ml</a><br />
<a href="/services/oauth2/">oauth2</a><br />
<a href="/services/pipelines/">pipelines</a><br />
<a href="/services/postgres/">postgres</a><br />
<a href="/services/qualitymonitorv2/">qualitymonitorv2</a><br />
<a href="/services/serving/">serving</a><br />
<a href="/services/settings/">settings</a><br />
<a href="/services/settingsv2/">settingsv2</a><br />
<a href="/services/sharing/">sharing</a><br />
<a href="/services/sql/">sql</a><br />
<a href="/services/tags/">tags</a><br />
<a href="/services/vectorsearch/">vectorsearch</a><br />
<a href="/services/workspace/">workspace</a><br />
</div>
</div>
