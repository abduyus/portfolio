import streamlit as st
import streamlit.components.v1 as components
# title and about me section

st.title("Yusuf Abdur-Rasheed")

st.subheader("About Me")
st.info("Hi! I am Yusuf, A student studying at Solihull School passionate about" 
        " programming based in Solihull, UK. 📍")



components.html(
    """
    <div id="badges">
        <a target="_blank" rel="noopener" data-a11y="false" aria-label="Link to https://github.com/abduyus" href="https://github.com/abduyus" class="css-hy23rq e1dx16qw0"><svg width="40" height="40" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 0C3.1325 0 0 3.21173 0 7.17706C0 10.3529 2.00375 13.0353 4.78625 13.9863C5.13625 14.0491 5.2675 13.8338 5.2675 13.6454C5.2675 13.4749 5.25875 12.9097 5.25875 12.3087C3.5 12.6406 3.045 11.8691 2.905 11.4653C2.82625 11.259 2.485 10.622 2.1875 10.4516C1.9425 10.317 1.5925 9.98508 2.17875 9.97611C2.73 9.96714 3.12375 10.4964 3.255 10.7118C3.885 11.7973 4.89125 11.4923 5.29375 11.3039C5.355 10.8374 5.53875 10.5234 5.74 10.3439C4.1825 10.1645 2.555 9.54549 2.555 6.80026C2.555 6.01976 2.82625 5.37382 3.2725 4.87143C3.2025 4.692 2.9575 3.95635 3.3425 2.96951C3.3425 2.96951 3.92875 2.78111 5.2675 3.70516C5.8275 3.54367 6.4225 3.46293 7.0175 3.46293C7.6125 3.46293 8.2075 3.54367 8.7675 3.70516C10.1063 2.77214 10.6925 2.96951 10.6925 2.96951C11.0775 3.95635 10.8325 4.692 10.7625 4.87143C11.2087 5.37382 11.48 6.01079 11.48 6.80026C11.48 9.55446 9.84375 10.1645 8.28625 10.3439C8.54 10.5682 8.75875 10.9988 8.75875 11.6717C8.75875 12.6316 8.75 13.4032 8.75 13.6454C8.75 13.8338 8.88125 14.0581 9.23125 13.9863C11.9963 13.0353 14 10.3439 14 7.17706C14 3.21173 10.8675 0 7 0Z" fill="#73737D"></path></svg><span class="css-mglztx e1dx16qw1"></span></a>
    </div>
    """
)

# How to add github profile views, add it in the above "components.html" block of code
# <a href="github.com/abduyus">
# <img src="https://komarev.com/ghpvc/?username=abduyus&style=flat-square&color=blue" alt=""/>
#   </a>

st.subheader("🧰 Tools and Languages: ")


components.html(
    """
    <img align="left" alt="Git" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />

    <img align="left" alt="HTML" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain.svg" />
    <img align="left" alt="CSS" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain.svg" />

    <img align="left" alt="Python" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" />

    <img align="left" alt="GitHub" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />

    """)



