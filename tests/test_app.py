import unittest
import threading
import json
from urllib.request import urlopen
from urllib.error import HTTPError
from http.server import HTTPServer
from app import Handler

class AppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(
            target=cls.server.serve_forever, daemon=True
        )
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_home(self):
        with urlopen(self.url + "/") as response:
            self.assertEqual(response.status, 200)
            self.assertIn(b"Task 4 CI/CD Pipeline", response.read())

    def test_health(self):
        with urlopen(self.url + "/health") as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read())
            self.assertEqual(data["status"], "healthy")

    def test_not_found(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(self.url + "/missing")
        self.assertEqual(error.exception.code, 404)

if __name__ == "__main__":
    unittest.main()
