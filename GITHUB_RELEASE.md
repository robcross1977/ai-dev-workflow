# GitHub Release Instructions

## 🚀 Creating Your First Release

### **Method 1: Manual Release via GitHub Web Interface**

1. **Go to Releases Page**:
   [https://github.com/robcross1977/ai-dev-workflow/releases](https://github.com/robcross1977/ai-dev-workflow/releases)

2. **Click "Create a new release"**

3. **Fill in Release Details**:

   - **Tag**: `v1.0.0`
   - **Release title**: `AI Development Workflow v1.0.0`
   - **Target**: `trunk` (your main branch)

4. **Upload Distribution Files**:
   Drag these files from your local `dist/` folder:

   - `ai_dev_workflow-1.0.0-py3-none-any.whl`
   - `ai_dev_workflow-1.0.0.tar.gz`

5. **Release Description** (copy this):

   ````markdown
   🚀 Initial release of AI Development Workflow

   ## Features

   - **Automated Project Setup**: NextJS with TypeScript, Unity with C#
   - **Feature Template Generation**: Comprehensive task breakdowns with testing
   - **CLI Tools**: Global `ai-workflow` command for project management
   - **Cursor Integration**: Optimized AI settings and documentation
   - **Progress Tracking**: Visual progress monitoring across features
   - **Validation Tools**: Ensure feature completeness before development

   ## Installation

   ```bash
   pip install git+https://github.com/robcross1977/ai-dev-workflow.git
   ```
   ````

   ## One-Liner Install

   ```bash
   # Unix/Linux/macOS
   curl -sSL https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/trunk/install.sh | bash

   # Windows PowerShell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/trunk/install.ps1" -OutFile "install.ps1"; .\install.ps1
   ```

   ## Quick Start

   ```bash
   ai-workflow setup my-project
   ai-workflow feature user-auth --issue 123
   ai-workflow validate --all
   ```

   ## What's Included

   - **Global CLI**: `ai-workflow` command
   - **Project templates**: NextJS + Unity support
   - **Feature generation**: Comprehensive task breakdowns
   - **Cursor integration**: AI-optimized settings
   - **Validation tools**: Quality assurance
   - **Progress tracking**: Visual completion status

   ## Documentation

   - [README](https://github.com/robcross1977/ai-dev-workflow#readme)
   - [Installation Guide](https://github.com/robcross1977/ai-dev-workflow/blob/trunk/INSTALL.md)
   - [Distribution Guide](https://github.com/robcross1977/ai-dev-workflow/blob/trunk/DISTRIBUTION_SIMPLE.md)
   - [Implementation Status](https://github.com/robcross1977/ai-dev-workflow/blob/trunk/IMPLEMENTATION_STATUS.md)

   ```

   ```

6. **Click "Publish release"**

---

### **Method 2: GitHub CLI (if you install `gh` later)**

If you install GitHub CLI (`gh`), you can create releases from command line:

```bash
# Install GitHub CLI first (optional)
# Windows: winget install --id GitHub.cli
# macOS: brew install gh
# Linux: see https://github.com/cli/cli#installation

# Then create release
gh release create v1.0.0 dist/* \
  --title "AI Development Workflow v1.0.0" \
  --notes-file RELEASE_NOTES.md
```

---

## 🔄 **Future Releases Workflow**

### **When You Make Updates:**

1. **Update Version Numbers**:

   - `pyproject.toml`: `version = "1.1.0"`
   - `ai_dev_workflow/__init__.py`: `__version__ = "1.1.0"`

2. **Rebuild Package**:

   ```bash
   python -m build
   ```

3. **Commit and Push**:

   ```bash
   git add -A
   git commit -m "Version 1.1.0 - Add new features"
   git push
   ```

4. **Create New Release**:
   - Tag: `v1.1.0`
   - Upload new `dist/` files
   - Update release notes with changes

---

## 📋 **Release Checklist**

### **Before Each Release:**

- [ ] Update version in `pyproject.toml`
- [ ] Update version in `ai_dev_workflow/__init__.py`
- [ ] Run `python -m build` to create fresh packages
- [ ] Test installation: `pip install dist/ai_dev_workflow-X.X.X-py3-none-any.whl`
- [ ] Test CLI: `ai-workflow --help`
- [ ] Commit and push all changes
- [ ] Create GitHub release with proper tag
- [ ] Upload distribution files
- [ ] Test public installation: `pip install git+https://github.com/robcross1977/ai-dev-workflow.git`

### **After Release:**

- [ ] Update documentation if needed
- [ ] Announce on social media/forums if desired
- [ ] Monitor for user feedback and issues

---

## 🎯 **Release Notes Templates**

### **Feature Release Template:**

````markdown
## 🚀 Version X.X.X

### ✨ New Features

- Added [feature name]: [description]
- Enhanced [component]: [improvements]

### 🐛 Bug Fixes

- Fixed [issue]: [description]
- Resolved [problem]: [solution]

### 📚 Documentation

- Updated [docs]: [changes]
- Added [guide]: [description]

### 🔧 Technical Changes

- Improved [component]: [details]
- Optimized [feature]: [benefits]

## Installation

```bash
pip install git+https://github.com/robcross1977/ai-dev-workflow.git
```
````

````

### **Patch Release Template:**
```markdown
## 🔧 Version X.X.X (Patch)

### 🐛 Bug Fixes
- Fixed [critical issue]
- Resolved [user reported problem]

### 📦 Installation
```bash
pip install --upgrade git+https://github.com/robcross1977/ai-dev-workflow.git
````

```

---

## 🌟 **Tips for Great Releases**

1. **Use Semantic Versioning**:
   - `1.0.0` → `1.0.1` (bug fixes)
   - `1.0.0` → `1.1.0` (new features)
   - `1.0.0` → `2.0.0` (breaking changes)

2. **Write Clear Release Notes**:
   - Focus on user benefits
   - Include code examples
   - Link to documentation

3. **Test Before Release**:
   - Always test the built packages
   - Verify installation works
   - Check CLI functionality

4. **Keep Archives**:
   - GitHub automatically keeps all release files
   - Users can install specific versions if needed

---

Your AI Development Workflow is ready for the world! 🚀
```
