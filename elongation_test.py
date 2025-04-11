import streamlit as st

def get_required_elongation(material, diameter):
    material = material.lower()
    if material == "aluminium 1350":
        if 1.5 < diameter <= 2.5:
            return 0.8
        elif 2.5 < diameter <= 3.25:
            return 1.0
        elif 3.25 < diameter <= 4.0:
            return 1.2
        elif 4.0 < diameter <= 4.75:
            return 1.4
    elif material == "alloy 1120":
        if 1.5 < diameter <= 4.75:
            return 3.0
    elif material == "alloy 6201a":
        if 1.5 < diameter <= 2.5:
            return 0.8
        elif 2.5 < diameter <= 3.25:
            return 1.0
        elif 3.25 < diameter <= 4.0:
            return 1.2
        elif 4.0 < diameter <= 4.75:
            return 1.4
    raise ValueError("Invalid material or unsupported diameter.")

# Streamlit UI
st.title("Elongation Test Checker")

material = st.selectbox("Select Material", ["Aluminium 1350", "Alloy 1120", "Alloy 6201A"])
diameter = st.number_input("Enter Wire Diameter (mm)", min_value=1.0, max_value=5.0, step=0.01)
final_length = st.number_input("Enter Final Length after Elongation (mm)", min_value=0.0, step=0.1)

if st.button("Check Result"):
    try:
        original_length = 250
        required = get_required_elongation(material, diameter)
        actual = ((final_length - original_length) / original_length) * 100
        result = "PASS" if actual >= required else "FAIL"
        st.success(f"Required Elongation: {required}%")
        st.info(f"Measured Elongation: {round(actual, 2)}%")
        st.write(f"**Result: {result}**")
    except Exception as e:
        st.error(str(e))