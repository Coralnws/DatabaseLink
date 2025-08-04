# test_databaselink.py
"""
Tests for DatabaseLink module.
"""

import unittest
from databaselink import DatabaseLink

class TestDatabaseLink(unittest.TestCase):
    """Test cases for DatabaseLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DatabaseLink()
        self.assertIsInstance(instance, DatabaseLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DatabaseLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
