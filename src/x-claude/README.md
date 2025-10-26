


# Python Project

A basic Python project structure with organized modules and local imports.

## Project Structure

```
python_project/
├── main.py                 # Entry point to run the application
├── src/
│   └── python/
│       ├── __init__.py     # Package initialization
│       ├── app.py          # Main application class
│       ├── models.py       # Data models (User, Product)
│       └── utils.py        # Utility classes (Calculator, StringHelper)
└── README.md
```

## Features

- **Models**: User and Product classes with basic functionality
- **Utilities**: Calculator and StringHelper with common operations
- **Application**: Main app class that demonstrates importing and using local modules
- **Demo**: Built-in demo function to showcase all features

## How to Run

### Option 1: Run the main entry point
```bash
python3 main.py
```

### Option 2: Run the app module directly
```bash
python3 -m src.python.app
```

### Option 3: Import and use as a library
```python
import sys
sys.path.insert(0, 'src')

from python import Application, User, Product, Calculator

# Create application
app = Application()

# Add users and products
app.add_user("John Doe", "john@example.com")
app.add_product("Widget", 19.99, 10)

# Display summary
app.display_summary()
```

## Module Overview

### models.py
- `User`: Represents a user with name, email, and age
- `Product`: Represents a product with name, price, and quantity

### utils.py
- `Calculator`: Basic math operations (add, multiply, divide)
- `StringHelper`: String manipulation (reverse, capitalize)

### app.py
- `Application`: Main application class that ties everything together
- `demo()`: Demonstration function showing all features

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)