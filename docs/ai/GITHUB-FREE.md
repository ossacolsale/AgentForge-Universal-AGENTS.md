# GitHub Free resource policy

Apply this policy to public and private repositories when designing or running GitHub workflows, storing outputs, or distributing software.

## Services and quotas

Consult current official GitHub documentation before choosing a service or estimating usage. Check the plan, repository visibility, and the owner's usage and budgets when available.

| Service | Use and billing scope | Official reference |
| --- | --- | --- |
| Actions runners | Execute jobs. Standard GitHub-hosted runner execution is free in public repositories. Eligible private compute draws from the owner's allowance. Check the rules for larger and self-hosted runners separately. | [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) |
| Actions artifacts | Keep workflow outputs for job handoffs, diagnostics, or required evidence. The storage allowance is shared with Packages. | [Workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) |
| Actions cache | Reuse regenerable files across runs when it saves work. Cache has a separate per-repository allowance and eviction rules. | [Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) |
| GitHub Releases | Distribute versioned software and its user-facing assets. Check release limits and access. | [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) |
| GitHub Packages | Host versioned packages or container images. Check registry-specific storage and transfer rules. | [Packages billing](https://docs.github.com/en/billing/concepts/product-billing/github-packages) |
| Git LFS | Track large versioned files with Git pointers. Check the separate storage and bandwidth quotas. | [Git LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs) |

The owning personal account or organization shares account-level allowances across its private repositories. A single repository cannot guarantee remaining capacity. Label any project size, runtime, or retention target as an internal threshold and keep it distinct from official quotas. Before adding a costly workflow, document expected runs per month, job count and duration by runner type, output size and retention, and estimated monthly compute, storage, and transfer where relevant. State assumptions and any unknown account headroom.

## Workflows

- Prefer targeted local tests during development. Skip remote runs whose only purpose is to repeat validation available locally. Preserve required CI, security checks, and necessary tests. Add costly remote pipelines to private repositories only for a concrete, documented need.
- Keep lightweight CI, distribution builds, and publication separately triggered or gated. Use selective events and branch, tag, or path filters while keeping required checks runnable. Avoid running equivalent checks on both `push` and `pull_request` for the same branch update. Use `concurrency` to cancel superseded CI where safe and set a job `timeout-minutes` appropriate to its work. [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

## Storage and distribution

- Keep private-repository artifacts small and upload only files needed for an explicit handoff, diagnosis, or required evidence. Avoid bulk uploads of `dist`, `build`, `node_modules`, virtual environments, runtimes, and dependencies. Set a short `retention-days` for intermediate artifacts. One to seven days is a suggested internal range when it covers the need and meets applicable requirements. [Artifact retention](https://docs.github.com/en/actions/tutorials/store-and-share-data#configuring-a-custom-artifact-retention-period)
- Prefer GitHub Releases for genuine versioned distribution assets, within the applicable terms, use policies, and release limits. Preserve distributed releases, tags, and assets unless there is a concrete reason to remove them and explicit authorization. [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) · [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)
- Keep private repositories private when reducing resource use. Obtain explicit authorization before introducing paid services or enabling billable usage.
