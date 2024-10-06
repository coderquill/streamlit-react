from streamlit_react.renderer import render_vdom


class AppManager:
    """
    A centralized manager for handling state updates and triggering re-renders.
    """

    def __init__(self):
        self.root_component = None

    def set_root_component(self, root_component):
        """
        Set the root component for the application.
        Args:
            root_component (Component): The root component to render.
        """
        self.root_component = root_component

    def update(self):
        """
        Update the VDOM and trigger a re-render based on the current state of the root component.
        """
        if self.root_component:
            vdom = self.root_component.render()
            render_vdom(vdom)

    def set_state(self, new_state, component):
        """
        Update the state for a specific component and trigger an update.
        Args:
            new_state (dict): The new state values to update.
            component (Component): The component whose state is being updated.
        """
        component.state.update(new_state)
        self.update()


app_manager = AppManager()
