import unittest

from textnode import TextNode, TextType

class TestTXTtoHTML(unittest.TestCase):
    def test_eq(self):
        node = TextNode('text', TextType.TEXT)
        node2 = TextNode('TEXT', TextType.BOLD)
        node3 = TextNode('text in italics', TextType.ITALIC)
        node4 = TextNode('code text', TextType.CODE)
        node5 = TextNode('this is a video', TextType.LINK, 'youtube.com')
        node6 = TextNode('this is ALT', TextType.IMAGE, 'this is the URL')
        node.text_node_to_html_node()
        node2.text_node_to_html_node()
        node3.text_node_to_html_node()
        node4.text_node_to_html_node()
        node5.text_node_to_html_node()
        node6.text_node_to_html_node()




if __name__ == "__main__":
    unittest.main()