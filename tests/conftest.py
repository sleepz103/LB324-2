import os
import sys

# Add parent directory to Python path so tests can find the arithmetic module
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
