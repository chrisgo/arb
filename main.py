#!/usr/bin/env python3
"""Main entry point for the Python project."""

import sys
from pathlib import Path

# Add the src directory to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / 'src'))

from python.app import demo

if __name__ == "__main__":
    demo()