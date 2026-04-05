# 📚 Learning Journey: GitHub Actions & CI/CD Automation
**Date:** April 6, 2026  
**Topic:** Automating Static Site Deployment

---

## 🛠 What I Learned Today

### 1. GitHub Actions Core Concepts
I understood how the **Workflow (.yml)** file works as a robot to automate tasks.
- **`on: push`**: Triggering the automation whenever code is pushed to the main branch.
- **`runs-on: ubuntu-latest`**: Getting a fresh Virtual Machine (Cloud Runner) from GitHub.

### 2. Deep Dive into Action Steps
I learned the functional meaning of these key pre-built actions:
- **`actions/checkout`**: Copying the code from the GitHub Repository to the Cloud Runner machine.
- **`actions/configure-pages`**: Setting up permissions and handshaking between the Runner and GitHub Pages.
- **`actions/upload-pages-artifact`**: Packing all static files (HTML/CSS) into a secure "Box" (Artifact) for deployment.
- **`actions/deploy-pages`**: Final step of taking the packed box and making it live on the internet.

### 3. Troubleshooting & Debugging
- Fixed **Spelling Errors** in action names (e.g., `configure-github-pages` vs `configure-pages`).
- Learned how to switch **Pages Source** from "Branch" to "GitHub Actions" in Repository Settings.
- Understood how to handle **Node.js Deprecation Warnings** by upgrading action versions (v4 to v5/v6).

---

## 💻 Technical Progress
- Successfully deployed a **Professional One-Page Portfolio**.
- Automated the deployment pipeline so that every `git push` updates the live site.
- Managed **Permissions** (`pages: write`, `id-token: write`) within the YAML file.

---

## 🎯 Next Goals
- [ ] Explore Multi-stage Docker builds.
- [ ] Connect custom domain to GitHub Pages.
- [ ] Integrate a "Contact Form" using a backend service.

---
> *"DevOps is not just about tools, it's about the process of constant improvement."*
