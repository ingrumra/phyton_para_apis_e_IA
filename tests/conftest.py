import sys, os

# Ensure the project root is on PYTHONPATH when running tests
top = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if top not in sys.path:
    sys.path.insert(0, top)
