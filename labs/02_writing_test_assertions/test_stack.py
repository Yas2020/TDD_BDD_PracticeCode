from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        l = len(self.stack.items)
        self.stack.push(4)
        self.assertEqual(len(self.stack.items), l+1)
        
    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push("SomethingWeird")
        self.assertEqual(self.stack.pop(), "SomethingWeird")

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push("SomethingWeird")
        self.assertEqual(self.stack.peek(), "SomethingWeird")

    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertTrue(self.stack.is_empty)
