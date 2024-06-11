import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node1 = HTMLNode("p", "this text goes in the paragraph", ["child1", "child2"], {"href": "https://www.supercombo.gg", "target": "_blank"})
        test1  = " href=\"https://www.supercombo.gg\" target=\"_blank\""
        self.assertEqual(node1.props_to_html(), test1)

