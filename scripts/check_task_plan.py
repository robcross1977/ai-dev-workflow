#!/usr/bin/env python3
"""
Task Plan Validation Script

This script validates the structure and completeness of feature markdown files
to ensure they follow the expected format and contain all required sections.
"""

import argparse
import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils.project_config import load_project_config, ensure_project_root

class TaskPlanValidator:
    """Validates feature markdown files for completeness and structure."""
    
    def __init__(self, config):
        self.config = config
        self.required_sections = [
            "Overview",
            "Tasks", 
            "Acceptance Criteria",
            "Files to Create/Modify",
            "Definition of Done"
        ]
        
        # Project-specific required subsections
        if config.type == "nextjs":
            self.required_task_subsections = [
                "Frontend Components",
                "API Integration", 
                "Testing"
            ]
        elif config.type == "unity":
            self.required_task_subsections = [
                "Core Scripts",
                "Game Objects & Prefabs",
                "Testing"
            ]
        else:
            self.required_task_subsections = ["Testing"]
    
    def validate_file(self, file_path: str) -> Tuple[bool, List[str]]:
        """
        Validate a feature markdown file.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        if not os.path.exists(file_path):
            return False, [f"File not found: {file_path}"]
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return False, [f"Failed to read file: {e}"]
        
        issues = []
        
        # Check file is not empty
        if not content.strip():
            issues.append("File is empty")
            return False, issues
        
        # Check for required sections
        for section in self.required_sections:
            if f"## {section}" not in content:
                issues.append(f"Missing required section: {section}")
        
        # Check for tasks subsections
        tasks_section = self._extract_section(content, "Tasks")
        if tasks_section:
            for subsection in self.required_task_subsections:
                if f"### {subsection}" not in tasks_section:
                    issues.append(f"Missing required tasks subsection: {subsection}")
        
        # Check for at least one task
        tasks = self._extract_tasks(content)
        if not tasks:
            issues.append("No tasks found. Feature must have at least one task.")
        
        # Check for file paths in tasks
        file_path_issues = self._validate_file_paths(tasks)
        issues.extend(file_path_issues)
        
        # Check for test tasks
        test_tasks = [task for task in tasks if "test" in task.lower()]
        if not test_tasks:
            issues.append("No testing tasks found. All features must include tests.")
        
        # Check for acceptance criteria
        acceptance_section = self._extract_section(content, "Acceptance Criteria")
        if acceptance_section:
            acceptance_criteria = self._extract_tasks(acceptance_section)
            if not acceptance_criteria:
                issues.append("No acceptance criteria defined.")
        
        # Check for Definition of Done
        dod_section = self._extract_section(content, "Definition of Done")
        if dod_section:
            dod_items = self._extract_tasks(dod_section)
            if not dod_items:
                issues.append("No Definition of Done items defined.")
        
        return len(issues) == 0, issues
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract a specific section from markdown content."""
        pattern = rf"## {re.escape(section_name)}(.*?)(?=## |\Z)"
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else ""
    
    def _extract_tasks(self, content: str) -> List[str]:
        """Extract task items from markdown content."""
        # Match both checked and unchecked task items
        pattern = r"^- \[[ x]\] (.+)$"
        matches = re.findall(pattern, content, re.MULTILINE)
        return matches
    
    def _validate_file_paths(self, tasks: List[str]) -> List[str]:
        """Validate that tasks contain proper file paths."""
        issues = []
        
        # Look for tasks that mention files but don't have proper paths
        for task in tasks:
            if any(keyword in task.lower() for keyword in ["create", "implement", "add", "update"]):
                # Check if task mentions a file with backticks
                if "`" in task:
                    # Extract file paths in backticks
                    file_paths = re.findall(r"`([^`]+)`", task)
                    for file_path in file_paths:
                        # Validate file path format
                        if not self._is_valid_file_path(file_path):
                            issues.append(f"Invalid file path format in task: {file_path}")
                else:
                    # Task mentions creation/modification but no file path
                    if any(word in task.lower() for word in ["file", "component", "script", "endpoint"]):
                        issues.append(f"Task mentions file operation but no path specified: {task[:50]}...")
        
        return issues
    
    def _is_valid_file_path(self, path: str) -> bool:
        """Check if a file path looks valid."""
        # Basic validation - should have an extension and proper structure
        if not path or path.isspace():
            return False
        
        # Should not be just a description
        if len(path.split()) > 5:  # Likely a description, not a path
            return False
        
        # Should have an extension or be a directory
        if '.' in os.path.basename(path) or path.endswith('/'):
            return True
        
        # Directory-like paths are ok
        if '/' in path:
            return True
        
        return False

def main():
    """Main validation function."""
    parser = argparse.ArgumentParser(description="Validate feature markdown file structure")
    parser.add_argument("file", nargs="?", help="Feature markdown file to validate")
    parser.add_argument("--all", action="store_true", help="Validate all feature files")
    parser.add_argument("--fix", action="store_true", help="Attempt to fix common issues")
    
    args = parser.parse_args()
    
    try:
        # Ensure we're in project root
        ensure_project_root()
        
        # Load project configuration  
        config = load_project_config()
        validator = TaskPlanValidator(config)
        
        files_to_check = []
        
        if args.all:
            # Find all feature markdown files
            features_dir = Path(config.features_dir)
            if features_dir.exists():
                files_to_check = list(features_dir.glob("*.md"))
            else:
                print(f"⚠️  Features directory not found: {config.features_dir}")
                return 1
        elif args.file:
            files_to_check = [Path(args.file)]
        else:
            parser.print_help()
            return 1
        
        if not files_to_check:
            print("No feature files found to validate.")
            return 0
        
        print(f"🔍 Validating {len(files_to_check)} feature file(s)...")
        
        all_valid = True
        total_issues = 0
        
        for file_path in files_to_check:
            print(f"\n📄 Checking: {file_path.name}")
            
            is_valid, issues = validator.validate_file(str(file_path))
            
            if is_valid:
                print("  ✅ Valid")
            else:
                print("  ❌ Issues found:")
                for issue in issues:
                    print(f"    • {issue}")
                all_valid = False
                total_issues += len(issues)
        
        # Summary
        print(f"\n{'='*50}")
        if all_valid:
            print("🎉 All feature files are valid!")
        else:
            print(f"❌ Found {total_issues} issue(s) across {len(files_to_check)} file(s)")
            print("\nRecommendations:")
            print("• Review the issues above and update your feature files")
            print("• Ensure all required sections are present")
            print("• Add specific file paths for implementation tasks")
            print("• Include comprehensive testing tasks")
        
        return 0 if all_valid else 1
        
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 