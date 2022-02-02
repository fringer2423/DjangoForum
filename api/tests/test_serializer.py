from django.test import TestCase
from api.models import Checkbox
from api.serializers import CheckboxSerializers


class CheckboxSerializerApiTestCase(TestCase):

    def test_serializer(self):
        checkbox_1 = Checkbox.objects.create(name="checkbox_1")
        checkbox_2 = Checkbox.objects.create(name="checkbox_2")
        serializer_data = CheckboxSerializers([checkbox_1, checkbox_2], many=True).data
        expected_data = [
            {
                "id": 1,
                "name": "checkbox_1",
                "is_checked": False,
            },
            {
                "id": 2,
                "name": "checkbox_2",
                "is_checked": False,
            },
        ]
        self.assertEqual(serializer_data, expected_data)
