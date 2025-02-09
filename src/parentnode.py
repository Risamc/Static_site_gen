from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props or {})
    
    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            self.children = []
        html_string = f'<{self.tag}>'

        for child in self.children:
            if isinstance(child, HTMLNode):
                html_string += child.to_html()
            else:
                html_string += str(child)

        html_string += f"</{self.tag}>"
        return html_string
