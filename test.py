import unittest
import lambda_function
import logging
import sys

stream_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


class LampdaTestCase(unittest.TestCase):

    def test_list_foods(self):
        event = {"route": "/foods"}
        print(lambda_function.lambda_handler(event, None))

    def test_list_brands(self):
        event = {
                    "route": "/foods/<int:food_id>/brands",
                    "food_id": 5
                }
        print(lambda_function.lambda_handler(event, None))

    def test_list_foods_checmicals(self):
        event = {
            "route": "/brands/<int:brand_id>/foods/<int:food_id>/chemicals",
            "food_id": 5,
            "brand_id": 17
        }
        print(lambda_function.lambda_handler(event, None))

if __name__ == '__main__':
    unittest.main()