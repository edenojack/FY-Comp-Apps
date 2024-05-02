import unittest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from APP.main import BinaryConverter
import tkinter as tk

class TestBinaryConverter(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = BinaryConverter(self.root)

    def test_binary_to_decimal_conversion(self):
        test_input = "1010"
        expected_output = "10"
        self.app.input_entry.insert(0, test_input)
        self.app.conversion_type.set("Binary to Decimal")
        self.app.convert()
        output = self.app.output_text.get("1.0", tk.END)
        test_result = "Pass" if expected_output in output else "Fail"
        print("="*40)
        print("Test 1 - Binary to Decimal Conversion:")
        print("-" * 40)
        print(f"Input: {test_input}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {output}")
        print(f"Test Result: {test_result}")
        print("="*40)
        self.assertIn(expected_output, output)

    def test_decimal_to_binary_conversion(self):
        test_input = "10"
        expected_output = "1010"
        self.app.input_entry.insert(0, test_input)
        self.app.conversion_type.set("Decimal to Binary")
        self.app.convert()
        output = self.app.output_text.get("1.0", tk.END)
        test_result = "Pass" if expected_output in output else "Fail"
        print("="*40)
        print("Test 2 - Decimal to Binary Conversion:")
        print("-" * 40)
        print(f"Input: {test_input}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {output}")
        print(f"Test Result: {test_result}")
        print("="*40)
        self.assertIn(expected_output, output)

    def test_decimal_to_hexadecimal_conversion(self):
        test_input = "255"
        expected_output = "FF"
        self.app.input_entry.insert(0, test_input)
        self.app.conversion_type.set("Decimal to Hexadecimal")
        self.app.convert()
        output = self.app.output_text.get("1.0", tk.END)
        test_result = "Pass" if expected_output in output else "Fail"
        print("="*40)
        print("Test 3 - Decimal to Hexadecimal Conversion:")
        print("-" * 40)
        print(f"Input: {test_input}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {output}")
        print(f"Test Result: {test_result}")
        print("="*40)
        self.assertIn(expected_output, output)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()



