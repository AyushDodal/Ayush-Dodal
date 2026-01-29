import streamlit as st 





def main():

    

    # Background Image
    st.markdown( 
        """ <style> 
        .stApp { 
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
        url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG"); 
        background-size: 70% 200%; 
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: scroll !important;
         } 
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
        top: 360px;
        left: 400px; 
        } </style> """, unsafe_allow_html=True) 
    
    st.markdown('<h1 class="hero-title", style="100vh">Ayush Dodal</h1>', unsafe_allow_html=True) 
    

   

    
    
if __name__=="__main__": 
    main()
