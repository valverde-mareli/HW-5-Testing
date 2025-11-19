
Overall coverage of the `src/` directory is:

- **95% total coverage**
- `pricing.py`: **100%**
- `order_io.py`: **90%**


Overall coverage of the `src/` directory is:

- **95% total coverage**
- `pricing.py`: **100%**
- `order_io.py`: **90%**

This exceeds the assignment's requirement of achieving >85% coverage.

---

## Coverage Details

| File           | Statements | Missed | Coverage | Missing Lines |
|----------------|------------|--------|----------|----------------|
| `src/order_io.py` | 20 | 2 | 90% | 12, 15 |
| `src/pricing.py`  | 23 | 0 | 100% | — |

---

## Uncovered Lines Explained

### `src/order_io.py` (Lines 12, 15)
These lines correspond to edge-case branches:

- **Line 12** — The branch that handles malformed CSV lines (e.g., lines without exactly two comma-separated values).  
- **Line 15** — A continuation of the error-handling path for irregular input.

These scenarios are uncommon in normal application usage and not essential to the core functionality tested in this assignment.

---

## Test Coverage Improvements
The most important logic paths are fully tested:

- Price parsing  
- Currency formatting  
- Discount calculation (with regression test)  
- Tax application  
- Bulk total calculation  
- Full integration workflow (load → compute → write receipt)

Only rare error-handling branches remain uncovered, which is acceptable for this project.

---

## Conclusion
The final test suite provides strong coverage of all primary components in the pricing workflow.  
The uncovered lines are limited to low-priority error-handling code, and the overall coverage meets the assignment expectations.

This exceeds the assignment's requirement of achieving >85% coverage.

---

## Coverage Details

| File           | Statements | Missed | Coverage | Missing Lines |
|----------------|------------|--------|----------|----------------|
| `src/order_io.py` | 20 | 2 | 90% | 12, 15 |
| `src/pricing.py`  | 23 | 0 | 100% | — |

---

## Uncovered Lines Explained

### `src/order_io.py` (Lines 12, 15)
These lines correspond to edge-case branches:

- **Line 12** — The branch that handles malformed CSV lines (e.g., lines without exactly two comma-separated values).  
- **Line 15** — A continuation of the error-handling path for irregular input.

These scenarios are uncommon in normal application usage and not essential to the core functionality tested in this assignment.

---

## Test Coverage Improvements
The most important logic paths are fully tested:

- Price parsing  
- Currency formatting  
- Discount calculation (with regression test)  
- Tax application  
- Bulk total calculation  
- Full integration workflow (load → compute → write receipt)

Only rare error-handling branches remain uncovered, which is acceptable for this project.

---

## Conclusion
The final test suite provides strong coverage of all primary components in the pricing workflow.  
The uncovered lines are limited to low-priority error-handling code, and the overall coverage meets the assignment expectations.

