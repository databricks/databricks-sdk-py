We happily welcome contributions to the Databricks SDK for Python. We use [GitHub Issues](github.com/databricks/databricks-sdk-py/issues) to track community reported issues and [GitHub Pull Requests](https://github.com/databricks/databricks-sdk-py/pulls) for accepting changes.
Contributions are licensed on a license-in/license-out basis.

# Contributing Guide

## Communication
Before starting work on a major feature, please open a GitHub issue. We will make sure no one else is already working on it and that it is aligned with the goals of the project.
A "major feature" is defined as any change that is > 100 LOC altered (not including tests), or changes any user-facing behavior.
We will use the GitHub issue to discuss the feature and come to agreement.
This is to prevent your time being wasted, as well as ours.
The GitHub review process for major features is also important so that organizations with commit access can come to agreement on design.
If it is appropriate to write a design document, the document must be hosted either in the GitHub tracking issue, or linked to from the issue and hosted in a world-readable location.
Small patches and bug fixes don't need prior communication.

## Coding Style

Code style is enforced by a formatter check in your pull request. We use [Black](https://github.com/psf/black) to format our code. Run `make fmt` to ensure your code is properly formatted prior to raising a pull request.

## Signed Commits
This repo requires all contributors to sign their commits. To configure this, you can follow [Github's documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) to create a GPG key, upload it to your Github account, and configure your git client to sign commits.

## Developer Certificate of Origin

To contribute to this repository, you must sign off your commits to certify 
that you have the right to contribute the code and that it complies with the 
open source license. The rules are pretty simple, if you can certify the 
content of [DCO](./DCO), then simply add a "Signed-off-by" line to your 
commit message to certify your compliance. Please use your real name as 
pseudonymous/anonymous contributions are not accepted.

```
Signed-off-by: Joe Smith <joe.smith@email.com>
```

If you set your `user.name` and `user.email` git configs, you can sign your 
commit automatically with `git commit -s`:

```
git commit -s -m "Your commit message"
```
