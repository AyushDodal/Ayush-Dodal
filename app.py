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


    }

    .hero-edu{
        position: absolute;
        top: 90vh;
        left: -350px;
        font-size: 60px !important;
        color: black !important;
        white-space: nowrap;
        font-family: 'Courier Prime', monospace !important;

        animation: animate-about;
        animation-timeline: scroll();

    }

    .hero-about{
        position: absolute;
        top: 30vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;
        white-space: nowrap;


        animation: animate-about;
        animation-timeline: scroll();
        
        
    }


    .hero-projects-archive{
        position: absolute;
        top: 130vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;
        font-weight: 600;
    }

    .hero-projects-list{
        position: absolute;
        top: 140vh;
        left: -350px;
        color: black !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 60px !important;

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
        <h1 class="hero-title">hi, i'm ayush, an<br> ai engineer from mumbai</h1>
        
        
    </div>
    """,
    unsafe_allow_html=True
)





    
    





    

   

    
    
if __name__=="__main__": 
    main()
