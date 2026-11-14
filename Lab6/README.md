# Lab 6: Code and Branch Coverage Analysis

**Tools Used:** Python, pytest, coverage  

## 1. Objective
Understand the difference between line coverage and branch coverage, measure coverage with the `coverage` tool, and write extra test cases for the paths the starter tests missed.

## 2. Application under test
`credit_card_rewards.py` has three functions:

- `reward_points()`: reward points from card tier, amount, category and weekend status
- `late_payment_fee()`: late fee from outstanding amount and days late
- `card_status()`: account status from utilisation, missed payments and frozen-card info

I did not change the application code. I only added tests.

## 3. Test files

| File | Tests | Purpose |
|------|-------|---------|
| `CodeCoverageTest_PES1UG24CS124_application.py` | 24 | Normal inputs plus boundary and invalid inputs, for line coverage |
| `BranchCoverageTest_PES1UG24CS124_application.py` | 28 | Both outcomes of each decision statement, for branch coverage |

`test_credit_card_rewards.py` is the starter test file given with the lab.

## 4. Results

| Type | Tests passed | Statements | Branches | Missed | Coverage |
|------|--------------|-----------|----------|--------|----------|
| Code (line) | 24 | 35 | – | 0 | **100%** |
| Branch | 28 | 35 | 26 | 0 (0 partial) | **100%** |

Screenshots: [`code_coverage_result.png`](code_coverage_result.png) and [`branch_coverage_result.png`](branch_coverage_result.png).

## 5. How to run

```bash
pip install coverage pytest

# Code coverage
python -m coverage erase
python -m coverage run --source=credit_card_rewards -m pytest -q CodeCoverageTest_PES1UG24CS124_application.py
python -m coverage report -m

# Branch coverage
python -m coverage erase
python -m coverage run --branch --source=credit_card_rewards -m pytest -q BranchCoverageTest_PES1UG24CS124_application.py
python -m coverage report -m
```

## 6. Commits

```
15c9f23  Code coverage tests
0594617  Branch coverage tests
```

## 7. Files in this folder

| File | Description |
|------|-------------|
| `credit_card_rewards.py` | Application (unchanged) |
| `test_credit_card_rewards.py` | Starter tests |
| `CodeCoverageTest_PES1UG24CS124_application.py` | Code coverage tests |
| `BranchCoverageTest_PES1UG24CS124_application.py` | Branch coverage tests |
| `code_coverage_result.png` | Code coverage screenshot |
| `branch_coverage_result.png` | Branch coverage screenshot |
| `PES1UG24CS124_Lab6_Coverage_Report.pdf` | Full report |

## 8. Key takeaway
Line coverage only shows that every line ran once. Branch coverage forces me to test both the True and False side of each decision, so it catches untested paths that line coverage hides.
