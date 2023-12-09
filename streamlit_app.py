import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
 st.subheader("Hey,I'm Almina Adlawon,an 18-year-old")
 st.title("Computer Engineering student at SNSU")
 st.write("I am passionate about turning ideas into code!")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Journey into Coding")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column
    with text_column
        st.write(
            """
           My journey into coding began when I was 18 years old and started studying Computer Engineering at SNSU. At first, I wasn't sure if I could understand it, and I felt a bit unsure about my abilities.
In the beginning, I learned that coding is like a language that helps you create things on computers. It was exciting to realize that I could turn my ideas into something real using code. This discovery marked the beginning of my coding adventure.

As I learned more, there were times when coding seemed difficult. I sometimes felt like I wasn't smart enough to figure it out. But I learned that it's okay to find things hard, and it doesn't mean you're not good enough. Everyone faces challenges when learning something new.

Now, I'm working on different projects that I'm proud of. Each project teaches me something new about coding. Even though I'm not an expert, I enjoy the process of making things with code and seeing my progress.

In conclusion, my coding journey is still ongoing. I'm not perfect, but I'm learning every day. Coding is like a puzzle, and it's okay not to have all the pieces at once. I'm excited to see where this journey takes me, and I'm grateful for the chance to learn and grow through coding.
            """
        )


     
