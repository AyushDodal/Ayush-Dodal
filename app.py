import streamlit as st

def main():

    # --- AOS (load once) ---
    st.markdown(
        """
        <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
        <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
        <script>
          document.addEventListener("DOMContentLoaded", function () {
            AOS.init({ once: true });
          });
        </script>
        """,
        unsafe_allow_html=True
    )

    # --- GLOBAL STYLES ---
    st.markdown(
        """
        <style>
        .stApp {
            background:
              linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
              url("https://raw.githubusercontent.com/AyushDodal/Ayush-Dodal/main/images/IMG_6667.JPG");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        @import url('https://fonts.cdnfonts.com/css/courier-prime');

        .hero {
            height: 100vh;
            position: relative;
        }

        .hero-title {
            position: absolute;
            top: 40%;
            left: 40px;
            font-size: 120px;
            font-weight: 700;
            color: white;
            font-family: 'Courier Prime', monospace;
            white-space: nowrap;
        }

        .section {
            max-width: 800px;
            margin: 0 auto;
            padding: 120px 20px;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- HERO ---
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title" data-aos="fade-right">
                Ayush&nbsp;Dodal
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- ABOUT ---
    st.markdown(
        """
        <div class="section" data-aos="fade-up">
            <h2>About Me</h2>
            <p>
            AI Engineer focused on data, LLMs, and real-world systems.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- PROJECTS ---
    st.markdown(
        """
        <div class="section" data-aos="fade-up">
            <h2>Projects</h2>
            <ul>
                <li>RAG Chatbot</li>
                <li>Kafka Streaming Pipeline</li>
                <li>Route Optimization System</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
