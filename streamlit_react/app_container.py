import streamlit as st

from streamlit_react.renderer import render_vdom


class AppContainer:
    """
    The AppContainer class handles the creation and management of the root component,
    similar to how ReactDOM manages the root component in a React application.
    """

    def __init__(self):
        self.root_component = None

    def set_root_component(self, component_class):
        """
        Sets the root component of the app.
        Stores the component instance in st.session_state to avoid re-initialization.
        Args:
            component_class (type): The class of the root component to instantiate.
        """
        if "root_component" not in st.session_state:
            st.session_state.root_component = component_class()
            print("Creating and storing root component in session state.")
        else:
            print("Using existing root component from session state.")

        self.root_component = st.session_state.root_component

    def render(self):
        """
        Render the root component if it is set.
        """
        if self.root_component:
            vdom = self.root_component.render()
            render_vdom(vdom)


def create_root(component_class):
    """
    Creates an AppContainer and sets the root component class.
    Args:
        component_class (type): The class of the root component to instantiate.
    Returns:
        AppContainer: The created AppContainer instance.
    """
    app_container = AppContainer()
    app_container.set_root_component(component_class)
    return app_container
