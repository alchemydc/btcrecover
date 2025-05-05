# Security Testing Plan

## 1. Preparation
- Define audit scope and goals (e.g., focus on seed/passphrase handling, file I/O, subprocess, cryptography).
- Set up a clean environment with all dependencies installed.

## 2. Automated Static Analysis
- Install and run Bandit:
  - `pip install bandit`
  - `bandit -r .`
- Review results for high/medium severity issues.

## 3. Manual Code Review
- Examine code for:
  - Hardcoded secrets or credentials.
  - Unsafe use of eval/exec or dynamic imports.
  - Insecure file operations and temp file handling.
  - Input validation and error handling.
  - Secure cryptographic usage.
- Focus on btcrecover.py, seedrecover.py, and any code handling user secrets.

## 4. Dependency Audit
- Install and run pip-audit:
  - `pip install pip-audit`
  - `pip-audit`
- Alternatively, use Safety:
  - `pip install safety`
  - `safety check`
- Review and update any vulnerable packages.

## 5. Data Flow and Logging Review
- Ensure no sensitive data is logged, printed, or sent over the network.
- Check for telemetry, analytics, or update-checking code.

## 6. Configuration and Defaults
- Confirm secure defaults (no debug mode, no open ports, no world-writable files).

## 7. Testing
- Run all available tests to ensure no regressions or security issues are introduced.

## 8. Documentation
- Document all findings, rate severity, and provide remediation recommendations.
