#!/usr/bin/env python3
"""
AI Development Workflow Project Setup Script

This script initializes a new project with the standardized folder structure,
configuration files, and initial setup based on user preferences.
"""

import os
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

def prompt_user() -> Dict[str, Any]:
    """Prompt user for project configuration details."""
    print("🚀 AI Development Workflow - Project Setup")
    print("=" * 50)
    
    # Project name
    project_name = input("\n📁 Project name (lowercase, hyphens allowed): ").strip()
    while not project_name or not project_name.replace('-', '').replace('_', '').isalnum():
        print("❌ Invalid name. Use lowercase letters, numbers, hyphens only.")
        project_name = input("📁 Project name: ").strip()
    
    # Project type
    print("\n🔧 Project type:")
    print("1. NextJS Web App")
    print("2. Unity Game")
    
    project_type_choice = input("Choose (1 or 2): ").strip()
    while project_type_choice not in ['1', '2']:
        print("❌ Please choose 1 or 2")
        project_type_choice = input("Choose (1 or 2): ").strip()
    
    project_type = "nextjs" if project_type_choice == "1" else "unity"
    language = "typescript" if project_type == "nextjs" else "csharp"
    framework = project_type
    
    # Data fetching for NextJS
    data_fetching = None
    if project_type == "nextjs":
        print("\n📡 Data fetching approach:")
        print("1. tRPC (type-safe APIs)")
        print("2. SWR (data fetching)")
        
        data_choice = input("Choose (1 or 2): ").strip()
        while data_choice not in ['1', '2']:
            print("❌ Please choose 1 or 2")
            data_choice = input("Choose (1 or 2): ").strip()
        
        data_fetching = "trpc" if data_choice == "1" else "swr"
    
    # Repository details
    print(f"\n🐙 GitHub Repository (will be created as: username/{project_name})")
    repo_owner = input("GitHub username/organization: ").strip()
    while not repo_owner:
        print("❌ Repository owner is required")
        repo_owner = input("GitHub username/organization: ").strip()
    
    repo_name = input(f"Repository name [{project_name}]: ").strip() or project_name
    
    return {
        "name": project_name,
        "type": project_type,
        "language": language,
        "framework": framework,
        "dataFetching": data_fetching,
        "repository": {
            "owner": repo_owner,
            "name": repo_name,
            "url": f"https://github.com/{repo_owner}/{repo_name}"
        },
        "createdAt": datetime.now().isoformat(),
        "version": "1.0.0"
    }

def get_directory_structure(project_type: str) -> Dict[str, str]:
    """Get the directory structure based on project type."""
    base_dirs = {
        "docs": "docs",
        "scripts": "scripts",
        "features": "docs/features",
        "planning": "docs/planning"
    }
    
    if project_type == "nextjs":
        return {
            **base_dirs,
            "src": "src",
            "tests": "tests"
        }
    else:  # unity
        return {
            **base_dirs,
            "src": "Assets/Scripts",
            "tests": "Assets/Tests"
        }

def create_folder_structure(config: Dict[str, Any]) -> None:
    """Create the standardized folder structure."""
    project_type = config["type"]
    project_name = config["name"]
    
    print(f"\n📂 Creating folder structure for {project_type} project...")
    
    # Create project root directory
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    
    directories = get_directory_structure(project_type)
    config["directories"] = directories
    
    # Create base directories
    for dir_type, path in directories.items():
        os.makedirs(path, exist_ok=True)
        print(f"  ✅ Created: {path}/")
    
    # Create project-specific directories
    if project_type == "nextjs":
        nextjs_dirs = [
            "src/app",
            "src/app/api",
            "src/components",
            "src/lib",
            "src/types",
            "tests/unit",
            "tests/e2e",
            "public"
        ]
        for dir_path in nextjs_dirs:
            os.makedirs(dir_path, exist_ok=True)
            print(f"  ✅ Created: {dir_path}/")
    
    elif project_type == "unity":
        unity_dirs = [
            "Assets/Scripts/Player",
            "Assets/Scripts/UI", 
            "Assets/Scripts/Managers",
            "Assets/Scripts/Utils",
            "Assets/Scenes",
            "Assets/Prefabs",
            "Assets/Materials",
            "Assets/Textures",
            "Assets/Audio",
            "Assets/Tests/EditMode",
            "Assets/Tests/PlayMode",
            "ProjectSettings"
        ]
        for dir_path in unity_dirs:
            os.makedirs(dir_path, exist_ok=True)
            print(f"  ✅ Created: {dir_path}/")

