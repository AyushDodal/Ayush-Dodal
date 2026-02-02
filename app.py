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
        font-size: 105px !important;
        color: black !important;
        font-weight: 700;
        font-family: 'Courier Prime', monospace !important;
        white-space: nowrap;
        pointer-events: none;
        animation: fadeIn;
        animation-duration: 2s;
        animation-timing-function: ease-out;
        animation-fill-mode: backwards;
    }

    .hero-about{
        position: absolute;
        top: 30vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;
        white-space: nowrap;
        pointer-events: none;
        animation: fadeIn;
        animation-duration: 2s;
        animation-timing-function: ease-out;
        animation-delay: 2s;
        animation-fill-mode: backwards;
    }

    .hero-edu{
        position: absolute;
        top: 90vh;
        left: -350px;
        font-size: 60px !important;
        color: black !important;
        white-space: nowrap;
        font-family: 'Courier Prime', monospace !important;


    }




    .hero-projects-archive{
        position: absolute;
        top: 90vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;
        font-weight: 600;
        animation: fadeIn;
        animation-timeline: view();
        animation-timing-function: ease-out;
        animation-duration: 1s;
        animation-fill-mode: backwards;
    }

    .hero-projects-list{
        position: absolute;
        top: 100vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;
        animation: fadeIn;
        animation-timeline: view();
        animation-timing-function: ease-out;
        animation-duration: 1s;
        animation-fill-mode: backwards;
    }
    
    .hero-projects-list a {
        color: black;
        text-decoration: none;
        animation: fadeIn;
        animation-timeline: view();
        animation-timing-function: ease-out;
        animation-duration: 1s;
        animation-fill-mode: backwards;
    }
    
    .hero-projects-list a:hover {
        text-decoration: underline;
        animation: fadeIn;
        animation-timeline: view();
        animation-timing-function: ease-out;
        animation-duration: 1s;
        animation-fill-mode: backwards;
    }


    .contact{
        position: absolute;
        top: 195vh;
        left: 190px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;
    }

    .insta-contact{
        position: absolute;
        top: 205vh;
        left: 700px;
        width: 2vw;
        height: auto;
        
    }

    .github-contact{
        position: absolute;
        top: 205vh;
        left: 0px;
        width: 2vw;
        height: auto;
    }

    .linkedin-contact{
        position: absolute;
        top: 205vh;
        left: 350px;
        width: 2vw;
        height: auto;
    }

    @keyframes animate-on-scroll{
    from{
    opacity:0
    }
    to{
    opacity:1
    }
    }


    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(60px); /* Optional: add a slight upward movement */
          }
      to {
        opacity: 1;
        transform: translateY(0);
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
        <h1 class="hero-title">hi, i'm ayush, an<br> ai engineer from mumbai</h1>
        <p class="hero-about">I like building things that work — <br>data systems, 
        ai tools, and ideas that <br>actually ship.</p>
        <p class="hero-projects-archive">projects archive</p>
        <p class="hero-projects-list">
        <a href="https://github.com/AyushDodal/repai">
        fitness tracking ai agent</a><br>
        <a href="https://github.com/AyushDodal/RagBOT">
        rag chatbot</a><br>
        <a href="https://github.com/AyushDodal/AQI_Analyzer">
        aqi analyzer</a><br>
        <a href="https://github.com/AyushDodal/Heart-Disease-Classification">
        heart disease classifier</a>
        </p>
    </div>
    <div class="contact">contact me!</div>
    <div class="insta-contact">
        <a href="https://www.instagram.com/ayush_dodal/">
            <img src="https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/icons8-instagram-logo-94.png">
        </a>
    </div>
    <div class="github-contact">
        <a href="https://github.com/AyushDodal">
            <img src="https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/icons8-github-logo-94.png">
        </a>
    </div>
    <div class="linkedin-contact">
        <a href="https://www.linkedin.com/in/ayush-dodal-b5646016b/">
            <img src="https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/icons8-linkedin-logo-48.png">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
    
    
if __name__=="__main__": 
    main()



