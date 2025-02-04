from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_img_lnk import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

def text_to_textnodes(text):
    textnode = TextNode(text, TextType.TEXT)

    return (
    split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter([textnode],
                    '**', TextType.BOLD),
                '*', TextType.ITALIC),
            '`', TextType.CODE)
        )
    )
    )
    

      

(
text_to_textnodes('This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')
)