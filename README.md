# Vulnerable Python Application

## Overview

This repository contains a Python application intentionally designed to be vulnerable, specifically for educational purposes and to demonstrate automated security scanning and pull request handling within a CI/CD pipeline using GitHub Actions. It incorporates security scanning with Bandit for Python code, automated pull request reviews based on scan results, and GitHub Advanced Security features.

**Warning**: The code in this repository is intentionally vulnerable and should **not** be used in production environments or as a base for developing applications. It is designed strictly for educational and testing purposes.

## Automated Security Scanning

This project uses GitHub Actions to automate security scanning on every pull request. The workflow includes:

- **Bandit Scanning**: Analyzes Python code for security issues.
- **Pull Request Handling**: Automatically blocks or merges pull requests based on the security scan results.
- **SBOM Generation**: Generates a Software Bill of Materials (SBOM) upon merge to the main branch.

## GitHub Advanced Security

GitHub Advanced Security is enabled for this repository to enhance code scanning capabilities and provide detailed security alerts.

## Fetching Code Scanning Alerts

A Python script is available to fetch and analyze code scanning alerts from the GitHub API, focusing on alerts with high or critical severity. This script is intended for use by repository maintainers to monitor and address potential vulnerabilities identified in the codebase.

## Security

This repository is for educational purposes and demonstrates both vulnerabilities and their detection/mitigation through automated tools. If you discover a security issue, please report it responsibly.
