import streamlit as st

st.set_page_config(layout="wide")

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)


col1, col2 = st.columns([2, 1])

with col1:
    st.title("Nanda Kishore Bellam Muralidhar")
    st.text(" ")
    st.subheader("Project: FOR3022")
    st.markdown("- #### [Parametric model order reduction in FMLs](https://doi.org/10.3390/modelling2040031)")

with col2:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.image("images/SHM.png", width=250)
    st.markdown(":orange[_Image reused from project proposal_]")

st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; is an approach to considerably decrease the computation "
            "effort to solve the system of equations that mimic the underlying physics of Lamb wave propagation in "
            "FMLs. As the damage identification is set to be accomplished through a stochastic inference procedure "
            "which requires to solve the FEM model several thousand times, the FEM simulation should happen as quickly "
            "as possible. Given that the excitation of the Lamb waves happen at a very high frequency, a very fine "
            "spatial discretization of the FML domain is required to capture the dynamics. This consequently results in"
            "a very large number of degrees of freedom to be solved in FEM. That is when the parametric model order "
            "reduction comes into picture. It aims to reduce the order of the system and accelerates the simulation"
            "speed. In our research work, we were able to accelerate the simulation by a speedup factor of "
            "approximately 34. This improvement is very well appreciated in the inverse procedure in the later part "
            "of our project.")

st.markdown("- #### [Numerical study of Lamb wave propagation in FMLs](https://doi.org/10.3390/acoustics4030032)")
st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; this article focuses mainly on the numerical analysis of Lamb "
            "wave propagation in fiber metal laminate structures. The dispersion diagrams derived from the analytical "
            "framework and numerical simulations are first determined and compared to each other. Subsequently, "
            "the displacement fields are computed using the global matrix method for two excitation frequencies. The "
            "results derived from the analytical framework is used to validate the numerically determined "
            "displacement fields based on a 2D and a 3D modeling approach.")

st.markdown("- #### [Damage identification in FMLs](https://doi.org/10.1016/j.cma.2022.115737)")
st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This research work focuses on damage identification in FML "
            "with guided ultrasonic waves (GUW) through an inverse approach based on the Bayesian paradigm. This part "
            "of our research work enjoys the parametric model order reduction that was developed earlier. a Markov "
            "Chain Monte-Carlo based Metropolis–Hastings algorithm and an Ensemble Kalman filtering technique are "
            "deployed to identify the damage. It is found that both methods are successful in multivariate "
            "characterization of the damage with a high accuracy and were also able to quantify their associated "
            "uncertainties.")

