Below is a comprehensive file that outlines a reusable AI development workflow using Mastra for Cursor, including a pre-script for project setup, a detailed workflow with sanity checks, and automation to minimize manual work. The workflow is designed to be reusable across projects, with a focus on modularity, automation, and integration with Cursor's AI features (Cursor Tab, Cursor Composer) and external tools (GitHub, testing frameworks). The pre-script sets up the project architecture, folder structure, coding standards, and Cursor rules, feeding metadata into Mastra for seamless execution.

---

# AI Development Workflow with Mastra in Cursor

This document defines a reusable AI development workflow for software projects using Mastra, integrated with Cursor's AI capabilities (Cursor Tab, Cursor Composer) and GitHub for version control. The workflow includes a pre-script for project setup, a feature development pipeline with sanity checks, and automation to minimize manual intervention. It's designed to be portable across projects, with configurable parameters for different languages, frameworks, and environments.

## Table of Contents

- [AI Development Workflow with Mastra in Cursor](#ai-development-workflow-with-mastra-in-cursor)
  - [Table of Contents](#table-of-contents)
  - [Pre-Script: Project Setup](#pre-script-project-setup)
    - [Steps](#steps)
    - [Output Files](#output-files)
  - [AI-Assisted Feature Planning](#ai-assisted-feature-planning)
    - [Steps](#steps-1)
    - [Output Files](#output-files-1)
    - [Benefits](#benefits)
  - [Feature Development Workflow](#feature-development-workflow)
    - [Steps](#steps-2)
  - [Sanity Checks](#sanity-checks)
  - [Mastra Configuration](#mastra-configuration)
    - [`.mastra/mastra-config.yaml`](#mastramastra-configyaml)
    - [`.mastra/workflows/feature-workflow.yaml`](#mastraworkflowsfeature-workflowyaml)
    - [`.mastra/workflows/planning-workflow.yaml`](#mastraworkflowsplanning-workflowyaml)
    - [Supporting Scripts](#supporting-scripts)
      - [Planning Scripts](#planning-scripts)
      - [Development Scripts](#development-scripts)
  - [Automation and Reusability](#automation-and-reusability)
  - [Implementation in Cursor](#implementation-in-cursor)
  - [Overview](#overview)
  - [Tasks](#tasks)
  - [Acceptance Criteria](#acceptance-criteria)
  - [Files to Create/Modify](#files-to-createmodify)
  - [Example Usage](#example-usage)
  - [Notes](#notes)
  - [Implementation Status](#implementation-status)
    - [What Needs to be Built:](#what-needs-to-be-built)
    - [Recommended Implementation Approach:](#recommended-implementation-approach)
    - [Current Limitations:](#current-limitations)

---

## Pre-Script: Project Setup

The pre-script initializes a new project with a standardized architecture, folder structure, coding standards, and Cursor rules. It generates metadata files that Mastra uses to understand the project structure and place files correctly.

### Steps

1. **Prompt for Project Details**:

   - Use Cursor's Composer to prompt the user for:
     - Project name (e.g., `my-app`).
     - Project type: Choose between "NextJS Web App" or "Unity Game".
     - For NextJS projects: Choose data fetching approach - "tRPC" or "SWR".
     - GitHub repository name (e.g., `username/my-app`).
   - Defaults applied automatically:
     - **NextJS projects**: TypeScript, Vitest (unit tests), Playwright (E2E tests), ESLint + Prettier (default configs).
     - **Unity projects**: C#, Unity Test Framework (built-in tests).
     - **Git host**: Always GitHub.
     - **Coding standards**: Default ESLint and Prettier configurations (no customization).
   - Output: A `project-config.json` file with these details.

2. **Create Folder Structure**:

   - Generate a standardized folder structure based on the framework:

   **NextJS Project Structure**:

   ```
   my-app/
   ├── src/                    # Source code
   │   ├── app/               # App Router (NextJS 13+)
   │   │   ├── api/          # API routes
   │   │   ├── globals.css   # Global styles
   │   │   ├── layout.tsx    # Root layout
   │   │   └── page.tsx      # Home page
   │   ├── components/        # Reusable UI components
   │   ├── lib/              # Utility functions and configurations
   │   └── types/            # TypeScript type definitions
   ├── tests/                 # Unit and E2E tests
   │   ├── unit/
   │   └── e2e/
   ├── docs/                  # Documentation
   │   ├── features/         # Feature Markdown files
   │   ├── completed/        # Completed feature files
   │   └── planning/         # Planning documents
   ├── scripts/               # Automation scripts
   ├── .mastra/              # Mastra workflow configs
   ├── .gitignore
   ├── README.md
   ├── package.json
   ├── tailwind.config.js     # Tailwind CSS config
   ├── next.config.js         # NextJS config
   ├── .env.example           # Environment variables template
   └── project-config.json    # Project metadata
   ```

   **Unity Project Structure**:

   ```
   my-game/
   ├── Assets/
   │   ├── Scripts/           # C# game scripts
   │   │   ├── Player/       # Player-related scripts
   │   │   ├── UI/           # UI scripts
   │   │   ├── Managers/     # Game managers
   │   │   └── Utils/        # Utility scripts
   │   ├── Scenes/           # Unity scenes
   │   ├── Prefabs/          # Prefabricated objects
   │   ├── Materials/        # 3D materials
   │   ├── Textures/         # Image textures
   │   ├── Audio/            # Sound effects and music
   │   └── Tests/            # Unity Test Framework tests
   │       ├── EditMode/     # Edit mode tests
   │       └── PlayMode/     # Play mode tests
   ├── ProjectSettings/       # Unity project settings
   ├── docs/                  # Documentation
   │   ├── features/         # Feature Markdown files
   │   ├── completed/        # Completed feature files
   │   └── planning/         # Planning documents
   ├── scripts/               # Automation scripts
   ├── .mastra/              # Mastra workflow configs
   ├── .gitignore
   ├── README.md
   └── project-config.json    # Project metadata
   ```

   - **Automation**: Use a script (e.g., `setup-project.sh`) to create directories and files.
   - **Output**: Folder structure and initial files (e.g., `README.md`, `.gitignore`).

3. **Set Up Coding Standards**:

   - Install linters/formatters (e.g., ESLint, Prettier for JS; Black, Flake8 for Python).
   - Configure Cursor rules:
     - Enable Cursor Tab for inline autocomplete suggestions.
     - Configure Cursor Composer for AI-assisted code generation and refactoring.
     - Configure tab settings, auto-save, and file exclusions.
   - **Output**: `.eslintrc.json`, `.prettierrc`, `.cursor/settings.json`.

4. **Initialize Git Repository**:

   - Run `git init`, `git add .`, and `git commit -m "Initial project setup"`.
   - Create a remote repository (e.g., via `gh repo create` for GitHub).
   - **Output**: Initialized Git repo with remote.

5. **Generate Mastra Metadata**:

   - Create a `mastra-config.yaml` in `.mastra/` with:
     - Project structure (e.g., where to place source files, tests).
     - Testing commands (e.g., `npm test`, `pytest`).
     - Git integration details (e.g., repository URL, PR template).
   - Example for NextJS project:
     ```yaml
     project:
       name: my-app
       type: nextjs
       language: typescript
       framework: nextjs
       dataFetching: trpc # or swr
       srcDir: src
       testDir: tests
       featureDir: docs/features
       git:
         host: github
         repo: user/my-app
       tests:
         unit: npm run test # vitest
         e2e: npm run test:e2e # playwright
       linting:
         eslint: default
         prettier: default
     ```
   - Example for Unity project:
     ```yaml
     project:
       name: my-game
       type: unity
       language: csharp
       framework: unity
       srcDir: Assets/Scripts
       testDir: Assets/Tests
       featureDir: docs/features
       git:
         host: github
         repo: user/my-game
       tests:
         unit: Unity Test Runner
         playmode: Unity Test Runner (Play Mode)
     ```
   - **Output**: `.mastra/mastra-config.yaml`.

6. **Install Dependencies**:

   - Install project dependencies (e.g., `npm install` for Node.js, `pip install -r requirements.txt` for Python).
   - Install testing frameworks and Mastra CLI.
   - **Output**: Installed dependencies and Mastra CLI.

7. **Sanity Check**:
   - Verify folder structure, Git repo, and dependencies.
   - Run linters and initial tests (if any).
   - Prompt user to confirm setup:
     - **If rejected**: Collect feedback, adjust `project-config.json`, and loop back to Step 2.
     - **If accepted**: Proceed to feature development.
   - **Automation**: Script checks for missing files, uncommitted changes, or dependency errors.

### Output Files

- `project-config.json`: Project metadata (name, language, framework, etc.).
- `.mastra/mastra-config.yaml`: Mastra configuration for workflow execution.
- `.cursor/settings.json`: Cursor-specific rules.
- Linter/formatter configs (e.g., `.eslintrc.json`, `.prettierrc`).
- Initial Git commit and remote repository.

---

## AI-Assisted Feature Planning

This planning phase uses AI to analyze your project architecture and create a comprehensive feature roadmap. It identifies dependencies, potential overlaps, and generates all necessary artifacts to enable parallel feature development.

### Steps

1. **Architecture Analysis**:

   - Use Cursor's Composer to analyze the current project structure:
     - Scan existing codebase for patterns, components, and modules.
     - Identify data models, API endpoints, UI components, and services.
     - Map out current dependencies and relationships.
   - Generate `docs/planning/architecture-map.md` with:
     - Project structure diagram (using Mermaid).
     - Key components and their responsibilities.
     - Data flow and API structure.
     - Existing patterns and conventions.
   - **Mastra Task**: `analyze-architecture`.

2. **Feature Requirements Gathering**:

   - Prompt user for high-level feature list or import from GitHub Issues/Product backlog.
   - Use Cursor's Composer to expand each feature into detailed requirements:
     - User stories and acceptance criteria.
     - Technical requirements and constraints.
     - UI/UX considerations.
     - Data requirements and API needs.
   - **Output**: `docs/planning/feature-requirements.md`.
   - **Mastra Task**: `gather-requirements`.

3. **AI-Powered Impact Analysis**:

   - For each feature, use AI to analyze:
     - **File Impact**: Which existing files will be modified.
     - **New Artifacts**: What new files/components need to be created.
     - **Dependencies**: What other features or components this depends on.
     - **Conflicts**: Potential overlaps with other planned features.
     - **Testing Strategy**: What types of tests are needed.
   - Generate `docs/planning/impact-analysis.md` with detailed breakdown.
   - **Mastra Task**: `analyze-impact`.

4. **Dependency Graph Generation**:

   - Use AI to create a feature dependency graph:
     - Identify which features can be developed in parallel.
     - Determine optimal development order.
     - Highlight blocking dependencies.
     - Suggest feature groupings for sprint planning.
   - Generate `docs/planning/dependency-graph.md` with Mermaid diagram.
   - **Mastra Task**: `generate-dependency-graph`.

5. **Artifact Planning**:

   - For each feature, generate a comprehensive artifact list:
     - **Code Files**: Specific file paths and their purposes.
     - **Test Files**: Unit, integration, and E2E test files needed.
     - **Documentation**: API docs, component docs, user guides.
     - **Configuration**: Environment variables, config files, migrations.
     - **Assets**: Images, icons, styles, or other resources.
   - Create `docs/planning/artifacts-manifest.md`.
   - **Mastra Task**: `plan-artifacts`.

6. **Parallel Development Strategy**:

   - Use AI to group features into development batches:
     - **Batch 1**: Independent features with no overlaps.
     - **Batch 2**: Features dependent on Batch 1 completion.
     - **Batch N**: Subsequent batches based on dependencies.
   - For each batch, identify:
     - Shared components that need to be created first.
     - Integration points between features.
     - Testing strategies for the batch.
   - Generate `docs/planning/development-batches.md`.
   - **Mastra Task**: `plan-parallel-development`.

7. **Feature Template Generation**:

   - For each feature, pre-generate the feature markdown template:
     - Tasks broken down by artifact type.
     - File paths pre-populated based on project architecture.
     - Test requirements specified.
     - Dependencies clearly marked.
   - Save templates in `docs/features/templates/`.
   - **Mastra Task**: `generate-feature-templates`.

8. **Manual Review and Approval**:
   - Present the complete planning package to user:
     - Architecture map and impact analysis.
     - Dependency graph and development batches.
     - Artifact manifest and feature templates.
   - Allow user to:
     - Adjust feature priorities or groupings.
     - Modify dependency relationships.
     - Add/remove features from batches.
   - **If changes needed**: Update planning documents and regenerate affected artifacts.
   - **If approved**: Proceed to batch development.
   - **Mastra Task**: `review-planning`.

### Output Files

- `docs/planning/architecture-map.md`: Current project structure and patterns.
- `docs/planning/feature-requirements.md`: Detailed feature specifications.
- `docs/planning/impact-analysis.md`: File and dependency impact for each feature.
- `docs/planning/dependency-graph.md`: Visual dependency relationships.
- `docs/planning/artifacts-manifest.md`: Complete list of artifacts needed.
- `docs/planning/development-batches.md`: Parallel development strategy.
- `docs/features/templates/<feature>.md`: Pre-generated feature templates.

### Benefits

- **Parallel Development**: Multiple features can be developed simultaneously without conflicts.
- **Reduced Rework**: Dependencies and impacts identified upfront.
- **Better Estimation**: Clear artifact lists enable accurate time estimates.
- **Consistent Architecture**: AI ensures new features follow existing patterns.
- **Comprehensive Testing**: Test strategies planned for each feature and batch.

---

## Feature Development Workflow

This workflow automates feature development, from branch creation to PR merging, with sanity checks to ensure correctness. It uses Mastra to orchestrate tasks and Cursor's AI for code/test generation. Features can be developed individually or in parallel batches based on the planning phase.

### Steps

1. **Create Feature Branch**:

   - Run `git checkout -b feature/<issue-id>-<feature-name>` based on `project-config.json`.
   - Push to remote (`git push origin feature/<feature-name>`).
   - **Mastra Task**: `create-branch`.

2. **Define Feature Requirements**:

   - Prompt user for feature details (or fetch from GitHub Issues/Jira).
   - Use Cursor's Composer to generate `docs/features/<feature>.md` with:
     - Tasks with checkboxes (e.g., `- [ ] Implement login API in src/api/login.js`).
     - Unit and E2E tests (e.g., `- [ ] Unit test: Validate login response`).
     - Acceptance criteria and edge cases.
   - **Mastra Task**: `generate-feature-md`.
   - **Automation**: Parse issue description or user input to create tasks.

3. **Manual Verification of Task Plan**:

   - Prompt user to review `<feature>.md` in Cursor.
     - **If adjustments needed**: Edit `<feature>.md` and loop back to Step 2.
     - **If approved**: Proceed to Step 4.
   - **Mastra Task**: `verify-task-plan`.
   - **Automation**: Send review request via Slack/Teams or Cursor UI.

4. **Sanity Check: Task Plan Completeness**:

   - Check `<feature>.md` for:
     - At least one task.
     - Tests defined for each task.
     - Clear file paths for implementation.
   - **If check fails**: Notify user, loop back to Step 2.
   - **Mastra Task**: `sanity-check-task-plan`.

5. **Implement Tasks Iteratively**:

   - For each unchecked task in `<feature>.md`:
     - **Write Code**: Use Cursor Tab for autocomplete or Cursor Composer for code generation in the specified file.
     - **Write Tests**: Generate unit/E2E tests in `tests/unit/` or `tests/e2e/`.
     - **Run Tests**: Execute tests via Mastra (e.g., `npm test`).
       - **If tests pass**: Mark task as complete (`- [x]`).
       - **If tests fail**: Use Cursor Composer to suggest fixes, apply, and re-run tests.
     - Commit changes (`git add .`, `git commit -m "Implement <task>"`).
   - **Mastra Task**: `implement-task`.
   - **Automation**: Loop through tasks automatically, updating `<feature>.md`.

6. **Sanity Check: Feature Implementation**:

   - Verify all tasks are checked off.
   - Run full test suite (unit + E2E).
   - Check code against linters/formatters.
   - **If check fails**: Identify failed task/test, loop back to Step 5.
   - **Mastra Task**: `sanity-check-implementation`.

7. **Manual Verification of Feature Completion**:

   - Prompt user to review feature (e.g., via local demo or screenshots).
     - **If rejected**: Collect feedback, update `<feature>.md`, loop back to Step 2.
     - **If accepted**: Proceed to Step 8.
   - **Mastra Task**: `verify-feature`.

8. **Finalize and Submit for Review**:

   - **Stage and Commit**: Run `git add .`, `git commit -m "Implement <feature-name>"`.
   - **Create PR**: Use `gh pr create` with a template from `<feature>.md`.
   - **Request Reviews**:
     - Enable GitHub Copilot code review on the PR (automatically triggered).
   - **Handle Feedback**:
     - **GitHub Copilot Feedback**:
       - If changes needed: Implement, commit, and re-request review.
       - If not needed: Comment why and resolve thread.
   - **Mastra Task**: `submit-pr`, `handle-reviews`.

9. **Sanity Check: PR Readiness**:

   - Verify:
     - All tests pass.
     - Linters/formatters report no issues.
     - PR has at least one approval.
   - **If check fails**: Loop back to Step 5 or 8 based on issue.
   - **Mastra Task**: `sanity-check-pr`.

10. **Merge PR and Cleanup**:
    - Merge PR via `gh pr merge`.
    - Delete branch (`git branch -d feature/<feature-name>`).
    - Archive `<feature>.md` to `docs/features/completed/`.
    - Update changelog or documentation.
    - **Mastra Task**: `merge-and-cleanup`.

---

## Sanity Checks

Sanity checks ensure correctness at key stages, reducing errors and rework.

1. **Task Plan Completeness (Step 4)**:

   - Checks: Tasks defined, tests specified, file paths valid.
   - Action on failure: Notify user, loop back to Step 2.

2. **Feature Implementation (Step 6)**:

   - Checks: All tasks complete, tests pass, linters clean.
   - Action on failure: Identify issue, loop back to Step 5.

3. **PR Readiness (Step 9)**:

   - Checks: Tests pass, linters clean, PR approved.
   - Action on failure: Loop back to Step 5 or 8.

4. **Post-Merge Validation**:
   - Checks: Branch deleted, `<feature>.md` archived, changelog updated.
   - Action on failure: Notify user, loop back to Step 10.

---

## Mastra Configuration

Mastra orchestrates the workflow using a reusable configuration. Below is an example `mastra-config.yaml` and workflow file.

### `.mastra/mastra-config.yaml`

```yaml
project:
  name: ${projectName}
  type: ${projectType} # nextjs or unity
  language: ${language} # typescript or csharp
  framework: ${framework} # nextjs or unity
  dataFetching: ${dataFetching} # trpc or swr (NextJS only)
  srcDir: ${srcDir} # src for NextJS, Assets/Scripts for Unity
  testDir: ${testDir} # tests for NextJS, Assets/Tests for Unity
  featureDir: docs/features
  completedDir: docs/features/completed
  planningDir: docs/planning
  templatesDir: docs/features/templates
  git:
    host: github
    repo: ${user}/${projectName}
  tests:
    unit: ${unitTestCommand} # npm run test or Unity Test Runner
    e2e: ${e2eTestCommand} # npm run test:e2e or Unity Test Runner (Play Mode)
  linting:
    eslint: default # NextJS only
    prettier: default # NextJS only
  notifications:
    slack: ${slackWebhook}
```

### `.mastra/workflows/feature-workflow.yaml`

```yaml
name: FeatureDevelopment
parameters:
  featureName: string
  issueId: string
steps:
  - name: create-branch
    run: git checkout -b feature/${issueId}-${featureName} && git push origin feature/${issueId}-${featureName}
  - name: generate-feature-md
    run: python scripts/generate_feature_md.py --feature ${featureName} --issue ${issueId}
    output: docs/features/${featureName}.md
  - name: verify-task-plan
    run: scripts/verify_task_plan.sh
    onFailure: notify --message "Task plan verification failed" --slack
  - name: sanity-check-task-plan
    run: scripts/check_task_plan.py
    onFailure: notify --message "Task plan incomplete" --slack
  - name: implement-task
    loop: tasks in docs/features/${featureName}.md
    steps:
      - run: python scripts/implement_task.py --task "${task.description}" --file "${task.file}"
      - run: python scripts/generate_tests.py --task "${task.description}" --test-file "${task.testFile}"
      - run: ${project.tests.unit} && ${project.tests.e2e}
        onFailure: python scripts/fix_failing_tests.py --file "${task.file}" --error "${testError}"
      - run: git add . && git commit -m "Implement ${task.description}"
  - name: sanity-check-implementation
    run: scripts/check_implementation.py
    onFailure: notify --message "Implementation check failed" --slack
  - name: verify-feature
    run: scripts/verify_feature.sh
    onFailure: notify --message "Feature verification failed" --slack
  - name: submit-pr
    run: gh pr create --title "Implement ${featureName}" --body-file docs/features/${featureName}.md
  - name: handle-reviews
    run: scripts/handle_reviews.py
    onFailure: notify --message "Review failed" --slack
  - name: sanity-check-pr
    run: scripts/check_pr.py
    onFailure: notify --message "PR not ready" --slack
  - name: merge-and-cleanup
    run: |
      gh pr merge
      git branch -d feature/${issueId}-${featureName}
      mv docs/features/${featureName}.md docs/features/completed/
      scripts/update_changelog.py
```

### `.mastra/workflows/planning-workflow.yaml`

```yaml
name: FeaturePlanning
parameters:
  featureList: array # List of feature names or GitHub issue IDs
steps:
  - name: analyze-architecture
    run: python scripts/analyze_architecture.py
    output: docs/planning/architecture-map.md
  - name: gather-requirements
    run: python scripts/gather_requirements.py --features "${featureList}"
    output: docs/planning/feature-requirements.md
  - name: analyze-impact
    run: python scripts/analyze_impact.py --requirements docs/planning/feature-requirements.md
    output: docs/planning/impact-analysis.md
  - name: generate-dependency-graph
    run: python scripts/generate_dependency_graph.py --impact docs/planning/impact-analysis.md
    output: docs/planning/dependency-graph.md
  - name: plan-artifacts
    run: python scripts/plan_artifacts.py --requirements docs/planning/feature-requirements.md --architecture docs/planning/architecture-map.md
    output: docs/planning/artifacts-manifest.md
  - name: plan-parallel-development
    run: python scripts/plan_parallel_development.py --dependencies docs/planning/dependency-graph.md --artifacts docs/planning/artifacts-manifest.md
    output: docs/planning/development-batches.md
  - name: generate-feature-templates
    run: python scripts/generate_feature_templates.py --batches docs/planning/development-batches.md --artifacts docs/planning/artifacts-manifest.md
    output: docs/features/templates/
  - name: review-planning
    run: scripts/review_planning.sh
    onFailure: notify --message "Planning review failed - adjustments needed" --slack
```

### Supporting Scripts

#### Planning Scripts

- `scripts/analyze_architecture.py`: Analyzes codebase structure and generates architecture map.
- `scripts/gather_requirements.py`: Expands feature list into detailed requirements.
- `scripts/analyze_impact.py`: Analyzes file and dependency impact for each feature.
- `scripts/generate_dependency_graph.py`: Creates feature dependency graph with Mermaid.
- `scripts/plan_artifacts.py`: Generates comprehensive artifact manifest.
- `scripts/plan_parallel_development.py`: Groups features into parallel development batches.
- `scripts/generate_feature_templates.py`: Pre-generates feature markdown templates.
- `scripts/review_planning.sh`: Prompts user for planning review and approval.

#### Development Scripts

- `scripts/generate_feature_md.py`: Generates `<feature>.md` templates.
- `scripts/implement_task.py`: Assists with code implementation for specific tasks.
- `scripts/generate_tests.py`: Creates test files and basic test structures.
- `scripts/fix_failing_tests.py`: Analyzes test failures and suggests fixes.
- `scripts/verify_task_plan.sh`: Prompts user for task plan approval.
- `scripts/check_task_plan.py`: Validates `<feature>.md` structure.
- `scripts/check_implementation.py`: Checks task completion and test status.
- `scripts/verify_feature.sh`: Prompts user for feature demo approval.
- `scripts/handle_reviews.py`: Processes GitHub Copilot feedback.
- `scripts/check_pr.py`: Verifies PR readiness.
- `scripts/update_changelog.py`: Updates project changelog.

---

## Automation and Reusability

To make the workflow reusable across projects:

1. **Template Repository**:

   - Create a GitHub template repository with:
     - `.mastra/` directory and configs.
     - `scripts/` directory with reusable scripts.
     - Default `project-config.json` and folder structure.
   - Clone this template for new projects.

2. **Parameterized Configs**:

   - Use variables in `mastra-config.yaml` (e.g., `${projectName}`, `${language}`) to adapt to different projects.
   - Allow user input to override defaults during setup.

3. **Script Modularity**:

   - Write scripts to read `project-config.json` for project-specific details.
   - Example: `generate_feature_md.py` uses `project.language` to tailor code generation.

4. **Mastra Reusability**:

   - Store `feature-workflow.yaml` in the template repository.
   - Use Mastra's CLI to apply the workflow to any project (`mastra run feature-workflow --feature login`).

5. **Automation**:
   - Integrate with GitHub Actions to trigger Mastra workflows on issue creation or PR updates.
   - Use Slack webhooks for notifications (e.g., review requests, failures).
   - Leverage Cursor's Composer to generate code/tests dynamically.

---

## Implementation in Cursor

1. **Install Mastra**:

   - Run `npm install -g @mastra/cli` or equivalent in Cursor's terminal.
   - Initialize Mastra in the project: `mastra init`.

2. **Set Up Scripts**:

   - Place scripts in `scripts/` and make them executable (`chmod +x`).
   - Example `generate_feature_md.py`:

     ```python
     import json
     import os

     def generate_feature_template(feature_name, project_config):
         """Generate a basic feature template based on project configuration."""
         template = f"""# {feature_name.title()} Feature
     ```

## Overview

Implementation of {feature_name} feature for {project_config['name']}.

## Tasks

- [ ] Create {feature_name} component/script in {project_config['srcDir']}
- [ ] Implement core {feature_name} functionality
- [ ] Add unit tests in {project_config['testDir']}
- [ ] Add integration tests if needed
- [ ] Update documentation

## Acceptance Criteria

- Feature works as expected
- All tests pass
- Code follows project standards

## Files to Create/Modify

- `{project_config['srcDir']}/{feature_name}.{project_config['language']}`
- `{project_config['testDir']}/{feature_name}.test.{project_config['language']}`
  """
  return template

       with open("project-config.json") as f:
           config = json.load(f)

       feature = input("Enter feature name: ")
       tasks = generate_feature_template(feature, config)

       os.makedirs("docs/features", exist_ok=True)
       with open(f"docs/features/{feature}.md", "w") as f:
           f.write(tasks)

       print(f"Generated feature template: docs/features/{feature}.md")
       ```

3. **Run Workflow**:

   - Execute `mastra run feature-workflow --feature <feature-name> --issue <issue-id>` in Cursor's terminal.
   - Monitor progress in Mastra's dashboard or Cursor's terminal output.

4. **Use Cursor's AI**:

   - Enable Cursor Tab for inline autocomplete suggestions.
   - Use Cursor Composer for AI-assisted code generation and refactoring through the UI.
   - Configure `.cursor/settings.json` to optimize AI behavior.

5. **Git Integration**:
   - Use Cursor's Git panel or `gh` CLI for branch/PR management.
   - Automate PR creation with Mastra tasks.

---

## Example Usage

1. **Create New Project**:

   ```bash
   git clone <template-repo> my-app
   cd my-app
   ./scripts/setup-project.sh
   ```

   - Follow prompts to set project type (NextJS/Unity), data fetching approach, etc.
   - Output: Initialized project with `project-config.json`, `.mastra/mastra-config.yaml`.

2. **Run Feature Planning** (Recommended for multiple features):

   ```bash
   mastra run planning-workflow --featureList "user-auth,dashboard,notifications,settings"
   ```

   - Analyzes project architecture and generates planning documents.
   - Creates dependency graph and development batches.
   - Generates pre-templated feature markdown files.
   - Output: Complete planning package in `docs/planning/` and templates in `docs/features/templates/`.

3. **Run Parallel Feature Development** (After planning):

   ```bash
   # Batch 1 - Independent features (can run simultaneously)
   mastra run feature-workflow --template docs/features/templates/user-auth.md &
   mastra run feature-workflow --template docs/features/templates/settings.md &

   # Batch 2 - Dependent features (run after Batch 1 completes)
   mastra run feature-workflow --template docs/features/templates/dashboard.md &
   mastra run feature-workflow --template docs/features/templates/notifications.md &
   ```

4. **Run Single Feature Development** (Traditional approach):

   ```bash
   mastra run feature-workflow --feature login --issue 123
   ```

   - Creates branch `feature/123-login`.
   - Generates `docs/features/login.md`.
   - Executes tasks, tests, and PR process.

5. **Handle Feedback**:

   - Mastra notifies via Slack for manual reviews or failures.
   - Use Cursor to edit code/tests based on GitHub Copilot feedback.

6. **Merge and Cleanup**:
   - Mastra merges PRs, deletes branches, and archives completed features.

---

## Notes

- **Dependencies**: Install Mastra CLI, GitHub CLI (`gh`), and project-specific tools (e.g., npm, pip).
- **Security**: Store API keys (e.g., GitHub, Slack) in `.env` and exclude from Git.
- **Extensibility**: Add new Mastra tasks for additional steps (e.g., deployment, documentation).
- **Error Handling**: Mastra's `onFailure` hooks ensure robust recovery.

## Implementation Status

**Current Status**: This workflow document represents a comprehensive plan that requires implementation.

### What Needs to be Built:

1. **All Python scripts** referenced in the workflows (16+ scripts total)
2. **Mastra integration testing** to verify workflow execution capabilities
3. **Cursor AI integration scripts** that work with Cursor's actual APIs/capabilities
4. **Project setup automation** for both NextJS and Unity projects

### Recommended Implementation Approach:

1. **Phase 1**: Build basic project setup scripts and folder structure automation
2. **Phase 2**: Create simple feature template generation (manual process initially)
3. **Phase 3**: Integrate with Mastra for workflow orchestration
4. **Phase 4**: Add AI-assisted planning and analysis features

### Current Limitations:

- Cursor Composer integration is manual (no CLI automation available)
- AI-powered architecture analysis requires custom implementation
- Dependency graph generation needs sophisticated parsing tools
- Parallel development coordination requires careful conflict detection

For specific script implementations or Mastra config tweaks, provide your project details (language, framework, Git host), and I can generate tailored code!
