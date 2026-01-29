import streamlit as st 





def main():
    
    
        
    st.markdown(
    """
    <style>
    @import url('https://fonts.cdnfonts.com/css/courier-prime');
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>




    .hero {
        min-height: 200vh;
        display: flex;
        justify-content: center;
        align-items: flex-start;
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
        left: -350px;
        font-size: 120px !important;
        color: white !important;
        font-weight: 700;
        font-family: 'Courier Prime', monospace !important;
        white-space: nowrap;
        pointer-events: none;
        text-shadow: 0px 8px 20px rgba(0,0,0,0.7);

    }


    .about{
    top: 120vh;
    left: -350px;
    color: white !important;
    font-size: 90px !important;
    text-shadow: 0px 8px 20px rgba(0,0,0,0.7);
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


    st.markdown(
    """
    <div class="about">
        <h2>About Me</h2>
        <p>
        AI Engineer focused on data, LLMs, and real-world systems.
        I build things that actually ship.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


    
    





    

   

    
    
if __name__=="__main__": 
    main()
