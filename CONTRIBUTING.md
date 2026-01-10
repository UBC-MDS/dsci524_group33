# Contributing

The following document outlines how each team member will contribute to
the project on this repository, as a part of the UBC Master of Data
Science program. Each member will follow the same guideline to ensure
code quality, reproducibility and smooth collaboration.

## Collaboration Strategy

-   The `main` branch always contains stable and working code
-   All work is done on `branches` created from `main`
-   Changes are merged into `main` using a PR (Pull Request), which
    should include:
    -   at least one team member for review
    -   a short description of what was changed
    -   how it has to be tested
-   After testing, the `branch` can be merged into `main` and can be
    deleted to keep the repository clean.

### Branching

Each task is done on its own branch, and all the branches are deleted
after being merged.

### Issues and Project Management

-   Github issues are used to plan, track and discuss work
-   Issues are grouped according to Milestones
-   Each issue is assigned to one team member
-   Project boards are used to keep track of the progress

### Commits

Commits should be frequent and should clearly state how the solution was
managed. All the contributors are expected to collect a comparable
number of commits throughout the project.

## Pull Requests

Changes are merged to `main` through a Pull Request. - PR should
include: - brief description to changes - any relevant verification
steps - Each PR should be assigned for review to at least one other team
member - PR feedback should be commented before merging to `main`

## Getting Started

### Clone the repository

``` bash
git clone <https://github.com/UBC-MDS/dsci524_group33.git>
```

### Create a new branch

``` bash
git switch -c <branch_name>
```

### Commit changes

``` bash
git add <files> git commit -m "Add a brief and descriptive message"
```

### Push changes to the branch

``` bash
git push origin <branch_name>
```

### Create a PR

Open a Pull Request on GitHub, link the issue, request a review from at
least one teammate and address the feedback before merging.

## Code of Conduct

All the team members are expected to follow those guidelines to support
an effective collaboration ([code of
conduct](https://github.com/UBC-MDS/dsci524_group33/blob/main/CODE_OF_CONDUCT.md))
