# AI Development Workflow Implementation

This repository contains the practical implementation of the AI Development Workflow for NextJS and Unity projects. This is a **Phase 1** implementation focusing on project setup and basic feature management.

## 🚀 Quick Start

### Installation

**One-liner installation:**

```bash
# Unix/Linux/macOS
curl -sSL https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/main/install.sh | bash

# Windows PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/main/install.ps1" -OutFile "install.ps1"; .\install.ps1
```

**Or install via pip:**

```bash
# Install from PyPI
pip install ai-dev-workflow

# Install with optional dependencies
pip install ai-dev-workflow[dev,github]
```

**Or install from source:**

```bash
git clone https://github.com/robcross1977/ai-dev-workflow.git
cd ai-dev-workflow
pip install -e .
```

### 1. Set Up a New Project

```bash
# Use the global command
ai-workflow setup

# Or if installed from source
python scripts/setup-project.py
```

Follow the prompts to configure:

- Project name and type (NextJS or Unity)
- Data fetching approach (tRPC or SWR for NextJS)
- GitHub repository details

### 2. Generate Your First Feature

```bash
# Using the global CLI
ai-workflow feature user-authentication --issue 123

# Or if installed from source
python scripts/ai-workflow feature user-authentication --issue 123
```

### 3. Validate Feature Files

```bash
# Validate all feature files
ai-workflow validate --all

# Validate specific file
ai-workflow validate docs/features/user-auth.md
```

### 4. Cursor Integration

Copy the Cursor configuration to enable AI assistance:

```bash
# Copy to your project
cp -r .cursor ./my-project/

# The .cursor/settings.json tells Cursor about your workflow patterns
# The .cursor/docs.md provides context for AI assistance
```

## 📁 What Gets Created

### Project Structure (NextJS)

```
my-app/
├── src/
│   ├── app/              # NextJS App Router
│   ├── components/       # React components
│   ├── lib/             # Utilities
│   └── types/           # TypeScript definitions
├── tests/
│   ├── unit/            # Unit tests (Vitest)
│   └── e2e/             # E2E tests (Playwright)
├── docs/
│   ├── features/        # Feature markdown files
│   └── planning/        # Planning documents
├── scripts/             # Workflow automation scripts
└── project-config.json  # Project metadata
```

### Project Structure (Unity)

```
my-game/
├── Assets/
│   ├── Scripts/         # C# game scripts
│   ├── Scenes/          # Unity scenes
│   ├── Prefabs/         # Game objects
│   ├── Tests/           # Unity Test Framework
│   └── ...              # Other Unity assets
├── docs/
│   ├── features/        # Feature markdown files
│   └── planning/        # Planning documents
├── scripts/             # Workflow automation scripts
└── project-config.json  # Project metadata
```

## 🛠️ Available Tools

### CLI Interface

```bash
# Setup new project
python scripts/ai-workflow setup

# Generate feature template
python scripts/ai-workflow feature <name> [--issue <id>]

# Validate feature files
python scripts/ai-workflow validate [--all | <file>]

# Show project information
python scripts/ai-workflow info

# List all features with progress
python scripts/ai-workflow list
```

### Individual Scripts

- `scripts/setup-project.py` - Project initialization
- `scripts/generate_feature_md.py` - Feature template generation
- `scripts/check_task_plan.py` - Feature file validation
- `scripts/utils/project_config.py` - Configuration utilities

## 📋 Feature Templates

The workflow generates comprehensive feature templates tailored to your project type:

### NextJS Features Include:

- Frontend component tasks
- API integration (tRPC or SWR)
- Database/state management
- Unit, integration, and E2E tests
- Accessibility requirements
- Performance considerations

### Unity Features Include:

- Core script implementation
- GameObject and prefab setup
- UI integration
- Game mechanics
- Edit mode and play mode tests
- Asset management

## ✅ Current Implementation Status

### ✅ **Completed (Phase 1)**

- Project setup automation for NextJS and Unity
- Standardized folder structure creation
- Git repository initialization
- Feature template generation
- Basic validation and CLI tools
- Project configuration management

### 🚧 **In Progress/Planned (Phase 2)**

- Mastra workflow integration
- Automated task implementation assistance
- GitHub integration for issues/PRs
- Code generation helpers
- Test automation

### 📋 **Future Phases**

- AI-powered architecture analysis
- Dependency graph generation
- Parallel development coordination
- Advanced code generation
- Full CI/CD integration

## 🔧 Requirements

- Python 3.7+
- Git
- GitHub CLI (`gh`) - optional but recommended
- Node.js (for NextJS projects)
- Unity 2022.3+ (for Unity projects)

## 📖 Usage Examples

### Setting Up a NextJS Project

```bash
python scripts/setup-project.py
# Choose: 1 (NextJS Web App)
# Choose: 1 (tRPC) or 2 (SWR)
# Enter GitHub username and repo name
```

### Creating a Feature

```bash
# Generate authentication feature
python scripts/ai-workflow feature user-auth --issue 45

# This creates: docs/features/user-auth.md
# With sections for:
# - Component implementation
# - API endpoints
# - Testing strategy
# - File paths and structure
```

### Validating Your Work

```bash
# Check all feature files
python scripts/ai-workflow validate --all

# Get project overview
python scripts/ai-workflow info

# See feature progress
python scripts/ai-workflow list
```

## 🤝 Development Workflow

1. **Initialize Project**: Run setup script for standardized structure
2. **Plan Features**: Generate feature templates with clear task breakdowns
3. **Implement**: Follow the task list in your feature markdown files
4. **Validate**: Use validation tools to ensure completeness
5. **Track Progress**: Monitor feature completion with the CLI

## 🐛 Known Limitations

- **Manual Implementation**: Currently requires manual code implementation (Phase 2 will add automation)
- **No Mastra Integration**: Workflow orchestration is manual for now
- **Basic Validation**: File structure validation only, no code analysis yet
- **Limited AI Integration**: Templates are static, not AI-generated

## 🔮 Roadmap

### Phase 2: Automation & Integration

- Mastra workflow orchestration
- Basic code generation assistance
- GitHub API integration
- Automated testing workflows

### Phase 3: AI-Powered Features

- Architecture analysis and recommendations
- Intelligent dependency detection
- AI-assisted code generation
- Advanced project planning tools

## 📄 License

[Add your license here]

## 🤝 Contributing

This is an evolving workflow implementation. Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with improvements

---

**Current Version**: 1.0.0 (Phase 1)  
**Last Updated**: 2024-12-19

For questions or issues, please create a GitHub issue or discussion.
