import streamlit as st 





def main():

    st.markdown(
    """
    <style>
    .block-container {
        padding: 0;
        max-width: 100%;
    }

    .hero {
        width: 100vw;
        height: 100vh;
        position: relative;
        margin-left: calc(-50vw + 50%);
        overflow: hidden;
    }

    .hero img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.5;
    }

    .hero-title {
        position: absolute;
        top: 50%;
        left: 40px;
        transform: translateY(-50%);
        color: white;
        font-size: clamp(48px, 8vw, 120px);
        font-weight: 700;
        white-space: nowrap;
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
