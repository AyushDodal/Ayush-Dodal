import streamlit as st 





def main():

    st.markdown(
    """
    <style>
    .scroll-watcher {
        position: fixed;
        top: 0;
        left: 0;
        height: 10px;
        width: 100%;
        background-color: black;
        transform-origin: left;
        transform: scaleX(0);
        z-index: 9999;
    }
    </style>

    <div class="scroll-watcher"></div>

    <script>
    const bar = document.querySelector(".scroll-watcher");

    const container = document.querySelector("section.main");

    container.addEventListener("scroll", () => {
        const scrollTop = container.scrollTop;
        const scrollHeight = container.scrollHeight - container.clientHeight;
        const progress = scrollTop / scrollHeight;
        bar.style.transform = `scaleX(${progress})`;
    });
    </script>
    """,
    unsafe_allow_html=True
)

    
    st.markdown( 
        """ <style> 
        .stApp { 
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
        url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG"); 
        background-size: contain; 
        background-position: center; 
        background-repeat: no-repeat; 
        min-height: 200vh; } 
        </style> """, unsafe_allow_html=True ) 
        
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
        position: absolute; 
        top: 360px; 
        left: -400px; 
        } </style> """, unsafe_allow_html=True) 
    
    st.markdown('<h1 class="hero-title", style="100vh">Ayush Dodal</h1>', unsafe_allow_html=True) 

    
    
if __name__=="__main__": 
    main()
