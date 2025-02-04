import unittest

from htmlnode import HTMLNode 


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', "This is a html node", [], {"href": "https://www.google.com"})
        node3 = HTMLNode('a', 'This is not a html node', [], {})
        node4 = HTMLNode('h1', 'This is not a html node', [], {"href": "https://www.google.com"})
        node.props_to_html()
        #node3.to_html()
        node4.__repr__()


if __name__ == "__main__":
    unittest.main()