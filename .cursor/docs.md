# AI Development Workflow - Cursor Integration Guide

This document provides Cursor AI with context about the AI Development Workflow package and how to work with it effectively.

## Package Overview

The AI Development Workflow is a Python package that automates project setup and feature development for NextJS and Unity projects. It provides:

- **Automated Project Setup**: Creates standardized folder structures
- **Feature Template Generation**: Comprehensive task breakdowns
- **Validation Tools**: Ensures feature completeness
- **CLI Interface**: Easy-to-use commands
- **Progress Tracking**: Visual progress monitoring

## Key Components

### 1. Project Configuration (`ai_dev_workflow/config.py`)

- `ProjectConfig` class: Central configuration management
- `load_project_config()`: Loads project settings from JSON
- Path generation methods for different file types
- Cross-platform path handling

### 2. Project Setup (`ai_dev_workflow/setup.py`)

- Interactive project initialization
- NextJS and Unity folder structure creation
- Git repository setup with GitHub integration
- Configuration file generation

### 3. Feature Management (`ai_dev_workflow/feature.py`)

- `generate_nextjs_feature_template()`: NextJS-specific templates
- `generate_unity_feature_template()`: Unity-specific templates
- Comprehensive task breakdowns with file paths
- Testing strategy integration

### 4. Validation (`ai_dev_workflow/validation.py`)

- `TaskPlanValidator` class: Feature file validation
- Structure completeness checking
- File path validation
- Progress tracking capabilities

### 5. CLI Interface (`ai_dev_workflow/cli.py`)

- Unified command interface
- Subcommands: setup, feature, validate, info, list
- Error handling and user feedback

## Working with This Package

### When Adding New Features

1. Use the `ProjectConfig` class for accessing settings
2. Add proper docstrings and type hints
3. Include comprehensive error handling
4. Follow the established CLI patterns
5. Add validation for user inputs
6. Include tests for new functionality

### Code Style Guidelines

- Use descriptive names (no abbreviations except common ones)
- Keep functions under 15 lines when possible
- Use declarative programming style (list comprehensions, etc.)
- Single responsibility per function/class
- Comprehensive docstrings for public APIs

### Template Generation Patterns

When creating feature templates:

- Include specific file paths based on project type
- Break down tasks into actionable items
- Include testing requirements
- Add acceptance criteria
- Specify files to create/modify
- Include technical notes and examples

### Project Type Handling

The package supports two project types:

- **NextJS**: TypeScript, React, App Router, tRPC/SWR
- **Unity**: C#, MonoBehaviour, GameObject/Prefab patterns

Always check `config.type` and generate appropriate templates.

### Error Handling Patterns

- Use meaningful error messages
- Validate inputs early
- Provide helpful suggestions for fixes
- Use try/except blocks for external operations
- Return proper exit codes from CLI commands

## CLI Command Structure

```bash
ai-workflow setup                    # Interactive project setup
ai-workflow feature <name> [--issue] # Generate feature template
ai-workflow validate [--all | file]  # Validate feature files
ai-workflow info                     # Show project information
ai-workflow list                     # List features with progress
```

## File Structure Patterns

### NextJS Projects

```
src/
├── app/           # App Router
├── components/    # React components
├── lib/          # Utilities
└── types/        # TypeScript definitions
tests/
├── unit/         # Vitest tests
└── e2e/          # Playwright tests
```

### Unity Projects

```
Assets/
├── Scripts/      # C# scripts
├── Scenes/       # Unity scenes
├── Prefabs/      # GameObjects
└── Tests/        # Unity Test Framework
```

## Integration with Cursor

This package is designed to work seamlessly with Cursor:

1. **Code Generation**: Templates provide specific file paths for Cursor to work with
2. **Task Tracking**: Markdown files can be opened in Cursor for progress tracking
3. **Validation**: Built-in validation ensures code meets standards
4. **CLI Integration**: Can be run from Cursor's terminal

## Common Operations

### Setting Up a New Project

```python
# In Cursor's terminal:
ai-workflow setup
# Follow prompts for project type and configuration
```

### Generating Features

```python
# Generate a feature template:
ai-workflow feature user-authentication --issue 123
# Opens docs/features/user-authentication.md in Cursor
```

### Validating Work

```python
# Check all feature files:
ai-workflow validate --all
# Shows validation results in terminal
```

## Extension Points

When extending this package:

- Add new project types by extending the setup and feature generation
- Add new validation rules in the TaskPlanValidator class
- Add new CLI commands following the established patterns
- Include new template types for different frameworks

The package is designed to be modular and extensible while maintaining consistency across all operations.
