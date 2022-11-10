import unittest
import rename

class TestRename(unittest.TestCase):
    # def test_getAllFile(self):
    #     self.assertEqual(rename.getAllFile("."), [("temp", "rename.py"), ("temp", "rename_test.py")])
    def test_filterRule(self):
        self.assertTrue(rename.filterRule("summary.md"))
        self.assertTrue(rename.filterRule("navigation.md"))
        self.assertFalse(rename.filterRule("README.md"))

    def test_renameRule(self):
        self.assertEqual(rename.renameRule("summary.md"), "SUMMARY.md")
        self.assertEqual(rename.renameRule("navigation.md"), "NAVIGATION.md")

    def test_renameFiles(self):
        pass

if __name__ == "__main__":
    unittest.main()