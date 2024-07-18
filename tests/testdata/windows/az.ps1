#!/usr/bin/env pwsh

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
