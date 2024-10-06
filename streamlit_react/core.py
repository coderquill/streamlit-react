class VNode:
    """
    Represents a virtual DOM node.
    """

    def __init__(self, type, key=None, props=None, children=None):
        # Type of element, e.g., "text", "button", "container"
        self.type = type
        # Unique key to identify the node
        self.key = key
        self.props = props or {}
        # Child nodes
        self.children = children or []

    def __repr__(self):
        return f"VNode(type={self.type}, key={self.key}, props={self.props})"
