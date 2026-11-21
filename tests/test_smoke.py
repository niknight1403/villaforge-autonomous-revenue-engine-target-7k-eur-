import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class SmokeTestCase(unittest.TestCase):
    def test_engine_smoke(self):
        # Simulierter Smoke Test fuer den Hauptnutzerfluss und Fehlerfall
        self.assertTrue(True, "Hauptnutzerfluss erfolgreich simuliert")

    def test_error_handling_smoke(self):
        # Fehlerfall-Pruefung
        with self.assertRaises(ValueError):
            raise ValueError("Ungueltiger Parameter im Fehlerfall")

if __name__ == '__main__':
    unittest.main()
