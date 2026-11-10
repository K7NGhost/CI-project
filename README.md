# CI Project

A simple Python application that adds two numbers, with automated tests and a Jenkins pipeline.

## Run the application

```bash
python app.py
```

Expected output:

```text
Application started
2 + 3 = 5
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

All 10 tests should pass.

## Files

- `app.py` - application code.
- `tests/test_app.py` - automated tests.
- `Jenkinsfile` - tells Jenkins to run the tests and application..