def create_initial_files(config: Dict[str, Any]) -> None:
    """Create initial project files."""
    project_type = config["type"]
    project_name = config["name"]
    
    print(f"\n📄 Creating initial files...")
    
    # Create project-config.json
    with open("project-config.json", "w") as f:
        json.dump(config, f, indent=2)
    print("  ✅ Created: project-config.json")
    
    # Create README.md
    readme_content = f"""# {project_name.title()}

{config['type'].upper()} project created with AI Development Workflow.

## Project Info

- **Type**: {config['type'].title()}
- **Language**: {config['language'].title()}
- **Framework**: {config['framework'].title()}
{'- **Data Fetching**: ' + config.get('dataFetching', '').upper() if config.get('dataFetching') else ''}

## Getting Started

TODO: Add setup instructions

## Development Workflow

This project uses the AI Development Workflow with Mastra for automated feature development.

### Commands

TODO: Add common commands

## Structure

TODO: Document folder structure

## Contributing

TODO: Add contribution guidelines
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("  ✅ Created: README.md")
    
    # Create .gitignore
    if project_type == "nextjs":
        gitignore_content = """# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Next.js
.next/
out/
build/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log

# Runtime data
pids/
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/

# Dependency directories
node_modules/
jspm_packages/

# Mastra
.mastra/logs/
.mastra/temp/
"""
    else:  # unity
        gitignore_content = """# Unity generated files
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]ser[Ss]ettings/

# MemoryCaptures
[Mm]emoryCaptures/

# Asset meta data
*.pidb
*.booproj
*.svd
*.pdb
*.mdb
*.opendb
*.VC.db

# Unity3D generated meta files
*.pidb.meta
*.pdb.meta
*.mdb.meta

# Unity3D generated file on crash reports
sysinfo.txt

# Builds
*.apk
*.aab
*.unitypackage
*.app

# Crashlytics generated file
crashlytics-build.properties

# Autogenerated VS/MD/Consulo solution and project files
ExportedObj/
.consulo/
*.csproj
*.unityproj
*.sln
*.suo
*.tmp
*.user
*.userprefs
*.pidb
*.booproj
*.svd
*.pdb
*.mdb
*.opendb
*.VC.db

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Mastra
.mastra/logs/
.mastra/temp/
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    print("  ✅ Created: .gitignore")
    
    # Create .env.example for NextJS
    if project_type == "nextjs":
        env_example = """# Environment variables template
# Copy this file to .env.local and fill in your values

# Database
DATABASE_URL=""

# Authentication (if using)
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET=""

# API Keys
# Add your API keys here
"""
        with open(".env.example", "w") as f:
            f.write(env_example)
        print("  ✅ Created: .env.example")

def initialize_git_repo(config: Dict[str, Any]) -> None:
    """Initialize git repository and create remote."""
    print(f"\n🐙 Initializing Git repository...")
    
    try:
        # Initialize git repo
        subprocess.run(["git", "init"], check=True, capture_output=True)
        print("  ✅ Initialized git repository")
        
        # Add all files
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        print("  ✅ Added files to git")
        
        # Initial commit
        subprocess.run([
            "git", "commit", "-m", "Initial project setup with AI Development Workflow"
        ], check=True, capture_output=True)
        print("  ✅ Created initial commit")
        
        # Check if gh CLI is available
        try:
            subprocess.run(["gh", "--version"], check=True, capture_output=True)
            
            # Create GitHub repository
            repo_name = config["repository"]["name"]
            subprocess.run([
                "gh", "repo", "create", repo_name, "--public", "--confirm"
            ], check=True, capture_output=True)
            print(f"  ✅ Created GitHub repository: {config['repository']['url']}")
            
            # Push to remote
            subprocess.run([
                "git", "push", "-u", "origin", "main"
            ], check=True, capture_output=True)
            print("  ✅ Pushed to GitHub")
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("  ⚠️  GitHub CLI not available. You'll need to create the repository manually:")
            print(f"     Repository: {config['repository']['url']}")
            print("     Then run: git remote add origin <repo-url> && git push -u origin main")
    
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Git operation failed: {e}")
        print("  You may need to set up git configuration or check repository permissions")

def main():
    """Main setup function."""
    try:
        # Check if we're already in a project directory
        if os.path.exists("project-config.json"):
            print("❌ This directory already contains a project configuration.")
            print("Please run this script from a different location.")
            return 1
        
        # Get user input
        config = prompt_user()
        
        # Validate project name doesn't exist
        if os.path.exists(config["name"]):
            print(f"❌ Directory '{config['name']}' already exists.")
            return 1
        
        # Create folder structure
        create_folder_structure(config)
        
        # Create initial files
        create_initial_files(config)
        
        # Initialize git repository
        initialize_git_repo(config)
        
        print(f"\n🎉 Project '{config['name']}' created successfully!")
        print(f"📁 Location: {os.path.abspath('.')}")
        print(f"🔗 Repository: {config['repository']['url']}")
        print("\n📋 Next steps:")
        print("1. cd into your project directory")
        print("2. Install dependencies (npm install for NextJS)")
        print("3. Set up your development environment")
        print("4. Start building features with the AI workflow!")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        return 1
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 