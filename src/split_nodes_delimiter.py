from nodes import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	if old_nodes is None:
		raise Exception('No node is provided')
	result = []
	for node in old_nodes:

		if not isinstance(node, TextNode):
			result.append(node)
			continue
		split_node = node.text.split(delimiter)
		for n in range(len(split_node)):
			if n % 2 == 0:
				result.append(TextNode(split_node[n], node.text_type))
			elif n % 2 != 0:
				result.append(TextNode(split_node[n], text_type))
	return result