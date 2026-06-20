import streamlit as st

st.set_page_config(
    page_title="Digital Twin of Climate-Vulnerable Islands",
    page_icon="🌍",
    layout="wide"
)

# HERO SECTION

st.title("🌍 Digital Twin of Climate-Vulnerable Island Systems")

st.markdown("""
### *Can We Predict the Future of an Island Before It Disappears?*

An integrated geospatial, environmental, ecological and socio-economic
digital twin framework for climate-vulnerable island systems.
""")

st.markdown("---")

# PROJECT OVERVIEW

st.header("📖 Project Overview")

st.write("""
This project develops a comprehensive **Digital Twin Framework**
for island systems threatened by climate change.

Unlike conventional studies that focus on individual factors such as
flooding or sea-level rise, this framework integrates environmental,
ecological, economic and social processes into a unified modelling system.

The objective is to simulate future island conditions under multiple
climate scenarios and support resilience planning before real-world
damage occurs.
""")

# STUDY AREAS

st.markdown("---")

st.header("🏝️ Study Areas")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🇲🇻 Maldives")

with col2:
    st.info("🇮🇳 Lakshadweep")

with col3:
    st.info("🇸🇨 Seychelles")

col4, col5 = st.columns(2)

with col4:
    st.info("🇫🇯 Fiji")

with col5:
    st.info("🇪🇸 Canary Islands")

# RESEARCH QUESTION

st.markdown("---")

st.header("🔬 Research Question")

st.warning("""
How will sea-level rise, coastal erosion, coral reef degradation,
tourism fluctuations and population migration collectively reshape
the sustainability and resilience of island systems by 2050?
""")

# SYSTEM COMPONENTS

st.markdown("---")

st.header("⚙️ Integrated System Components")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌊 Environmental System")

    st.write("""
    • Sea Level Rise

    • Coastal Erosion

    • Elevation (DEM)

    • Cyclones & Storm Surges

    • Flood Risk
    """)

    st.subheader("🌿 Ecological System")

    st.write("""
    • Coral Reefs

    • Mangroves

    • Biodiversity Hotspots

    • Ecosystem Vulnerability

    • Habitat Loss
    """)

with col2:

    st.subheader("🏘️ Socio-Economic System")

    st.write("""
    • Population Density

    • Settlements

    • Tourism Infrastructure

    • Fisheries Production

    • Employment Dynamics
    """)

    st.subheader("🏗️ Infrastructure System")

    st.write("""
    • Airports

    • Ports

    • Hospitals

    • Roads

    • Critical Facilities
    """)
    st.markdown("---")

st.header("🎯 Project Objectives")

st.markdown("""

1. Develop a Digital Twin Framework for climate-vulnerable island systems.

2. Assess future environmental and socio-economic impacts under climate change.

3. Simulate interactions between ecological, economic and human systems.

4. Identify vulnerability hotspots and resilience pathways.

5. Support adaptation planning and climate-risk assessment.

6. Create a transferable framework applicable to island regions worldwide.
   """)

st.markdown("---")

st.header("🏗️ Digital Twin Architecture")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🌊 Environmental Layer")

with col2:
    st.info("🌿 Ecological Layer")

with col3:
    st.info("🏘️ Socio-Economic Layer")

st.info("🧠 Integrated Climate Simulation Engine")

st.info("📊 Decision Support & Resilience Assessment Framework")

st.markdown("---")

st.header("📊 Expected Research Outputs")

st.markdown("""
• Island Vulnerability Atlas

• Sea Level Rise Risk Maps

• Population Exposure Maps

• Tourism Vulnerability Assessment

• Infrastructure Risk Assessment

• Coral Reef Health Assessment

• Mangrove Protection Assessment

• Climate Resilience Mapping

• Comparative Island Ranking System

• Interactive Digital Twin Dashboard
""")
st.markdown("---")

st.header("🌎 Study Region Coverage")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🇲🇻 Maldives", "20 Atolls")

with col2:
    st.metric("🇮🇳 Lakshadweep", "36 Islands")

with col3:
    st.metric("🇸🇨 Seychelles", "115 Islands")

with col4:
    st.metric("🇫🇯 Fiji", "330+ Islands")

with col5:
    st.metric("🇪🇸 Canary Islands", "8 Islands")
# FOOTER

st.markdown("---")

st.markdown("""
### 🌎 Digital Twin of a Drowning Island

**Author:** Sakshi Maske

**Tools:** QGIS • Python • Remote Sensing • Geospatial Analysis • Streamlit

*"Predicting Island Futures Before They Disappear."*
""")
