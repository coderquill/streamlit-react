import streamlit as st

def use_state(key, initial_value=None):
    """
    Custom use_state hook to manage state directly in Streamlit.
    Args:
        key (str): The unique key for the state.
        initial_value (Any): The initial value of the state.

    Returns:
        state: The current state value.
        set_state: A function to update the state.
    """
    if key not in st.session_state:
        st.session_state[key] = initial_value
        print(f"Initialized state: {key} = {initial_value}")

    def set_state(new_value):
        st.session_state[key] = new_value
        print(f"Updated state: {key} = {new_value}")
        st.rerun()

    return st.session_state[key], set_state
