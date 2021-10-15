import unittest
from main import getSchema

class TestJSONToSchema(unittest.TestCase):
    def test_create_data_1_schema(self):
        expected_result = {
            "battle": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
            },
            "joiner": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
            },
            "participantIds": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
            }
        }
        self.assertEqual(getSchema("data/data_1.json"), expected_result)

    def test_create_data_2_schema(self):
        expected_result = {
            "user": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
            },
            "time": {
                "type": "INTEGER",
                "tag": "",
                "description": "",
                "required": False
            },
            "acl": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
            },
            "publicFeed": {
                "type": "BOOLEAN",
                "tag": "",
                "description": "",
                "required": False
            },
            "internationalCountries": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
            },
            "topTraderFeed": {
                "type": "BOOLEAN",
                "tag": "",
                "description": "",
                "required": False
            }
        }
        self.assertEqual(getSchema("data/data_2.json"), expected_result)