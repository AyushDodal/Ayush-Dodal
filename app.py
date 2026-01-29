import streamlit as st


def main():
  st.markdown(
    """
    <style>
    .stApp {
        background: 
          linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
          url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG");
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 200vh;
    }
    </style>
    """,
    unsafe_allow_html=True
  )

  #st.title("Ayush Dodal")
  st.markdown('<h1 class="hero">Ayush Dodal</h1>', unsafe_allow_html=True)


if __name__=="__main__":
  main()
