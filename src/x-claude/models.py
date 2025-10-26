"""Data models for the project."""


class User:
    """Represents a user in the system."""
    
    def __init__(self, name, email, age=None):
        self.name = name
        self.email = email
        self.age = age
    
    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}', age={self.age})"
    
    def get_info(self):
        """Return formatted user information."""
        info = f"Name: {self.name}\nEmail: {self.email}"
        if self.age:
            info += f"\nAge: {self.age}"
        return info


class Product:
    """Represents a product with price and quantity."""
    
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"Product(name='{self.name}', price=${self.price}, quantity={self.quantity})"
    
    def get_total_value(self):
        """Calculate total value of product stock."""
        return self.price * self.quantity
    
    def is_in_stock(self):
        """Check if product is available."""
        return self.quantity > 0
