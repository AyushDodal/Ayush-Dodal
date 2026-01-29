import streamlit as st 





def main():

    st.markdown(
    """
    <style>
    .hero {
        min-height: 200vh;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 0;
        position: relative;
    }

    .hero img {
        width: 65vw;          /* controls horizontal size */
        max-width: 6000px;     /* cap for big screens */
        height: auto;
        opacity: 0.6;
    }




    .hero-title {
        position: absolute;
        top: 35vh;
        left: 5vw;
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

    
    





    

   

    
    
if __name__=="__main__": 
    main()
