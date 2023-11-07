import json
import unittest
from unittest.mock import patch, mock_open

from core.datahandler import OriginData, DataHandler


class TestOriginData(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "country": "US",
            "city": "Boston",
            "currency": "USD",
            "amount": 100
        }
        self.origin_data = OriginData()

    def test_load_from_dict(self):
        self.origin_data.load_from_dict(self.sample_data)
        self.assertEqual(self.origin_data.country, "US")
        self.assertEqual(self.origin_data.city, "Boston")
        self.assertEqual(self.origin_data.currency, "USD")
        self.assertEqual(self.origin_data.amount, 100)

    def test_transform_by_keys(self):
        self.origin_data.load_from_dict(self.sample_data)
        transformed = self.origin_data.transform_by_keys("currency", "country")
        expected = {
            "USD": {
                "US": [{"city": "Boston", "amount": 100}]
            }
        }
        self.assertEqual(transformed, expected)


class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.json_data = [
            {"country": "US", "city": "Boston", "currency": "USD", "amount": 100},
            {"country": "FR", "city": "Paris", "currency": "EUR", "amount": 20}
        ]
        self.handler = DataHandler()

    def test_load_from_json(self):
        with patch("builtins.open", mock_open(read_data=json.dumps(self.json_data))) as mock_file:
            self.handler.load_from_json("dummy_path.json")
            mock_file.assert_called_with("dummy_path.json")
            self.assertEqual(len(self.handler.data), 2)
            self.assertEqual(self.handler.data[0].country, "US")
            self.assertEqual(self.handler.data[1].currency, "EUR")

    def test_aggregate_by_keys(self):
        with patch("builtins.open", mock_open(read_data=json.dumps(self.json_data))):
            self.handler.load_from_json("dummy_path.json")
            aggregated = self.handler.aggregate_by_keys(["currency", "country"])
            expected = {
                "USD": {"US": [{"city": "Boston", "amount": 100}]},
                "EUR": {"FR": [{"city": "Paris", "amount": 20}]}
            }
            self.assertEqual(aggregated, expected)

    def test_data_access_methods(self):
        with patch("builtins.open", mock_open(read_data=json.dumps(self.json_data))):
            self.handler.load_from_json("dummy_path.json")
            # Test __getitem__
            self.assertEqual(self.handler[0].city, "Boston")
            # Test __iter__
            for data in self.handler:
                self.assertIn("city", data.__dict__)


class TestFullDataImplementation(unittest.TestCase):

    def setUp(self):
        self.sample_data_path = "../data/input_data.json"  # forgive me for input data dependency in tests
        self.handler = DataHandler()

    def test_aggregate_by_keys_currency_country_city(self):
        self.handler.load_from_json(self.sample_data_path)
        aggregated = self.handler.aggregate_by_keys(("currency", "country", "city"))

        expected = {
            "USD": {
                "US": {
                    "Boston": [
                        {
                            "amount": 100
                        }
                    ]
                }
            },
            "EUR": {
                "FR": {
                    "Paris": [
                        {
                            "amount": 20
                        }
                    ],
                    "Lyon": [
                        {
                            "amount": 12.3
                        }
                    ]
                },
                "ES": {
                    "Madrid": [
                        {
                            "amount": 9.1
                        }
                    ]
                }
            },
            "GBP": {
                "UK": {
                    "London": [
                        {
                            "amount": 22.33
                        }
                    ]
                }
            },
            "FBP": {
                "UK": {
                    "London": [
                        {
                            "amount": 11.99
                        }
                    ]
                }
            }
        }

        self.assertEqual(expected, aggregated)


if __name__ == '__main__':
    unittest.main()
