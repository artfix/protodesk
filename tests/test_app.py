import unittest

import app

class TestApp(unittest.TestCase):
    def test_import(self):
        """Ensure the main module imports without error."""
        self.assertTrue(hasattr(app, 'ProtonDesktopApp'))

if __name__ == "__main__":
    unittest.main()
