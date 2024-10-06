import streamlit as st
from streamlit_react.core import VNode
import uuid


class Text:
    """
    Represents a text component.
    """

    def __init__(self, text, key=None):
        self.text = text
        self.key = key

    def render(self):
        print(f"Rendering Text component with key: {self.key}")
        return VNode(
            type="text",
            key=self.key,
            props={"content": self.text}
        )


class TextInputComponent:
    """
    A controlled component for a text input box that relies on props and callbacks for state management.
    """

    def __init__(self, label="Enter a new item", key=None, value="", on_change=None):
        """
        Initialize the TextInputComponent as a controlled component.

        Args:
            label (str): The label to display above the input field.
            key (str): The unique key for this component's state management.
            value (str): The current value of the input field.
            on_change (callable): Optional callback function to call when the input changes.
        """
        self.label = label
        self.key = key if key else "text_input_component"
        self.value = value
        self.on_change = on_change

    def render(self):
        """
        Render the TextInputComponent and return a VNode representation.

        Returns:
            VNode: The virtual DOM node representation of the input field.
        """
        return VNode(
            type="text_input",
            key=self.key,
            props={
                "label": self.label,
                "value": self.value,
                "on_change": self._on_change
            }
        )

    def _on_change(self):
        """
        Internal method to handle input changes and notify the parent component.
        """
        new_value = st.session_state[self.key]
        if self.on_change:
            self.on_change(new_value)


class Button:
    """
    Represents a button component.
    """

    def __init__(self, label, key=None, on_click=None):
        self.label = label
        self.key = key
        self.on_click = on_click

    def render(self):
        print(f"Rendering Button component with key: {self.key}")
        return VNode(
            type="button",
            key=self.key,
            props={
                "label": self.label,
                "on_click": self.on_click
            }
        )


class Container:
    """
    A container component that can hold other components.
    """

    def __init__(self, children=None, key=None, props=None):
        self.key = key
        self.props = props if props else {}
        self.children = children or []

    def render(self):
        rendered_children = [
            child.render() if hasattr(child, "render") else child for child in self.children
        ]
        return VNode(
            type="container",
            key=self.key,
            props=self.props,
            children=rendered_children
        )


class Component:
    """
    Base Component class for managing state and triggering re-renders.
    Each component has a unique ID to track its state and render cycle.
    """

    def __init__(self):
        self.component_id = str(uuid.uuid4())

    def render(self):
        """
        Render the component. Should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")
