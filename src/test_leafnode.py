import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode('p', 'this is the text in the paragraph')
        node2 = LeafNode('a', '')
        node3 = LeafNode('a', 'Click me!', 'not a link to malware <--')
        node.to_html()
        node2.to_html()
        node3.to_html()


if __name__ == '__main__':
    unittest.main()

