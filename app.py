import streamlit as st 





def main():
    st.markdown(
    """
    <div class="hero">
        <img src="https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG"
             style="width:150%; height:200vh; object-fit:cover; opacity:0.5;">
        <h1 class="hero-title">Ayush Dodal</h1>
    </div>
    """,
    unsafe_allow_html=True
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



    

   

    
    
if __name__=="__main__": 
    main()
