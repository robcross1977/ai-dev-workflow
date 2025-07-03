# AI Development Workflow - Windows PowerShell Install Script
# Run with: Invoke-WebRequest -Uri "https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/main/install.ps1" -OutFile "install.ps1"; .\install.ps1

param(
    [switch]$SkipOptionalTools
)

# Set error action preference
$ErrorActionPreference = "Stop"

Write-Host "🚀 Installing AI Development Workflow..." -ForegroundColor Blue

# Function to write colored output
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$ForegroundColor = "White"
    )
    Write-Host $Message -ForegroundColor $ForegroundColor
}

# Check if Python is available
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
}

if (-not $pythonCmd) {
    Write-ColorOutput "❌ Python is required but not installed. Please install Python 3.7+" "Red"
    Write-ColorOutput "Download from: https://www.python.org/downloads/" "Yellow"
    exit 1
}

$pythonVersion = & $pythonCmd --version
Write-ColorOutput "✅ Found Python: $pythonVersion" "Green"

# Check if pip is available
try {
    $pipVersion = & $pythonCmd -m pip --version
    Write-ColorOutput "✅ Found pip: $pipVersion" "Green"
} catch {
    Write-ColorOutput "❌ pip is required but not available. Please install pip." "Red"
    exit 1
}

# Install the package
Write-ColorOutput "📦 Installing ai-dev-workflow..." "Blue"

try {
    # Try to install from PyPI first
    & $pythonCmd -m pip install ai-dev-workflow
    Write-ColorOutput "✅ Successfully installed from PyPI" "Green"
} catch {
    Write-ColorOutput "⚠️ PyPI installation failed, trying GitHub..." "Yellow"
    try {
        & $pythonCmd -m pip install git+https://github.com/robcross1977/ai-dev-workflow.git
        Write-ColorOutput "✅ Successfully installed from GitHub" "Green"
    } catch {
        Write-ColorOutput "❌ Installation failed. Please check your internet connection and try again." "Red"
        Write-ColorOutput "Error: $($_.Exception.Message)" "Red"
        exit 1
    }
}

# Verify installation
try {
    $aiWorkflowVersion = & ai-workflow --version 2>$null
    Write-ColorOutput "✅ ai-workflow command is available" "Green"
} catch {
    Write-ColorOutput "⚠️ ai-workflow command not found in PATH. You may need to restart your terminal." "Yellow"
    Write-ColorOutput "Or add Python Scripts directory to your PATH." "Yellow"
}

Write-ColorOutput "🎉 AI Development Workflow installed successfully!" "Green"

Write-Host ""
Write-ColorOutput "Next steps:" "Blue"
Write-Host "1. Start a new project: ai-workflow setup"
Write-Host "2. Generate a feature: ai-workflow feature <name>"
Write-Host "3. Check project info: ai-workflow info"

Write-Host ""
Write-ColorOutput "For Cursor integration:" "Blue"
Write-Host "1. Copy .cursor/settings.json to your Cursor settings"
Write-Host "2. Add .cursor directory to your projects"
Write-Host "3. Read .cursor/docs.md for detailed instructions"

Write-Host ""
Write-ColorOutput "Documentation: https://github.com/robcross1977/ai-dev-workflow#readme" "Blue"
Write-ColorOutput "Support: https://github.com/robcross1977/ai-dev-workflow/issues" "Blue"

# Optional tools installation
if (-not $SkipOptionalTools) {
    Write-Host ""
    $installOptional = Read-Host "Would you like to install optional development tools (GitHub CLI, Node.js tools)? [y/N]"
    
    if ($installOptional -match "^[Yy]") {
        Write-ColorOutput "📦 Installing optional tools..." "Blue"
        
        # Check for GitHub CLI
        if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
            Write-ColorOutput "Installing GitHub CLI..." "Blue"
            
            # Check if winget is available
            if (Get-Command winget -ErrorAction SilentlyContinue) {
                try {
                    winget install GitHub.cli
                    Write-ColorOutput "✅ GitHub CLI installed via winget" "Green"
                } catch {
                    Write-ColorOutput "⚠️ Failed to install GitHub CLI via winget. Please install manually." "Yellow"
                    Write-ColorOutput "Download from: https://cli.github.com/" "Yellow"
                }
            } elseif (Get-Command choco -ErrorAction SilentlyContinue) {
                try {
                    choco install gh
                    Write-ColorOutput "✅ GitHub CLI installed via Chocolatey" "Green"
                } catch {
                    Write-ColorOutput "⚠️ Failed to install GitHub CLI via Chocolatey. Please install manually." "Yellow"
                    Write-ColorOutput "Download from: https://cli.github.com/" "Yellow"
                }
            } else {
                Write-ColorOutput "⚠️ Please install GitHub CLI manually for your platform." "Yellow"
                Write-ColorOutput "Download from: https://cli.github.com/" "Yellow"
            }
        } else {
            Write-ColorOutput "✅ GitHub CLI already installed" "Green"
        }
        
        # Check for Node.js
        if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
            Write-ColorOutput "⚠️ Node.js not found. Please install Node.js 18+ for NextJS projects." "Yellow"
            Write-ColorOutput "Download from: https://nodejs.org/" "Blue"
        } else {
            $nodeVersion = & node --version
            Write-ColorOutput "✅ Node.js found: $nodeVersion" "Green"
            
            # Install global npm packages
            if (Get-Command npm -ErrorAction SilentlyContinue) {
                Write-ColorOutput "Installing global npm packages..." "Blue"
                try {
                    npm install -g create-next-app @playwright/test vitest
                    Write-ColorOutput "✅ Global npm packages installed" "Green"
                } catch {
                    Write-ColorOutput "⚠️ Failed to install some npm packages. You can install them manually later." "Yellow"
                }
            }
        }
    }
}

Write-ColorOutput "🎉 Setup complete! Happy coding!" "Green"

# Pause to let user read the output
Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 