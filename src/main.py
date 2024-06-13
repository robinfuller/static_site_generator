from textnode import TextNode, textnode_to_html_node



def main():
    supercombo = TextNode("TextNode, yay", "link", "https://www.supercombo.gg")
    print(supercombo)
    supercombo_converted = textnode_to_html_node(supercombo)
    print(supercombo_converted.to_html())

main()