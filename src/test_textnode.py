import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a node with an url", "italic", "https://www.supercombo.gg")
        node2 = TextNode("This is a node with an url", "italic", "https://www.supercombo.gg")        
        self.assertEqual(node, node2)

    def test_url_not_equal(self):
        node = TextNode("This is a node with none url", "italic")
        node2 = TextNode("This is a node with none url", "italic", "None")
        self.assertNotEqual(node, node2)

    def test_text_not_equal(self):
        node = TextNode("This is one node", "bold", "https://www.supercombo.gg")
        node2 = TextNode("This is another node", "bold", "https://www.supercombo.gg")
        self.assertNotEqual(node, node2)
        

if __name__ == "__main__":
    unittest.main()