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
  st.markdown(
    """
    <style>
    @import url('https://fonts.cdnfonts.com/css/courier-prime');
    .hero-title {
        white-space: nowrap !important;
        font-size: 125px !important;
        font-weight: 700 !important;
        color: white !important;
        font-family: 'Courier Prime' !important;
        text-align: left !important;
        margin-top: 40px !important;
    }
    </style>
    """,
    unsafe_allow_html=True)
  st.markdown('<h1 class="hero-title">Ayush Dodal</h1>', unsafe_allow_html=True)
  


if __name__=="__main__":
  main()
