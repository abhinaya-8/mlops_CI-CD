```python
import unittest
from app import app


class TestPredictionAPI(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Student Result Prediction API is running",
            response.get_json()["message"]
        )

    def test_pass_prediction(self):
        response = self.client.post(
            "/predict",
            json={"internal_marks": 70, "attendance": 85}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["predicted_result"], "PASS"
        )

    def test_fail_prediction(self):
        response = self.client.post(
            "/predict",
            json={"internal_marks": 30, "attendance": 85}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["predicted_result"], "FAIL"
        )

    def test_missing_fields(self):
        response = self.client.post(
            "/predict",
            json={"internal_marks": 70}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_input(self):
        response = self.client.post(
            "/predict",
            json={"internal_marks": "abc", "attendance": 85}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
```
