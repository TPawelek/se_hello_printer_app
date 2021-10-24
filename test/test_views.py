import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
import json


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{"imie": "Tomek", "msg": "Hello World!"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<greetings><name>Tomek</name><msg>' +
                         'Hello World!</msg>' +
                         b'</greetings>', rv.data)

    def test_msg_with_output_json_with_name(self):
        expected_name = "Justyna"
        rv = self.app.get('/?output=json&name=' + expected_name)
        rd = json.loads(rv.data)
        self.assertEqual(expected_name, rd['imie'])
