# 🚀 Selenium QA Automation Project

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-automation-green?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![uv](https://img.shields.io/badge/astral-uv-orange?logoColor=white)](https://astral.sh/uv)

A Selenium-based QA automation project written in **Python**, designed for reliable and maintainable end-to-end testing.  
This project uses **Astral `uv`** for fast, reproducible dependency and virtual environment management.

---

## 📦 Prerequisites

Make sure the following are installed on your system:

- **Python** (version specified in `.python-version`)
- **uv** (Astral package manager)
- **Google Chrome** and/or **Mozilla Firefox**
- Corresponding **WebDriver**
  - Chrome → ChromeDriver
  - Firefox → GeckoDriver

---

## ⚡ Install `uv`

If you don’t already have `uv` installed:

### Linux / macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### Check is it installed 
```bash
uv --version
```
### Clone the repo 
git clone https://github.com/sakarkharel/saucedemo_qa
```bash
cd saucedemo_qa
```

### Sync the dependencies 
```bash
uv sync
```

### Activate the virtual environment 
```bash
source .venv/bin/activate
```

### Run the Automation Script 
```bash
python3 script.py
```
