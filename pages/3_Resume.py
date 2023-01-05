import base64

import streamlit as st

st.set_page_config(layout="wide")

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.title("Nanda Kishore Bellam Muralidhar")

with col2:
    st.text(" ")


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="850" height="800" ' \
    #               f'type="application/pdf"></iframe> '

    # pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="850" height="1000" ' \
    #               F'type="application/pdf"> '

    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe> '
    st.markdown(pdf_display, unsafe_allow_html=True)


show_pdf('Resume.pdf')

