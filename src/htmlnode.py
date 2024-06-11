import typing
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        
        string  = ""
        for k, v in self.props.items():
            string = string + f" {k}=\"{v}\""
        return string
    
    def __repr__(self):
        return f"HTMLNode {self.tag}, {self.value}, {self.children}, {self.props}"