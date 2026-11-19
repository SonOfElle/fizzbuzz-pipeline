# FizzBuzz Pipeline

A clean, tested Python implementation of the FizzBuzz workload automated via a two-stage GitHub Actions CI pipeline.

## Story Point Estimation

**Estimate:** **2 Story Points** (Fibonacci sequence)

The implementation is a small, deterministic task with clearly defined acceptance criteria (`1..100`) and zero external runtime dependencies. The estimate covers core logic with input validation, unit and integration testing (`pytest`), static analysis (`ruff`), a gated CI workflow, and documentation.

---

## Engineering Principles Demonstrated

* **Separation of Concerns & Testability:** `evaluate_number()` isolates pure transformation logic from I/O, while `main(sink: TextIO | None = None)` resolves the output stream at call time so tests can inject an `io.StringIO()` buffer or capture `stdout` cleanly.
* **Lazy Sequence Generation:** `generate_sequence()` yields values lazily via an `Iterator[str]`, avoiding unnecessary list materialization while keeping iteration straightforward.
* **Defensive Input Contract:** `evaluate_number()` enforces explicit type and range boundaries, rejecting booleans (`bool` is a subclass of `int` in Python) and non-integers with `TypeError`, and integers `< 1` with `ValueError`.
* **Blocking CI Quality Gates:** The `run-fizzbuzz` job depends on `lint-and-test` (`needs: lint-and-test`). Failing lint checks, formatting drift, or failing tests block execution immediately, while JUnit XML results are uploaded as an artifact (`if: always()`).
* **Least Privilege & Reproducibility:** The workflow restricts `GITHUB_TOKEN` permissions to `contents: read`, uses standard library code only at runtime, and pins dev tooling in `requirements-dev.txt`.

---

## Repository Structure

```text
fizzbuzz-pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml                # Stage 1: Lint & Test -> Stage 2: Execute Workload
├── src/
│   └── fizzbuzz.py               # Core FizzBuzz logic and CLI entrypoint
├── tests/
│   └── test_fizzbuzz.py          # Parameterized unit, generator, and integration tests
├── .gitignore
├── backlog_refinement.txt        # Prioritized Backlog Refinement proposals
├── pyproject.toml                # Ruff & Pytest configuration
├── README.md                     # Story Point estimate, design notes, and setup guide
└── requirements-dev.txt          # Pinned development dependencies
```

---

## Running Locally (Windows 11)

### Git Bash
```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate

# 2. Install dev dependencies
pip install -r requirements-dev.txt

# 3. Run linter, format check, and tests
ruff check .
ruff format --check .
pytest -v

# 4. Execute the FizzBuzz script
PYTHONPATH=src python -m fizzbuzz
```

### Windows PowerShell
```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dev dependencies
pip install -r requirements-dev.txt

# 3. Run linter, format check, and tests
ruff check .
ruff format --check .
pytest -v

# 4. Execute the FizzBuzz script
$env:PYTHONPATH = "src"
python -m fizzbuzz
```
