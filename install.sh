#!/bin/bash

# AI Development Workflow - Quick Install Script
# Run with: curl -sSL https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/main/install.sh | bash

set -e

echo "🚀 Installing AI Development Workflow..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_color() {
    printf "${2}${1}${NC}\n"
}

print_color "Installing AI Development Workflow package..." "$BLUE"

# Check if Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    print_color "❌ Python is required but not installed. Please install Python 3.7+" "$RED"
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

print_color "✅ Found Python: $($PYTHON_CMD --version)" "$GREEN"

# Check if pip is available
if ! $PYTHON_CMD -m pip --version &> /dev/null; then
    print_color "❌ pip is required but not available. Please install pip." "$RED"
    exit 1
fi

print_color "✅ Found pip: $($PYTHON_CMD -m pip --version)" "$GREEN"

# Install the package
print_color "📦 Installing ai-dev-workflow..." "$BLUE"

# Try to install from PyPI first, fallback to GitHub
if $PYTHON_CMD -m pip install ai-dev-workflow; then
    print_color "✅ Successfully installed from PyPI" "$GREEN"
else
    print_color "⚠️  PyPI installation failed, trying GitHub..." "$YELLOW"
    if $PYTHON_CMD -m pip install git+https://github.com/robcross1977/ai-dev-workflow.git; then
        print_color "✅ Successfully installed from GitHub" "$GREEN"
    else
        print_color "❌ Installation failed. Please check your internet connection and try again." "$RED"
        exit 1
    fi
fi

# Verify installation
if command -v ai-workflow &> /dev/null; then
    print_color "✅ ai-workflow command is available" "$GREEN"
else
    print_color "⚠️  ai-workflow command not found in PATH. You may need to restart your terminal." "$YELLOW"
    print_color "Or add ~/.local/bin to your PATH if using --user installation." "$YELLOW"
fi

print_color "🎉 AI Development Workflow installed successfully!" "$GREEN"

echo ""
print_color "Next steps:" "$BLUE"
echo "1. Start a new project: ai-workflow setup"
echo "2. Generate a feature: ai-workflow feature <name>"
echo "3. Check project info: ai-workflow info"
echo ""
print_color "For Cursor integration:" "$BLUE"
echo "1. Copy .cursor/settings.json to your Cursor settings"
echo "2. Add .cursor directory to your projects"
echo "3. Read .cursor/docs.md for detailed instructions"
echo ""
print_color "Documentation: https://github.com/robcross1977/ai-dev-workflow#readme" "$BLUE"
print_color "Support: https://github.com/robcross1977/ai-dev-workflow/issues" "$BLUE"

# Optional: Install common development tools
echo ""
read -p "Would you like to install optional development tools (GitHub CLI, Node.js tools)? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_color "📦 Installing optional tools..." "$BLUE"
    
    # Check for GitHub CLI
    if ! command -v gh &> /dev/null; then
        print_color "Installing GitHub CLI..." "$BLUE"
        # Platform-specific installation
        if [[ "$OSTYPE" == "darwin"* ]]; then
            if command -v brew &> /dev/null; then
                brew install gh
            else
                print_color "⚠️  Homebrew not found. Please install GitHub CLI manually." "$YELLOW"
            fi
        elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
            if command -v apt &> /dev/null; then
                sudo apt update && sudo apt install gh
            elif command -v yum &> /dev/null; then
                sudo yum install gh
            else
                print_color "⚠️  Please install GitHub CLI manually for your distribution." "$YELLOW"
            fi
        else
            print_color "⚠️  Please install GitHub CLI manually for your platform." "$YELLOW"
        fi
    else
        print_color "✅ GitHub CLI already installed" "$GREEN"
    fi
    
    # Check for Node.js (for NextJS projects)
    if ! command -v node &> /dev/null; then
        print_color "⚠️  Node.js not found. Please install Node.js 18+ for NextJS projects." "$YELLOW"
        print_color "Visit: https://nodejs.org/" "$BLUE"
    else
        print_color "✅ Node.js found: $(node --version)" "$GREEN"
        
        # Install global npm packages
        if command -v npm &> /dev/null; then
            print_color "Installing global npm packages..." "$BLUE"
            npm install -g create-next-app @playwright/test vitest
        fi
    fi
fi

print_color "🎉 Setup complete! Happy coding!" "$GREEN" 