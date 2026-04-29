# Security Policy

## Supported Versions

The `main` branch is the supported development line for security fixes and dependency updates.

## Reporting A Vulnerability

Do not open public issues for suspected secrets, credential exposure, or exploitable vulnerabilities. Contact the repository maintainer privately with:

- A short description of the issue.
- Steps to reproduce or confirm it.
- Affected files, dependencies, or workflows.
- Any recommended mitigation.

## Security Controls

This repository includes:

- `.gitignore` rules for `.env`, raw datasets, logs, checkpoints, and model binaries.
- `.env.example` for non-secret configuration.
- Bandit static security scanning in CI.
- `pip-audit` dependency vulnerability checks in CI.
- CodeQL Python analysis.
- Dependabot updates for Python packages and GitHub Actions.

## Data And Model Artifact Handling

Raw EMNIST files, generated samples, trained models, experiment databases, and logs should remain outside version control unless explicitly approved and documented.
