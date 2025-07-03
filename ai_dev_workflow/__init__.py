"""
AI Development Workflow Package

A comprehensive workflow system for automating NextJS and Unity project development
with AI assistance and standardized processes.
"""

__version__ = "1.0.0"
__author__ = "AI Development Team"
__email__ = "dev@example.com"

# Public API exports
from .config import ProjectConfig, load_project_config
from .setup import main as setup_project
from .feature import generate_nextjs_feature_template, generate_unity_feature_template
from .validation import TaskPlanValidator

__all__ = [
    "ProjectConfig",
    "load_project_config", 
    "setup_project",
    "generate_nextjs_feature_template",
    "generate_unity_feature_template",
    "TaskPlanValidator",
] 