# test_marketpredictor.py
"""
Tests for MarketPredictor module.
"""

import unittest
from marketpredictor import MarketPredictor

class TestMarketPredictor(unittest.TestCase):
    """Test cases for MarketPredictor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarketPredictor()
        self.assertIsInstance(instance, MarketPredictor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarketPredictor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
