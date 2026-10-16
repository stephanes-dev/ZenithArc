# test_zenitharc.py
"""
Tests for ZenithArc module.
"""

import unittest
from zenitharc import ZenithArc

class TestZenithArc(unittest.TestCase):
    """Test cases for ZenithArc class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZenithArc()
        self.assertIsInstance(instance, ZenithArc)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZenithArc()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
