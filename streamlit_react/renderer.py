import streamlit as st

from streamlit_react.components import Container
from streamlit_react.core import VNode


def render_vdom(vnode, depth=0):
    """
    Recursively renders the virtual DOM nodes using Streamlit functions.
    Includes logging to help identify non-VNode objects and their keys.
    """
    if isinstance(vnode, Container):
        container_vnode = vnode.render()
        vnode = container_vnode
    if not isinstance(vnode, VNode):
        node_key = getattr(vnode, "key", "No key attribute found")
        print(f"{' ' * depth * 2}Error: Expected a VNode, but got {type(vnode).__name__}.")
        print(f"{' ' * depth * 2}Key of the problematic object: {node_key}")
        print(f"{' ' * depth * 2}Contents of the problematic object: {vnode}")
        raise TypeError(f"Expected a VNode, but got {type(vnode).__name__} with key: {node_key}")

    print(f"{' ' * depth * 2}Rendering VNode: {vnode.type}, Key: {vnode.key}")

    if vnode.type == "container":
        print(f"{' ' * depth * 2}Rendering a container VNode with {len(vnode.children)} children.")
        for child in vnode.children:
            render_vdom(child, depth + 1)
    elif vnode.type == "text":
        st.write(vnode.props["content"])
    elif vnode.type == "button":
        if st.button(vnode.props["label"], key=vnode.key):
            if "on_click" in vnode.props:
                vnode.props["on_click"]()

    elif vnode.type == "text_input":
        value = vnode.props.get("value", "")
        key = vnode.key
        label = vnode.props.get("label", "")
        on_change = vnode.props.get("on_change", None)

        st.text_input(label=label, value=value, key=key, on_change=on_change)
    elif vnode.type == "checkbox":
        st.checkbox(label=vnode.props["label"], value=vnode.props.get("value", False), key=vnode.key,
                    on_change=vnode.props.get("on_change", None))
    else:
        print(f"{' ' * depth * 2}Unknown VNode type: {vnode.type}, Key: {vnode.key}")
        raise TypeError(f"Unknown VNode type: {vnode.type}, Key: {vnode.key}")
