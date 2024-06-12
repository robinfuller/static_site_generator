import typing

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""    
        string  = ""
        for k, v in self.props.items():
            string = string + f" {k}=\"{v}\""
        return string
    
    def __repr__(self):
        return f"HTMLNode {self.tag}, {self.value}, {self.children}, {self.props}"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value 
            and self.children == other.children
            and self.props == other.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None ):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode {self.tag}, {self.value}, {self.props}"
    
    def __eq__(self, other):
        super().__eq__(self.tag, self.value, self.props)

    def props_to_html(self):
        return super().props_to_html()

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return super().__repr__() ##check if this works without the value property or if a new __repr__ is needed

    def __eq__(self, other):
        return super().__eq__(self.tag, self.children, self.props)

    def to_html(self):
        if self.children == [] or self.children is None:
            raise ValueError("No Children Provided to Parentnode")
        children_html = ""
        for child in self.children:
            children_html  += child.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"
    