import unittest
import logging
from ..runner import Runner

logging.basicConfig(level=logging.INFO)

class TestHtmlParserLocal(unittest.TestCase):

    def setUp(self):
        inv_file = "\\inventory.json"
        drv_file = "\\driver\\chromedriver.exe"
        self.test_runner = Runner(inv_file, drv_file, True)

    def run_query_by_item_id(self, item_id):
        result = self.test_runner.run_query(item_id)
        logging.info("Result for <{}>: {}".format(item_id, result))
        return result

    def test_find_by_name(self):
        result = self.run_query_by_item_id("test_find_by_name")
        self.assertNotEqual(result, [])
        self.assertEqual(str(result[0]), "<h2>This is first heading 2</h2>")
    
    def test_find_by_string(self):
        result = self.run_query_by_item_id("test_find_by_string")
        self.assertNotEqual(result, [])
        self.assertEqual(str(result[0]), "Span number three.")
    
    def test_find_by_name_and_string(self):
        result = self.run_query_by_item_id("test_find_by_name_and_string")
        self.assertNotEqual(result, [])
        self.assertEqual(str(result[0]), "<span>Span number three.</span>")
    
    def tearDown(self):
        self.test_runner.quit()
    
    if __name__ == '__main__':
        unittest.main()