import unittest
from ..runner import Runner

class TestHtmlParserLocal(unittest.TestCase):

    def setUp(self):
        inv_file = "\\inventory.json"
        drv_file = "\\driver\\chromedriver.exe"
        self.test_runner = Runner(inv_file, drv_file, True)

    def run_query_by_item_id(self, item_id):
        return self.test_runner.run_query(item_id)

    def test_runner_exists(self):
        self.assertIsNotNone(self.test_runner)
    
    def test_find_by_name_local(self):
        r = self.run_query_by_item_id("03")
        self.assertNotEqual(r, "")
    
    def tearDown(self):
        self.test_runner.quit()
    
    if __name__ == '__main__':
        unittest.main()