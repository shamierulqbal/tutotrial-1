import streamlit as st
import os 

#Profile
col1, col2 = st.columns([1, 3])

with col1:
    # Use local image (must be in same folder as app.py)
    if os.path.exists("profile.png"):
        st.image("profile.png", caption="YUSRI BIN RAZALI", width=180)
    else:
        st.warning("profile.jpg not found. Please place it in the same folder as this app.")


st.title("MUHAMMAD SHAMIERUL IQBAL BIN MOHD SHAMSUDDIN")
st.header("Contact Information")
st.write("Email: SHAMIERULQBAL@GMAIL.COM")
st.write("Phone: 010-278-5963")
st.write("LinkedIn: linkedin.com/in/yourprofile")

st.header("Education")
st.write("Bachelor of Information Technology (Hons), University Malaysia Kelantan, Year 4")

st.header("Work Experience")
st.write("Salesman, 7 Eleven Company, 2019")
  

st.header("Skills")
st.write("- AI Specialist")
st.write("- Machine learning Development")
st.write("- UIUX Development")

st.header("Projects")
st.write("DIETLAH: FOR NUTRITION AND CALORIES TRACKING ")
st.write("-This Project focus for healty life and help people for reduce weight")
