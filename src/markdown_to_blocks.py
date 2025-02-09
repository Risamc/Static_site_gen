def markdown_to_blocks(markdown):
    split_md = markdown.split('\n\n')
    result = []
    for string in split_md:
        result.append(string)
    return result

