from markdown_to_blocks import markdown_to_blocks
from block_to_block import block_to_block_type
from nodes import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    #print(blocks)
    parentnode = HTMLNode('div', None)
    
    for block in blocks:
        #print(block + '\n')
        block_type = block_to_block_type(block)
        
        block_node = None
        
        match(block_type):
            case('QUOTE BLOCK'):
                block.strip('>').strip()
                block_node = (HTMLNode('blockquote', block))
            case('PARAGRAPH'):
                block_node = (HTMLNode('p', block))
            case('UNORDERED LIST'):
                list_items = block.split('\n')
                children_list = []
                for item in list_items:
                    item = item[2:]
                    children_list.append(HTMLNode('li', item))
                block_node = (HTMLNode('ul', None, children_list))
            case('ORDERED LIST'):
                list_items = block.split('\n')
                children_list = []
                for item in list_items:
                    num_and_item = item.split('.', 1)
                    children_list.append(HTMLNode('li', num_and_item[1].strip()))
                block_node = (HTMLNode('ol', None, children_list))
            case('CODE BLOCK'):
                block = block.strip('`')
                block_node = HTMLNode('pre', None, [HTMLNode('code', block)])
            case('HEADING BLOCK'):
                counter = 0
                for char in block[:6]:
                    if char == '#':
                        counter += 1
                    else:
                        break
                block = block.strip('#').strip()
                block_node = (HTMLNode(f'h{counter}', block))
            
        if block_node:
            parentnode.children.append(block_node)
    
    #print(parentnode)
    return parentnode
