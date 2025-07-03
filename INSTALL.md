# Installation Guide

This guide provides multiple ways to install and use the AI Development Workflow package.

## Quick Start

### Option 1: Install from PyPI (Recommended)

```bash
# Install the package globally
pip install ai-dev-workflow

# Or install with optional dependencies
pip install ai-dev-workflow[dev,github]
```

### Option 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/robcross1977/ai-dev-workflow.git
cd ai-dev-workflow

# Install in development mode
pip install -e .

# Or install with optional dependencies
pip install -e .[dev,github]
```

### Option 3: Use as a Project Template

```bash
# Create a new project from this template
git clone https://github.com/robcross1977/ai-dev-workflow.git my-new-project
cd my-new-project

# Remove the git history and start fresh
rm -rf .git
git init

# Install the package locally
pip install -e .
```

## Setting Up Cursor Integration

### 1. Copy Cursor Configuration

After installation, copy the Cursor configuration to your global settings:

```bash
# On Windows
cp .cursor/settings.json %APPDATA%/Cursor/User/settings.json

# On macOS
cp .cursor/settings.json ~/Library/Application\ Support/Cursor/User/settings.json

# On Linux
cp .cursor/settings.json ~/.config/Cursor/User/settings.json
```

### 2. Configure Cursor for AI Development Workflow

The `.cursor/settings.json` file includes:

- AI context about the workflow package
- Coding standards and rules
- Python development settings
- File exclusions and formatting preferences

### 3. Add Project-Specific Rules

For each project using this workflow:

1. **Copy the template `.cursor` directory**:

   ```bash
   cp -r /path/to/ai-dev-workflow/.cursor ./
   ```

2. **Update project-specific settings** in `.cursor/settings.json`

3. **Cursor will automatically**:
   - Understand your project structure
   - Generate appropriate feature templates
   - Follow your coding standards
   - Provide relevant AI suggestions

## Usage Examples

### Creating a New Project

```bash
# Start interactive setup
ai-workflow setup

# Follow prompts to configure:
# - Project name and type (NextJS/Unity)
# - GitHub repository
# - Data fetching approach (for NextJS)
```

### Generating Features

```bash
# Generate a feature template
ai-workflow feature user-authentication --issue 123

# This creates: docs/features/user-authentication.md
# With comprehensive task breakdown and file paths
```

### Validation and Progress

```bash
# Check all feature files
ai-workflow validate --all

# List features with progress
ai-workflow list

# Show project information
ai-workflow info
```

## Integration with Development Tools

### GitHub CLI

Install GitHub CLI for repository management:

```bash
# On Windows (using winget)
winget install GitHub.cli

# On macOS (using Homebrew)
brew install gh

# On Linux (using apt)
sudo apt install gh

# Authenticate
gh auth login
```

### Node.js (for NextJS projects)

```bash
# Install Node.js 18+ and npm
# Then install global tools
npm install -g create-next-app @playwright/test vitest
```

### Unity (for Unity projects)

1. Install Unity Hub and Unity Editor
2. Ensure Unity Test Framework is available
3. Configure Unity to use external script editor (optional)

## Troubleshooting

### Common Issues

**1. Import errors after installation**

```bash
# Ensure you're using the correct Python environment
which python
pip list | grep ai-dev-workflow

# Reinstall if needed
pip uninstall ai-dev-workflow
pip install ai-dev-workflow
```

**2. CLI commands not found**

```bash
# Check if scripts are in PATH
echo $PATH

# Reinstall with user flag if needed
pip install --user ai-dev-workflow
```

**3. GitHub authentication issues**

```bash
# Check GitHub CLI authentication
gh auth status

# Re-authenticate if needed
gh auth login
```

**4. Cursor not recognizing configuration**

- Ensure `.cursor/settings.json` is in your project root
- Restart Cursor after adding configuration
- Check Cursor's output panel for any errors

### Getting Help

1. **Check the documentation**: Review `README.md` and `.cursor/docs.md`
2. **Validate your setup**: Run `ai-workflow info` to check configuration
3. **Check logs**: Look for error messages in terminal output
4. **Create an issue**: Report bugs on the GitHub repository

## Development Setup

If you want to contribute to the package:

```bash
# Clone and setup development environment
git clone https://github.com/robcross1977/ai-dev-workflow.git
cd ai-dev-workflow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Format code
black ai_dev_workflow/
flake8 ai_dev_workflow/
```

## Next Steps

After installation:

1. **Start with a new project**: Run `ai-workflow setup`
2. **Read the documentation**: Check `.cursor/docs.md` for Cursor integration details
3. **Generate your first feature**: Use `ai-workflow feature` to create a template
4. **Customize as needed**: Modify templates and configurations for your workflow

The AI Development Workflow is designed to grow with your needs and can be customized for different project types and team preferences.
