import streamlit as st


def main():
  st.markdown(
    """
    <style>
    .stApp {
        background: 
          linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)),
          url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG");
        background-size: 50%;
        backgorund-height: 100%
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
  )

  st.title("Ayush Dodal")

if __name__=="__main__":
  main()
