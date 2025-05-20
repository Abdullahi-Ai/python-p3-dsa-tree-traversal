class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)  # remove first node
            
            if node['id'] == id:
                result.append(node)
            
            # Add children (if any) to the beginning of the list
            nodes_to_visit = node.get('children', []) + nodes_to_visit

        return result[0] if result else None
