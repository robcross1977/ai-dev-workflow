"""
Project Configuration Utilities

This module provides utilities for loading and validating project configuration
across all AI Development Workflow scripts.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

class ProjectConfig:
    """Handles loading and accessing project configuration."""
    
    def __init__(self, config_path: str = "project-config.json"):
        """
        Initialize project configuration.
        
        Args:
            config_path: Path to the project configuration file
        """
        self.config_path = config_path
        self._config: Optional[Dict[str, Any]] = None
        
    def load(self) -> Dict[str, Any]:
        """Load project configuration from file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"Project configuration not found: {self.config_path}\n"
                "Run 'python scripts/setup-project.py' to initialize a project."
            )
        
        try:
            with open(self.config_path, 'r') as f:
                self._config = json.load(f)
            return self._config
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {self.config_path}: {e}")
    
    @property
    def config(self) -> Dict[str, Any]:
        """Get the loaded configuration."""
        if self._config is None:
            self.load()
        return self._config
    
    @property
    def name(self) -> str:
        """Get project name."""
        return self.config["name"]
    
    @property
    def type(self) -> str:
        """Get project type (nextjs or unity)."""
        return self.config["type"]
    
    @property
    def language(self) -> str:
        """Get primary language (typescript or csharp)."""
        return self.config["language"]
    
    @property
    def framework(self) -> str:
        """Get framework (nextjs or unity)."""
        return self.config["framework"]
    
    @property
    def data_fetching(self) -> Optional[str]:
        """Get data fetching approach (trpc or swr, NextJS only)."""
        return self.config.get("dataFetching")
    
    @property
    def directories(self) -> Dict[str, str]:
        """Get directory structure."""
        return self.config.get("directories", {})
    
    @property
    def src_dir(self) -> str:
        """Get source directory path."""
        return self.directories.get("src", "src")
    
    @property
    def tests_dir(self) -> str:
        """Get tests directory path."""
        return self.directories.get("tests", "tests")
    
    @property
    def docs_dir(self) -> str:
        """Get documentation directory path."""
        return self.directories.get("docs", "docs")
    
    @property
    def features_dir(self) -> str:
        """Get features directory path."""
        return self.directories.get("features", "docs/features")
    
    @property
    def planning_dir(self) -> str:
        """Get planning directory path."""
        return self.directories.get("planning", "docs/planning")
    
    @property
    def scripts_dir(self) -> str:
        """Get scripts directory path."""
        return self.directories.get("scripts", "scripts")
    
    @property
    def repository(self) -> Dict[str, str]:
        """Get repository information."""
        return self.config.get("repository", {})
    
    @property
    def repo_owner(self) -> str:
        """Get repository owner."""
        return self.repository.get("owner", "")
    
    @property
    def repo_name(self) -> str:
        """Get repository name."""
        return self.repository.get("name", "")
    
    @property
    def repo_url(self) -> str:
        """Get repository URL."""
        return self.repository.get("url", "")
    
    def get_file_extension(self) -> str:
        """Get the appropriate file extension for the project language."""
        if self.language == "typescript":
            return ".ts"
        elif self.language == "csharp":
            return ".cs"
        else:
            return ".txt"
    
    def get_test_file_extension(self) -> str:
        """Get the appropriate test file extension for the project language."""
        if self.language == "typescript":
            return ".test.ts"
        elif self.language == "csharp":
            return ".cs"  # Unity test files are also .cs
        else:
            return ".test.txt"
    
    def get_component_path(self, component_name: str) -> str:
        """
        Get the path where a component should be created.
        
        Args:
            component_name: Name of the component
            
        Returns:
            Path where the component should be created
        """
        if self.type == "nextjs":
            return f"{self.src_dir}/components/{component_name}.tsx"
        elif self.type == "unity":
            return f"{self.src_dir}/{component_name}.cs"
        else:
            return f"{self.src_dir}/{component_name}{self.get_file_extension()}"
    
    def get_test_path(self, component_name: str) -> str:
        """
        Get the path where a test file should be created.
        
        Args:
            component_name: Name of the component being tested
            
        Returns:
            Path where the test file should be created
        """
        if self.type == "nextjs":
            return f"{self.tests_dir}/unit/{component_name}.test.ts"
        elif self.type == "unity":
            return f"{self.tests_dir}/EditMode/{component_name}Tests.cs"
        else:
            return f"{self.tests_dir}/{component_name}{self.get_test_file_extension()}"
    
    def get_api_path(self, endpoint_name: str) -> str:
        """
        Get the path where an API endpoint should be created.
        
        Args:
            endpoint_name: Name of the API endpoint
            
        Returns:
            Path where the API endpoint should be created
        """
        if self.type == "nextjs":
            return f"{self.src_dir}/app/api/{endpoint_name}/route.ts"
        else:
            return f"{self.src_dir}/api/{endpoint_name}{self.get_file_extension()}"
    
    def save(self) -> None:
        """Save the current configuration back to file."""
        if self._config is None:
            raise ValueError("No configuration loaded to save")
        
        with open(self.config_path, 'w') as f:
            json.dump(self._config, f, indent=2)

def load_project_config(config_path: str = "project-config.json") -> ProjectConfig:
    """
    Load project configuration from file.
    
    Args:
        config_path: Path to the project configuration file
        
    Returns:
        ProjectConfig instance
    """
    config = ProjectConfig(config_path)
    config.load()
    return config

def ensure_project_root() -> None:
    """
    Ensure we're running from the project root directory.
    
    Raises:
        FileNotFoundError: If project-config.json is not found in current directory
    """
    if not os.path.exists("project-config.json"):
        raise FileNotFoundError(
            "No project configuration found in current directory.\n"
            "Please run this script from the project root directory."
        )

def get_project_info() -> Dict[str, str]:
    """
    Get basic project information for display purposes.
    
    Returns:
        Dictionary with project name, type, language, and framework
    """
    config = load_project_config()
    return {
        "name": config.name,
        "type": config.type,
        "language": config.language,
        "framework": config.framework,
        "data_fetching": config.data_fetching or "N/A"
    } 