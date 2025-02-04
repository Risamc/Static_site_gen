from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
		if not old_nodes:
			raise Exception('No node is provided')
		result = []
		for node in old_nodes:
			split_node = node.text.split(delimiter)
			
			for n in range(len(split_node)):
				if n % 2 == 0:
					result.append(TextNode(split_node[n], node.text_type))
				elif n % 2 != 0:
					result.append(TextNode(split_node[n], text_type))
		return result