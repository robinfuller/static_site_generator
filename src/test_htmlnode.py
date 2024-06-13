import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    #HTMLNode
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

    #LeafNode

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    #ParentNode

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span></div>"
            )    
   
if __name__ == "__main__":
    unittest.main()