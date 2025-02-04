import re

def block_to_block_type(block_text):
    if block_text.startswith('>'):
        lines = block_text.split('\n')
        x = 0
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                x += 1
        if x == len(lines): 
            return "QUOTE BLOCK"
        return "PARAGRAPH"
    
    elif block_text.startswith('* ') or block_text.startswith('- '):
        lines = block_text.split('\n')
        x = 0
        for line in lines:
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                x += 1
        if x == len(lines):
            return "UNORDERED LIST"
        return "PARAGRAPH"
    
    elif re.match(r'^\d+\. ', block_text):
        block_text = block_text.strip()
        lines = block_text.split('\n')
        x = 1
        for line in lines:
            line = line.strip()
            if line.startswith(f"{x}. "):
                x += 1
            else:
                return  "PARAGRAPH"
        return "ORDERED LIST"
    
    elif block_text.startswith('```') and block_text.endswith('```'):
        return "CODE BLOCK"
    
    elif bool(re.match(r"^#{1,6} ", block_text)):
        return "HEADING BLOCK"

    return f"PARAGRAPH"