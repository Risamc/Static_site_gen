from nodes import TextNode, TextType
from image_links_regex import * 
import re

def split_nodes_image(old_nodes):
    result = []

    for node in old_nodes:
        image_list_of_tuples = extract_markdown_images(node.text)
        imageless_text = re.sub(r"!\[(.*?)\]\((.*?)\)", 'IMAGE_PLACEHOLDER', node.text).split()
        #print(imageless_text)
        string = ''
        for word in imageless_text:
            
            if word == 'IMAGE_PLACEHOLDER':
                result.append(TextNode(string, node.text_type, node.url))
                string = ' '
                result.append(TextNode(image_list_of_tuples[0][0], TextType.IMAGE, image_list_of_tuples[0][1]))
                image_list_of_tuples.pop(0)
            else:
                string += f"{word} "
        result.append(TextNode(string, node.text_type, node.url))
    #print(result)
    return result


def split_nodes_link(old_nodes):
    result = []

    for node in old_nodes:
        link_list_of_tuples = extract_markdown_links(node.text)
        linkless_text = re.sub(r"\[(.*?)\]\((.*?)\)", 'LINK_PLACEHOLDER', node.text).split()
        
        string = ''
        for word in linkless_text:
            
            if word == 'LINK_PLACEHOLDER':
                result.append(TextNode(string, node.text_type, node.url))
                string = ' '
                result.append(TextNode(link_list_of_tuples[0][0], TextType.LINK, link_list_of_tuples[0][1]))
                link_list_of_tuples.pop(0)
            else:
                string += f"{word} "
        result.append(TextNode(string, node.text_type, node.url))
    #print(result)
    return result