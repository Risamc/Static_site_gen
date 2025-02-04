import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_PN(self):
        node = ParentNode('p', [
            LeafNode('p', 'this is the text in the paragraph'),
            LeafNode('a', ''),
            LeafNode('a', 'Click me!', 'not a link to malware <--')
        ])
        node2 = ParentNode('p', [
            node,
            LeafNode('a', 'Click me!', 'not a link to malware <--')
        ])
        node3 = ParentNode('p', None, None)
        node4 = ParentNode('p', None)

        node.to_html()
        node2.to_html()
        #node3.to_html()
        #node4.to_html()
if __name__ == "__main__":
    unittest.main()
