def markdown_to_blocks(markdown):
    split_md = markdown.split('\n\n')
    result = []
    for string in split_md:
        result.append(string)
    return result

print(markdown_to_blocks(
"""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
))