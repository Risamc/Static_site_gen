from markdown_to_blocks import markdown_to_blocks
from block_to_block import block_to_block_type
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    #print(blocks)
    ParentNode = HTMLNode('div', None)
    
    for block in blocks:
        #print(block + '\n')
        block_type = block_to_block_type(block)
        
        block_node = None
        
        match(block_type):
            case('QUOTE BLOCK'):
                block_node = (HTMLNode('blockquote', block))
            case('PARAGRAPH'):
                block_node = (HTMLNode('p', block))
            case('UNORDERED LIST'):
                list_items = block.split('\n')
                children_list = []
                for item in list_items:
                    children_list.append(HTMLNode('li', item))
                block_node = (HTMLNode('ul', None, children_list))
            case('ORDERED LIST'):
                list_items = block.split('\n')
                children_list = []
                for item in list_items:
                    children_list.append(HTMLNode('li', item))
                block_node = (HTMLNode('ol', None, children_list))
            case('CODE BLOCK'):
                block_node = ('pre', None, [HTMLNode('code', block)])
            case('HEADING BLOCK'):
                counter = 0
                for char in block[:6]:
                    if char == '#':
                        counter += 1
                    else:
                        break
                block_node = (HTMLNode(f'h{counter}', block))
            
        if block_node:
            ParentNode.children.append(block_node)
    
    #print(ParentNode)
    return ParentNode

(markdown_to_html_node(
"""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

"""
))