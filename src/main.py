from textnode import TextNode
import htmlnode


def main():
    supercombo = TextNode("TextNode, yay", "link", "https://www.supercombo.gg")
    print(supercombo)
    supercombo_converted = htmlnode.textnode_to_html_node(supercombo)
    print(supercombo_converted.to_html())

main()