from streamlit_react.app_container import create_root
from streamlit_react.components import Component
from streamlit_react.core import VNode
from streamlit_react.hooks import use_state


class Counter(Component):
    """
    A simple Counter component using the use_state hook.
    """

    def __init__(self):
        super().__init__()

    def increment(self):
        """
        Increment the count by 1 and update state.
        """
        self.set_count(self.count + 1)

    def decrement(self):
        """
        Decrement the count by 1 and update state.
        """
        self.set_count(self.count - 1)

    def render(self):
        """
        Render the component's UI.
        The render method calls use_state for the component's state.
        """
        self.count, self.set_count = use_state(f"counter_{self.component_id}_count", 0)

        return VNode(
            type="container",
            key=f"counter_container_{self.component_id}",
            props={},
            children=[
                VNode(type="text", key=f"count_display_{self.component_id}",
                      props={"content": f"Current Count: {self.count}"}),
                VNode(type="button", key=f"increment_button_{self.component_id}",
                      props={"label": "Increase", "on_click": self.increment}),
                VNode(type="button", key=f"decrement_button_{self.component_id}",
                      props={"label": "Decrease", "on_click": self.decrement})
            ]
        )


root = create_root(Counter)
root.render()
