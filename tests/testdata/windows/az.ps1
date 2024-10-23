#!/usr/bin/env pwsh

# If the arguments are "account show", return the account details.
if ($args[0] -eq "account" -and $args[1] -eq "show") {
    $output = @{
        environmentName = "AzureCloud"
        id = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        isDefault = $true
        name = "Pay-As-You-Go"
        state = "Enabled"
        tenantId = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        user = @{
            name = if ($env:AZ_USER_NAME) { $env:AZ_USER_NAME } else { "testuser@databricks.com" }
            type = if ($env:AZ_USER_TYPE) { $env:AZ_USER_TYPE } else { "user" }
        }
    }
    $output | ConvertTo-Json
    exit 0
}

if ($env:WARN) {
    Write-Error "WARNING: $env:WARN"
}

if ($env:FAIL -eq "yes") {
    Write-Error "This is just a failing script."
    exit 1
}

if ($env:FAIL -eq "logout") {
    Write-Error "No subscription found. Run 'az account set' to select a subscription."
    exit 1
}

if ($env:FAIL -eq "corrupt") {
    Write-Output "{accessToken: ..corrupt"
    exit
}

param (
    [string[]]$Args
)

foreach ($arg in $Args) {
    if ($arg -eq $env:FAIL_IF) {
        Write-Output "Failed"
        exit 1
    }
}

# If FAIL_IF_TENANT_ID_SET is set & --tenant-id is passed, fail.
if ($env:FAIL_IF_TENANT_ID_SET) {
    foreach ($arg in $args) {
        if ($arg -eq "--tenant-id" -or $arg -like "--tenant*") {
            Write-Error "ERROR: Tenant shouldn't be specified for managed identity account"
            exit 1
        }
    }
}

try {
    $EXP = (Get-Date).AddSeconds($env:EXPIRE -as [int])
} catch {
    $expireString = $env:EXPIRE
    $expireString = $expireString -replace "S", "seconds"
    $expireString = $expireString -replace "M", "minutes"
    $EXP = (Get-Date).AddSeconds($expireString -as [int])
}

if (-not $env:TF_AAD_TOKEN) {
    $TF_AAD_TOKEN = "..."
} else {
    $TF_AAD_TOKEN = $env:TF_AAD_TOKEN
}

$expiresOn = $EXP.ToString("yyyy-MM-dd HH:mm:ss")

Write-Output "{
  `"accessToken`": `"$TF_AAD_TOKEN`",
  `"expiresOn`": `"$expiresOn`",
  `"subscription`": `"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`",
  `"tenant`": `"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`",
  `"tokenType`": `"Bearer`"
}"
