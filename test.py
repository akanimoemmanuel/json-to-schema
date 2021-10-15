import unittest
from main import createSchema, getSchema

class TestJSONToSchema(unittest.TestCase):

    def test_create_schema(self):
        test_json = {
            "STRING": "Akanimo Emmanuel",
            "INTEGER": 1,
            "ENUM": ["ONE", "TWO", "THREE", "FOUR"],
            "ARRAY": {1: "ONE", 2: "TWO"}
        }
        expected_result = {
            "STRING": {
                "type": "STRING",
                "tag": "",
                "description": "",
                "required": False
            },
            "INTEGER": {
                "type": "INTEGER",
                "tag": "",
                "description": "",
                "required": False
            },
            "ENUM": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
            },
            "ARRAY": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
            },
        }
        self.assertEqual(createSchema(test_json), expected_result)
