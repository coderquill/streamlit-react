import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

def increase_count():
    st.session_state.count += 1


def decrease_count():
    st.session_state.count -= 1


st.title("Simple Counter App")

st.write(f"Current Count: {st.session_state.count}")

st.button("Increase", on_click=increase_count)
st.button("Decrease", on_click=decrease_count)
