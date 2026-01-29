import streamlit as st 





def main():
    
    
    # Background Image
    st.markdown( 

        """ <style> 
        .stApp {  
        background-image:
        url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/i.jpg");
        background-repeat: no-repeat;
         } 
       
        </style> """, unsafe_allow_html=True 
    ) 
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
