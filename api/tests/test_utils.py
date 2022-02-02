from django.test import TestCase
from api.utils import Sum


class UtilsTestCase(TestCase):

    def test_sum(self):
        params = {
            "val_1": 10,
            "val_2": 10,
        }
        result = Sum(params).call().get("result")
        self.assertEqual(result, params["val_1"] + params["val_2"])
