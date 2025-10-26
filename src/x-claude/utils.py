"""Utility functions for the project."""


class Calculator:
    """A simple calculator class with basic operations."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class StringHelper:
    """Helper class for string operations."""
    
    @staticmethod
    def reverse(text):
        """Reverse a string."""
        return text[::-1]
    
    @staticmethod
    def capitalize_words(text):
        """Capitalize each word in a string."""
        return ' '.join(word.capitalize() for word in text.split())
