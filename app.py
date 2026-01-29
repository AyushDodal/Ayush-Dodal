import streamlit as st 





def main():

    

    # Background Image
    st.markdown( 

        """ <style> 
        .stApp {  
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
        url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG"); 
        background-position-x: center;
        background-position-y: center;
        background-repeat: no-repeat;
        background-size: 1600px 200vh;
        background-attachment: scroll !important;
        animation-name: animation;
        animation-timeline: scroll();
         } 
        @keyframes animate{
        to{background-image: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9));}
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
         
        } </style> """, unsafe_allow_html=True) 
    
    st.markdown('<h1 class="hero-title", style="100vh">Ayush Dodal</h1>', unsafe_allow_html=True) 


    for i in range(100):
        st.write("i")
    

   

    
    
if __name__=="__main__": 
    main()
