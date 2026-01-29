import streamlit as st 





def main():

    st.markdown(
    """
    <style>
    .hero {
        min-height: 120vh;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 10vh;
        position: relative;
    }

    .hero img {
        width: 40vw;          /* controls horizontal size */
        max-width: 600px;     /* cap for big screens */
        height: auto;
        opacity: 0.6;
    }

    .hero-title {
        position: absolute;
        top: 25vh;
        left: 10vw;
        font-size: clamp(48px, 8vw, 120px);
        color: white;
        font-weight: 700;
        white-space: nowrap;
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    
    st.markdown(
    """
    <div class="hero">
        <img src="https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG">
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
