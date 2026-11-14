# Lab 7: Fuzzing for Input Validation Bugs

**Tools Used:** Python, pytest, Hypothesis  

## 1. Objective
Use property-based fuzz testing with Hypothesis to find input-validation bugs in a Python application, then fix the application so it handles unexpected inputs safely.

## 2. Application under test
`credit_card_rewards_parser.py` has three functions:

- `mask_card_number()`: masks a card number except the last four digits
- `parse_transaction()`: parses a `DATE,CATEGORY,AMOUNT` line
- `parse_statement_total()`: extracts the total from a line like `Total: 12,500`

## 3. Bugs found by fuzzing

| Function | Failing input | Error |
|----------|---------------|-------|
| `mask_card_number()` | `None` | `AttributeError` |
| `parse_transaction()` | `""` | `IndexError` |
| `parse_transaction()` | `None` | `AttributeError` |
| `parse_statement_total()` | `":"` | `ValueError` |
| `parse_statement_total()` | `""` | `IndexError` |
| `parse_statement_total()` | `None` | `AttributeError` |

## 4. Fix
Each function now checks the input type, validates the format, and returns `None` for invalid input instead of crashing. Valid inputs give the same output as before.

## 5. Results

| Stage | Result |
|-------|--------|
| Original app, valid input | Works |
| Fuzz tests on original app | Failures in all three functions |
| Fixed app, valid input | Works |
| Fuzz tests on fixed app | **6 passed** |

## 6. Screenshots

| File | Shows |
|------|-------|
| `SS1_Original_Application.png` | Original app run |
| `SS2A_Card_Number_Failure.png` | `mask_card_number` failure |
| `SS2B_Transaction_Failure.png` | `parse_transaction` failures |
| `SS2C_Statement_Total_Failure.png` | `parse_statement_total` failures |
| `SS3_Fixed_Application.png` | Fixed app run |
| `SS4_All_Tests_Passing.png` | All 6 tests passing |


## 7. How to run

```bash
pip install hypothesis pytest

python credit_card_rewards_parser.py
python -m pytest -q test_credit_card_rewards_parser.py
```

## 8. Files in this folder

| File | Description |
|------|-------------|
| `credit_card_rewards_parser.py` | Fixed application |
| `test_credit_card_rewards_parser.py` | Hypothesis fuzz tests and extra tests |
| `SS1` to `SS4` PNG files | Screenshots |
| `PES1UG24CS124_CHAITHANYA_N_Lab7_FuzzTesting_Report.pdf` | Full report |

## 9. Key takeaway
Fuzzing found edge cases (`None`, empty strings, malformed text) that I would not have thought to test by hand. Writing the test as a property ("this should never crash") lets Hypothesis do the guessing.
