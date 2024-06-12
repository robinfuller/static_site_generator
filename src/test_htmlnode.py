import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_node_eq(self):
        node1 = HTMLNode("h1", "Heading1", ["child1", "child2"], {"href": "https://www.supercombo.gg", "target": "_blank"})
        node2 = HTMLNode("h1", "Heading1", ["child1", "child2"], {"href": "https://www.supercombo.gg", "target": "_blank"})
        self.assertEqual(node1, node2)

    def test_node_props_not_provided(self):
        node1 = HTMLNode("h1", "Heading1", ["child1", "child2"])
        node2 = HTMLNode("h1", "Heading1", ["child1", "child2"])
        self.assertEqual(node1, node2)


    def test_prop(self):
        node1 = HTMLNode("p", "this text goes in the paragraph", ["child1", "child2"], {"href": "https://www.supercombo.gg", "target": "_blank"})
        test1  = " href=\"https://www.supercombo.gg\" target=\"_blank\""
        self.assertEqual(node1.props_to_html(), test1)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        
   
if __name__ == "__main__":
    unittest.main()