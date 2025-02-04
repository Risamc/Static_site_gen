from textnode import TextNode, TextType
import unittest
from split_nodes_delimiter import split_nodes_delimiter

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a *italics block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        print(new_nodes)

if __name__ == "__main__":
    unittest.main()