import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
 st.subheader("Hi I am Reign Heinz")
 st.title("A Students from SNSU")
 st.write("I am passionate to learn from this amazing school")

# ---- WHAT I DO ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
     """
