# GitHub Team Workflow

This document defines the GitHub collaboration standards for the WealthWise RAG Assistant project.

## 1. Branching Strategy

- The `main` branch contains only stable and releasable code.
- Every new feature or bug fix must be developed in a separate branch.
- Feature branches follow the naming convention `feature/short-description`.
- Other supported branch types include `fix/`, `docs/`, `refactor/`, and `chore/`.
- Branches should be deleted after successful merging.

## 2. Commit Message Convention

All commits must follow this format:

`[type]: [description]`

Supported commit types:

- `feat`: New features.
- `fix`: Bug fixes.
- `docs`: Documentation changes.
- `refactor`: Code restructuring.
- `chore`: Maintenance tasks.

Commit messages should be short, meaningful, and descriptive.

This convention maintains a clear project history and enables automated changelog generation.

## 3. Pull Request Review Process

- All changes must be submitted through Pull Requests.
- At least one approval is required before merging.
- Code reviews must focus on correctness, clarity, data integrity, and test coverage.
- Reviewers must also check commit message consistency.
- Pull Requests should clearly explain the purpose of the changes.

## 4. GitHub Issue Tracking

- Every new feature or bug fix must start with a GitHub Issue.
- Each issue must have a descriptive title and clear acceptance criteria.
- Issues must have appropriate labels and an assigned team member.
- Related issues must be linked in Pull Requests.
- Issues are closed when their corresponding Pull Requests are merged.