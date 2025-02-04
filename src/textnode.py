from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
	BOLD = 1
	ITALIC = 2
	TEXT = 3
	CODE = 4
	LINK = 5
	IMAGE = 6
	
class TextNode():
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	
	def __eq__(self, other):
		properties = ['text', 'text_type', 'url']
		for property in properties:
			if getattr(self, property) != getattr(other, property):
				return False
		return True
	
	def __repr__(self):
		return f'TextNode({self.text}, {self.text_type}, {self.url})'
	
	def text_node_to_html_node(self):
		match(self.text_type):
			case(TextType.TEXT):
				return LeafNode(None, self.text)
			case(TextType.BOLD):
				return LeafNode('b', self.text)
			case(TextType.ITALIC):
				return LeafNode('i', self.text)
			case(TextType.CODE):
				return LeafNode('code', self.text)
			case(TextType.LINK):
				return LeafNode('a', self.text, {'href':self.url})
			case(TextType.IMAGE):				
				return LeafNode('img', '', {'src':self.url, 'alt':self.text})
			case _:
				raise Exception("This type doesn't exist")

