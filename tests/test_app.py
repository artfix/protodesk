import unittest

# Import the application module
try:
    import app
except Exception as e:
    # If import fails, the test will report the error
    raise

class TestApp(unittest.TestCase):
    def test_import(self):
        """Ensure the main module imports without error."""
        self.assertTrue(hasattr(app, 'ProtonDesktopApp'))

if __name__ == "__main__":
    unittest.main()
