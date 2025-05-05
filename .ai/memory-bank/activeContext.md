# Active Context

## Current Work Focus
- Establishing and populating the Memory Bank documentation for the btcrecover GUI project.
- Prioritizing documentation of the proof-of-concept steps for 25th word (BIP39 passphrase) recovery using the CLI.

## Recent Changes
- Added a top-level Security Considerations section to productContext.md, requiring careful handling of partial seeds and passphrase fragments.

## Next Steps
1. Fill in systemPatterns.md, techContext.md, and progress.md with initial project context.
2. Document the CLI workflow for 25th word recovery as the first actionable item after Memory Bank setup.

## Active Decisions and Considerations
- Security is a top-level requirement: all sensitive data must be handled with care and never leave the user's machine.
- The GUI must be accessible to non-technical users, with advanced options hidden by default.

## Important Patterns and Preferences
- Documentation-first workflow: Memory Bank is the single source of truth for project context and progress.
- Stepwise, user-friendly recovery process.

## Learnings and Project Insights
- Early focus on documentation and security requirements will guide both CLI and GUI development.
- The CLI workflow for 25th word recovery is foundational for the GUI feature set.
