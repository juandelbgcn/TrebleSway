# test_treblesway.py
"""
Tests for TrebleSway module.
"""

import unittest
from treblesway import TrebleSway

class TestTrebleSway(unittest.TestCase):
    """Test cases for TrebleSway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrebleSway()
        self.assertIsInstance(instance, TrebleSway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrebleSway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
