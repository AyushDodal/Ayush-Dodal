import streamlit as st


def main():
  st.markdown(
    """
    <style>
    .stApp {
        background: 
          linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
          url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_5533.jpg");
        background-size: 50%;
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
