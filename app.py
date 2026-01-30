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
        top: 1vh;
        left: -350px;
        font-size: 120px !important;
        color: black !important;
        font-weight: 700;
        font-family: 'Courier Prime', monospace !important;
        white-space: nowrap;
        pointer-events: none;
        text-shadow: 0px 8px 20px rgba(0,0,0,0.7);

    }


    .hero-about{
        position: absolute;
        top: 90vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 90px !important;
        text-shadow: 0px 8px 20px rgba(0,0,0,0.7);

        animation: animate-about;
        animation-timeline: scroll();
        
        
    }

    @keyframes animate-about{
    from{
    opacity:0
    }
    to{
    opacity:1
    }
    }

    </style>
    """,
    unsafe_allow_html=True
)

    
    st.markdown(
    """
    <div class="hero">
        <img src="https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG">
        <h1 class="hero-title">Hi, I'm Ayush</h1>
        <h2 class="hero-about">I'm a Data Analyst from Mumbai. Lately I've been learning about AI.</h2>
        
    </div>
    """,
    unsafe_allow_html=True
)





    
    





    

   

    
    
if __name__=="__main__": 
    main()
