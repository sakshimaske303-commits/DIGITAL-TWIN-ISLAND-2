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

# PROJECT WORKFLOW

st.markdown("---")

st.header("🧩 Project Workflow")

st.success("Phase 1 : Spatial Database Development")

st.success("Phase 2 : Environmental System Development")

st.success("Phase 3 : Socio-Economic System Development")

st.success("Phase 4 : Integrated Database Development")

st.success("Phase 5 : Climate Simulation Modelling")

st.success("Phase 6 : Digital Twin Development")

st.success("Phase 7 : Interactive Dashboard Development")

st.success("Phase 8 : Research Outputs & Policy Framework")

# OUTPUTS

st.markdown("---")

st.header("📊 Expected Outputs")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Study Regions", "5")

with col2:
    st.metric("Climate Scenarios", "3")

with col3:
    st.metric("Integrated Systems", "4")

st.write("""
✅ Island Vulnerability Atlas

✅ Flood Risk Assessment

✅ Infrastructure Exposure Analysis

✅ Tourism Vulnerability Assessment

✅ Population Exposure Mapping

✅ Resilience Score Framework

✅ Climate Adaptation Recommendations

✅ Interactive Digital Twin Dashboard
""")

# CURRENT STATUS

st.markdown("---")

st.header("🚀 Current Development Status")

st.write("✅ Island Boundary Database")

st.write("✅ Coral Reef Mapping")

st.write("✅ Mangrove Mapping")

st.write("✅ Tourism Infrastructure Mapping")

st.write("✅ Environmental Layer Compilation")

st.write("🔄 Climate Simulation Engine")

st.write("🔄 Interactive Dashboard Expansion")

st.write("🔄 Comparative Resilience Framework")

# FOOTER

st.markdown("---")

st.markdown("""
### 🌎 Digital Twin of a Drowning Island

**Author:** Sakshi Maske

**Tools:** QGIS • Python • Remote Sensing • Geospatial Analysis • Streamlit

*"Predicting Island Futures Before They Disappear."*
""")
