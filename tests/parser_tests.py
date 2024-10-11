import unittest
from services.parsers import DefinitionParser

class DefinitionParserTests(unittest.TestCase):

    def test_parse(self):
        definition_parser = DefinitionParser("SBO_OWNER.SBO_CTRL.txt")
        definition_result = definition_parser.parse()
        self.assertEquals(len(definition_result), 9)

        self.assertFalse(definition_result[0].nullable)
        self.assertTrue(definition_result[0].data_type == "str")
