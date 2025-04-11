import streamlit as st

# Title
st.title("Elongation Test Checker")

# Material selection
material = st.selectbox("Select Material", ["Steel", "Aluminum", "Copper"])

# User inputs
actual_length = st.number_input("Enter Actual Length (mm)", min_value=0.0, format="%.2f")
elongation_percent = st.number_input("Enter Elongation (%)", min_value=0.0, format="%.2f")

# Run calculation when button is clicked
if st.button("Check Result"):
    elongation = (elongation_percent / 100) * actual_length
    st.write(f"Elongation (mm): **{elongation:.2f} mm**")

    # Add your logic here based on material
    if material == "Steel":
        if elongation_percent >= 10:
            st.success("Steel passed the elongation test.")
        else:
            st.error("Steel failed the elongation test.")
    elif material == "Aluminum":
        if elongation_percent >= 12:
            st.success("Aluminum passed the elongation test.")
        else:
            st.error("Aluminum failed the elongation test.")
    elif material == "Copper":
        if elongation_percent >= 15:
            st.success("Copper passed the elongation test.")
        else:
            st.error("Copper failed the elongation test.")