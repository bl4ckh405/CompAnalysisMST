# CompAnalysis

A Python-based computational analysis project for data validation and processing using SHA256 checksums.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Running the Project](#running-the-project)

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional, for cloning the repository) - [Download Git](https://git-scm.com/downloads)

To verify your Python installation, run:
```bash
python --version
```
or
```bash
python3 --version
```

## Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/bl4ckh405/CompAnalysisMST.git
cd CompAnalysisMST
```


### 2. Navigate to the Project Directory

```bash
cd c:\Users\pavki\projects\companalysis
```

## Virtual Environment Setup

A virtual environment keeps your project dependencies isolated from other Python projects on your system.

#### Step 1: Create the Virtual Environment
```bash
python -m venv .venv
```

#### Step 2: Activate the Virtual Environment

**PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

If you encounter an execution policy error, run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.


## Running the Project

For this project, the standard library is used, so no additional packages are required.

### 1. Run the Main Script

```bash
python main.py
```

Expected output:
```
Task 1: Validate data using SHA256 checksum
Y values: [20, 93, 72, 35, 54, ...]
Expected checksum: 5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a
```