import streamlit as st


def main():
  st.markdown(
    """
    <style>
    .stApp {
        background: 
          linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
          url("images/IMG_5533.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
  )

  st.title("Ayush Dodal")

if __name__=="__main__":
  main()
