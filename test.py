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

    def test_add_food(self):
        event = {
                    "route": "/foods",
                    "name": "nova comida"
                }
        print(lambda_function.lambda_handler(event, None))

    def test_list_brands(self):
        event = {"route": "/brands"}
        print(lambda_function.lambda_handler(event, None))

    def test_add_brand(self):
        event = {
            "route": "/brands",
            "name": "nova marca"
        }
        print(lambda_function.lambda_handler(event, None))

    def test_list_chemicals(self):
        event = {"route": "/chemicals"}
        print(lambda_function.lambda_handler(event, None))

    def test_list_brands_food(self):
        event = {
                    "route": "/foods/<int:food_id>/brands",
                    "food_id": 5
                }
        print(lambda_function.lambda_handler(event, None))

    def test_list_foods_chemicals(self):
        event = {
            "route": "/brands/<int:brand_id>/foods/<int:food_id>/chemicals",
            "food_id": 5,
            "brand_id": 17
        }
        print(lambda_function.lambda_handler(event, None))

    def test_get_barcode(self):
        event = {
                    "route": "/brands/foods/<string:bar_code>",
                    "bar_code": "7896034300789"
                }
        print(lambda_function.lambda_handler(event, None))

    def test_add_brand_food(self):
        event = {
                    "route": "/brands/<int:brand_id>/foods/<int:food_id>",
                    "bar_code": "7097498413194",
                    "food_id": 29,
                    "brand_id": 31,
                    "chemicals": [179, 178]
                }
        print(lambda_function.lambda_handler(event, None))

if __name__ == '__main__':
    unittest.main()