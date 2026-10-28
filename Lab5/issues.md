# Lab 5 — Static Code Analysis: Issues and Fixes

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument (W0102) | Bug / Code quality | 18 | A default dictionary could be shared between function calls. | Removed the mutable default and explicitly passed the attendance register. |
| Disabled SSL certificate validation (B501) | High security | 60 | `verify=False` disabled certificate verification. | Removed `verify=False` and restored the default certificate verification. |
| Missing request timeout (B113) | Medium security / Reliability | 60 | The HTTP request could wait indefinitely. | Added `timeout=10`. |
| Wildcard backup command (B609, B607, B602) | Security | 64 | The backup used shell execution with a wildcard and partial executable path. | Replaced shell-based execution with Python's `tarfile` module. |
| Subprocess import (B404) | Security | 5 | The subprocess import was associated with the shell-based backup implementation. | Removed the import after replacing the backup implementation. |
| Legacy TLS protocol (B503) | Medium security | 66 | The original function used the legacy TLS 1.0 protocol default. | Replaced it with `ssl.create_default_context()`. |
| Shell execution in reminder job (B604) | Medium security | 73 | The reminder helper used `shell=True`. | Replaced the shell command string with an argument list. |
| Boolean comparison (C0121 / E712) | Bug / Style | 35 | A Boolean result was explicitly compared to `False`. | Used `not is_eligible(...)` instead. |
| Unused imports (W0611 / F401) | Code quality / Style | 1, 4, 6 | Some imported modules were not used. | Removed unused imports and retained necessary imports. |
| Formatting issues (E265, E302, E501) | Style | Multiple | Comments, blank lines and statement lengths violated style rules. | Corrected comment formatting, blank lines and long statements. |
| Empty attendance records | Logic | Percentage calculation | Dividing by zero was possible when a student had no records. | Added a check that returns zero for an empty record set. |
| Date representation | Logic | Latest-date calculation | Inconsistent date formatting could cause parsing failures. | Standardized dates and parsed them before comparison. |
| CSV formula injection | Security review | CSV export | Formula-like text could be interpreted by spreadsheet software. | Sanitized exported text fields before writing the CSV. |

## Verification

The corrected program was compiled and executed. Pylint, Bandit and Flake8 were run again, with their final reports saved separately from the original reports.