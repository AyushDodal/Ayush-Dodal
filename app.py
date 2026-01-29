import streamlit as st 





def main():

    

    # Background Image
    st.markdown( 
        """ <style> 
        .stApp { 
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
        url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG"); 
        background-size: contain; 
        background-position: center; 
        background-repeat: no-repeat; 
        min-height: 200vh } 
        </style> """, unsafe_allow_html=True ) 
        
    
    # TITLE
    #st.title("Ayush Dodal") 
    st.markdown( 
        """ <style> 
        @import url('https://fonts.cdnfonts.com/css/courier-prime'); 
        .hero-title { 
        white-space: wrap !important; 
        font-size: 125px !important; 
        font-weight: 700 !important; 
        color: white !important; 
        font-family: 'Courier Prime' !important;
        position: fixed;
        top: 380px;
        left: 400px; 
        } </style> """, unsafe_allow_html=True) 
    
    st.markdown('<h1 class="hero-title", style="100vh">Ayush Dodal</h1>', unsafe_allow_html=True) 

    # ABOUT
    st.markdown(
        """<style>
        .about{
        font-size: 75px;
        color: white;
        top: 500px;
        }
        </style>""", unsafe_allow_html=True
    )
    st.markdown('<div class="about">About</div>', unsafe_allow_html=True)

    
    
if __name__=="__main__": 
    main()
