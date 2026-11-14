# Lab 5: Static Code Analysis

**Tools Used:** Pylint, Bandit, Flake8  
**Assigned Repository:** https://github.com/SETAPESU26/L5_61_attendance-tracker  

## 1. Objective
Analyse a Python attendance tracker program with Pylint, Bandit and Flake8, document the issues they report, fix them, and re-run the tools to verify the fixes.

## 2. Tools

| Tool | Used for |
|------|----------|
| Pylint | Code quality: naming, docstrings, bad practices, overall score |
| Bandit | Security: unsafe shell use, SSL settings, risky calls |
| Flake8 | Style: PEP 8 formatting, unused imports, line length |

## 3. Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.55 / 10 | 10.00 / 10 |
| Bandit | 8 issues (2 High, 3 Medium, 3 Low) | No issues identified |
| Flake8 | Unused imports, blank-line, line-length and comparison violations | No violations |

## 4. Main Fixes

| Issue | Tool / Code | Fix |
|-------|-------------|-----|
| SSL certificate validation disabled | Bandit B501 (High) | Removed `verify=False` |
| Wildcard shell backup command | Bandit B609, B607, B602 | Replaced `subprocess` shell call with Python's `tarfile` |
| Request without timeout | Bandit B113, Pylint W3101 | Added `timeout=10` |
| Legacy TLS 1.0 default | Bandit B503 | Used `ssl.create_default_context()` |
| `shell=True` in reminder job | Bandit B604 | Passed an argument list instead of a shell string |
| Mutable default argument | Pylint W0102 | Removed the `{}` default and passed the register explicitly |
| Comparison to `False` | Pylint C0121, Flake8 E712 | Used `not is_eligible(...)` |
| Unused imports | Pylint W0611, Flake8 F401 | Removed them |
| Naming and docstrings | Pylint C0103, C0116 | Renamed to snake_case and added docstrings |
| Formatting | Flake8 E302, E305, E501 | Fixed blank lines and long lines |

I also fixed a divide-by-zero for students with no records, standardised date parsing, and sanitised CSV text fields against formula injection. The full table is in [issues.md](issues.md).

## 5. Commits

```
7242aa0  Fix Flake8 issues and add Lab 5 deliverables
fbd8290  Fix Bandit security findings
f2d2d5e  Fix Pylint code quality findings
```

## 6. Files in this folder

| File | Description |
|------|-------------|
| `attendance_tracker.py` | Fixed application |
| `pylint_report_before.txt` / `pylint_report_after.txt` | Pylint reports |
| `bandit_report_before.txt` / `bandit_report_after.txt` | Bandit reports |
| `flake8_report_before.txt` / `flake8_report_after.txt` | Flake8 reports (the "after" file is empty because there were no violations) |
| `issues.md` | Issue and fix table |
| `reflection.md` | Reflection answers |

## 7. How to run

```bash
python -m venv venv
venv\Scripts\activate            # Linux/Mac: source venv/bin/activate
pip install pylint bandit flake8 requests

python attendance_tracker.py
pylint attendance_tracker.py
bandit -r attendance_tracker.py
flake8 attendance_tracker.py
```

`sync_to_erp()` needs the `ERP_API_KEY` environment variable. The demo in `main()` skips the ERP sync.

## 8. Key takeaway
Static analysis catches problems early without running the code, but it cannot guarantee the program is correct or secure. It needs to be combined with testing and code review.
