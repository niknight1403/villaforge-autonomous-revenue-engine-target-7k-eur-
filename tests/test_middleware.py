import unittest
from flask import Flask
from src.middleware import rate_limit

class TestMiddleware(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        @self.app.route('/test')
        @rate_limit(limit=2, window=1)
        def test_route():
            return 'ok'
        self.client = self.app.test_client()

    def test_rate_limiting(self):
        self.client.get('/test')
        self.client.get('/test')
        response = self.client.get('/test')
        self.assertEqual(response.status_code, 429)

if __name__ == '__main__':
    unittest.main(exit=False)