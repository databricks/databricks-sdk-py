---
title: databricks_account
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_account
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

Account-level features, identity and provisioning for Databricks.

:::info

For Databricks workspace operations use the [__`databricks_workspace`__](https://databricks-workspace-provider.stackql.io/) provider.

:::

:::info[Provider Summary]

total services: __8__
total resources: __75__

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL databricks_account;
```

## Authentication

To use the databricks_account, set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/billing/">billing</a><br />
<a href="/services/catalog/">catalog</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/iamv2/">iamv2</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/oauth2/">oauth2</a><br />
<a href="/services/provisioning/">provisioning</a><br />
<a href="/services/settings/">settings</a><br />
<a href="/services/settingsv2/">settingsv2</a><br />
</div>
</div>
