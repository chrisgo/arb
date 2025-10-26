"""Main application class that demonstrates local imports."""

from .utils import Calculator, StringHelper
from .models import User, Product


class Application:
    """Main application class that uses other modules."""
    
    def __init__(self):
        self.users = []
        self.products = []
        self.calculator = Calculator()
    
    def add_user(self, name, email, age=None):
        """Add a new user to the application."""
        user = User(name, email, age)
        self.users.append(user)
        print(f"✓ Added user: {user.name}")
        return user
    
    def add_product(self, name, price, quantity=0):
        """Add a new product to the application."""
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"✓ Added product: {product.name}")
        return product
    
    def calculate_total_inventory_value(self):
        """Calculate the total value of all products."""
        total = sum(product.get_total_value() for product in self.products)
        return self.calculator.add(total, 0)  # Using calculator for demo
    
    def display_summary(self):
        """Display a summary of the application state."""
        print("\n" + "="*50)
        print("APPLICATION SUMMARY")
        print("="*50)
        
        print(f"\n👥 Total Users: {len(self.users)}")
        for user in self.users:
            print(f"  - {user.name} ({user.email})")
        
        print(f"\n📦 Total Products: {len(self.products)}")
        for product in self.products:
            status = "✓ In Stock" if product.is_in_stock() else "✗ Out of Stock"
            print(f"  - {product.name}: ${product.price} x {product.quantity} = ${product.get_total_value():.2f} [{status}]")
        
        print(f"\n💰 Total Inventory Value: ${self.calculate_total_inventory_value():.2f}")
        print("="*50 + "\n")


def demo():
    """Demonstrate the application functionality."""
    print("🚀 Starting Python Project Demo\n")
    
    # Create application instance
    app = Application()
    
    # Add some users
    app.add_user("Alice Johnson", "alice@example.com", 28)
    app.add_user("Bob Smith", "bob@example.com", 35)
    
    # Add some products
    app.add_product("Laptop", 999.99, 5)
    app.add_product("Mouse", 29.99, 15)
    app.add_product("Keyboard", 79.99, 0)
    
    # Display summary
    app.display_summary()
    
    # Demo string helper
    print("🔤 String Helper Demo:")
    text = "hello python world"
    print(f"Original: {text}")
    print(f"Reversed: {StringHelper.reverse(text)}")
    print(f"Capitalized: {StringHelper.capitalize_words(text)}")
    
    # Demo calculator
    print("\n🔢 Calculator Demo:")
    a, b = 42, 7
    print(f"{a} + {b} = {Calculator.add(a, b)}")
    print(f"{a} × {b} = {Calculator.multiply(a, b)}")
    print(f"{a} ÷ {b} = {Calculator.divide(a, b):.2f}")
    
    print("\n✨ Demo completed successfully!")


if __name__ == "__main__":
    demo()
