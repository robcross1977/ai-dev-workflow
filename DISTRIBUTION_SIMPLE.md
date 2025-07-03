# AI Development Workflow - Simple Distribution Guide

## 🚀 Easy Distribution (No PyPI Account Required)

Here are the simplest ways to share your AI Development Workflow package:

### **Option 1: GitHub Repository Installation (Recommended)**

**Steps:**

1. Create a GitHub repository (public)
2. Push your code
3. Users install directly from GitHub

**Commands:**

```bash
# You do once:
# 1. Create repo on GitHub.com named "ai-dev-workflow"
# 2. Push your code:
git remote add origin https://github.com/robcross1977/ai-dev-workflow.git
git push -u origin trunk

# Users install with:
pip install git+https://github.com/robcross1977/ai-dev-workflow.git
```

**Benefits:**

- ✅ No account setup needed
- ✅ Automatic updates when you push changes
- ✅ Works immediately
- ✅ Version control and issue tracking

---

### **Option 2: GitHub Releases with Package Files**

**Steps:**

1. Create GitHub repository (same as Option 1)
2. Create releases with your built packages
3. Users download and install locally

**Commands:**

```bash
# You do once per release:
gh release create v1.0.0 dist/* --title "AI Dev Workflow v1.0.0" --notes "Initial release"

# Users install with:
# Method A: Download and install wheel
pip install https://github.com/robcross1977/ai-dev-workflow/releases/download/v1.0.0/ai_dev_workflow-1.0.0-py3-none-any.whl

# Method B: Download, extract, and install
wget https://github.com/robcross1977/ai-dev-workflow/archive/refs/tags/v1.0.0.tar.gz
tar -xzf v1.0.0.tar.gz
cd ai-dev-workflow-1.0.0
pip install .
```

---

### **Option 3: One-Liner Installation Scripts**

**For maximum ease, users run your install scripts:**

**Unix/Linux/macOS:**

```bash
curl -sSL https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/trunk/install.sh | bash
```

**Windows PowerShell:**

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/trunk/install.ps1" -OutFile "install.ps1"; .\install.ps1
```

---

### **Option 4: Local Development/Testing**

**For immediate local use:**

```bash
# Install in development mode (changes reflect immediately)
pip install -e .

# Or install normally
pip install .

# Test the CLI
ai-workflow --help
```

---

## 📋 **Setup Checklist**

### **To Distribute via GitHub:**

1. **Create GitHub Repository:**

   - Go to [GitHub.com](https://github.com)
   - Click "New repository"
   - Name: `ai-dev-workflow`
   - Make it **Public**
   - Don't initialize (you already have files)

2. **Update URLs in Files:**
   Replace `yourusername` with your actual GitHub username in:

   - `pyproject.toml` (urls section)
   - `setup.py` (url field)
   - `install.sh` (download URL)
   - `install.ps1` (download URL)
   - `README.md` (installation instructions)

3. **Push to GitHub:**

   ```bash
   git remote add origin https://github.com/robcross1977/ai-dev-workflow.git
   git branch -M trunk
   git push -u origin trunk
   ```

4. **Create First Release:**
   ```bash
   gh release create v1.0.0 dist/* --title "AI Development Workflow v1.0.0" --notes "Initial release with project setup, feature templates, and CLI tools"
   ```

### **Test Installation:**

```bash
# Test from GitHub
pip install git+https://github.com/robcross1977/ai-dev-workflow.git

# Test CLI works
ai-workflow --help
ai-workflow setup my-test-project
```

---

## 🎯 **User Installation Instructions**

Once you've set up GitHub distribution, users can install with:

### **Quick Install (Recommended):**

```bash
pip install git+https://github.com/robcross1977/ai-dev-workflow.git
```

### **One-Liner Install:**

```bash
# Unix/Linux/macOS
curl -sSL https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/trunk/install.sh | bash

# Windows
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/robcross1977/ai-dev-workflow/trunk/install.ps1" -OutFile "install.ps1"; .\install.ps1
```

### **Verify Installation:**

```bash
ai-workflow --help
ai-workflow setup my-new-project
```

---

## 🔄 **Updating the Package**

When you make changes:

1. **Update version** in `pyproject.toml` and `ai_dev_workflow/__init__.py`
2. **Rebuild package:** `python -m build`
3. **Commit and push:** `git add . && git commit -m "Version X.Y.Z" && git push`
4. **Create new release:** `gh release create vX.Y.Z dist/* --title "Version X.Y.Z" --notes "Changes..."`

Users update with:

```bash
pip install --upgrade git+https://github.com/robcross1977/ai-dev-workflow.git
```

---

## 🎉 **That's It!**

No PyPI account needed. No complex setup. Just GitHub and your users get:

- ✅ Easy installation
- ✅ Automatic dependency handling
- ✅ Global `ai-workflow` command
- ✅ Cursor integration files
- ✅ One-liner installers

**Next Step:** Create your GitHub repository and push your code!
