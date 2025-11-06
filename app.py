import streamlit as st
import pandas as pd

st.title("📖 Church Member Directory")

# Initialize the data if it's not already stored
if "members" not in st.session_state:
    st.session_state["members"] = pd.DataFrame(columns=["Name", "Email", "Phone", "Ministry"])

# Add new members
with st.form("add_member"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    ministry = st.text_input("Ministry / Department")
    submitted = st.form_submit_button("Add Member")

    if submitted and name:
        new_member = pd.DataFrame([[name, email, phone, ministry]], columns=st.session_state["members"].columns)
        st.session_state["members"] = pd.concat([st.session_state["members"], new_member], ignore_index=True)
        st.success(f"✅ Added {name} to the directory!")

# Display the directory
st.subheader("Church Members")
st.dataframe(st.session_state["members"])
