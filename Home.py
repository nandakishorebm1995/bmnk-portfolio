import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

embed_component = {'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer 
type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" 
data-theme="dark" data-type="VERTICAL" data-vanity="nanda-kishore-bellam-muralidhar-25594b186" data-version="v1"><a 
class="badge-base__link LI-simple-link" href="https://de.linkedin.com/in/nanda-kishore-bellam-muralidhar-25594b186
?trk=profile-badge">Nanda Kishore Bellam Muralidhar</a></div>""" }

with col1:
    st.title("Nanda Kishore Bellam Muralidhar")

with col2:
    st.text(" ")
    with st.sidebar:
        components.html(embed_component['linkedin'], height=310)

col1, col2 = st.columns([1.5, 1.9])

with col1:
    st.text(" ")
    st.text(" ")
    st.image("images/my_photo.png", width=400)

with col2:
    st.text(" ")
    st.subheader("About me")
    content1 = f"""Hi, I am Nanda Kishore, currently working as a research scientist at Technical University 
    Braunschweig, Germany. During my two and a half year research within the FOR3022 group (funded by """
    content3 = f""") I taught myself about the state of the art technology in developing smart structures for 
    aircraft and automobiles. Being a computational engineer it is very fascinating for me to understand the underlying
    physics and establish a novel technology that exploits the propagation characteristics of Lamb waves, finite element 
    modeling and stochastic data-assimilation algorithms for damage identification in fiber metal laminate 
    structures. """
    st.write(content1,
             "[DFG](https://gepris.dfg.de/gepris/projekt/418311604?context=projekt&task=showDetail&id=418311604&)",
             content3)

footer = """
    <style>
    footer {visibility: hidden;}

    footer:hover,  footer:active {
        color: #ffffff;
        background-color: transparent;
        text-decoration: underline;
        transition: 400ms ease 0s;
    }

    footer:after {
        content:'Nanda Kishore BM'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
    }
    </style>
    """
st.markdown(footer, unsafe_allow_html=True)
