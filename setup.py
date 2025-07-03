#!/usr/bin/env python3
"""
Setup script for AI Development Workflow package.

This allows the workflow to be installed as a Python package and used globally.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="ai-dev-workflow",
    version="1.0.0",
    description="AI Development Workflow for NextJS and Unity projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AI Development Team",
    author_email="dev@example.com",
    url="https://github.com/yourusername/ai-dev-workflow",
    
    # Package configuration
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ai_dev_workflow': [
            'templates/*',
            'schemas/*',
            '*.md',
        ],
    },
    
    # Scripts and entry points
    entry_points={
        'console_scripts': [
            'ai-workflow=ai_dev_workflow.cli:main',
            'ai-setup=ai_dev_workflow.setup:main',
        ],
    },
    
    # Dependencies
    install_requires=[
        "click>=8.0.0",
        "jsonschema>=4.0.0",
        "pyyaml>=6.0.0",
        "gitpython>=3.1.0",
        "requests>=2.28.0",
    ],
    
    # Optional dependencies
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
            'mypy>=1.0.0',
        ],
        'github': [
            'PyGithub>=1.58.0',
        ],
    },
    
    # Python version requirement
    python_requires=">=3.7",
    
    # Classification
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Build Tools",
    ],
    
    # Keywords for discoverability
    keywords="ai development workflow nextjs unity automation cursor",
    
    # Project URLs
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ai-dev-workflow/issues",
        "Documentation": "https://github.com/yourusername/ai-dev-workflow#readme",
        "Source": "https://github.com/yourusername/ai-dev-workflow",
    },
) 