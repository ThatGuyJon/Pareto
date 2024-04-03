import streamlit as st

# Define a dictionary of business names and their corresponding webpages
business_websites = {
    "Business A": "[Business A Website](https://www.businessa.com)",
    "Business B": "[Business B Website](https://www.businessb.com)",
    "Business C": "[Business C Website](https://www.businessc.com)"
}

# Define a dictionary of workstation and server options
options = {
    "Workstation": "workstation",
    "Server": "server"
}

# Create a Streamlit app
st.title("Business Webpage Selector")

# Dropdown for selecting a business name
selected_business = st.selectbox("Select a business name:", list(business_websites.keys()))

# Dropdown for selecting workstation or server
selected_option = st.selectbox("Select workstation or server:", list(options.keys()))

# Button to open the selected webpage
if st.button("Open Webpage"):
    if selected_option == "workstation":
        st.write(f"Opening {selected_business} workstation webpage: {business_websites[selected_business]}")
    elif selected_option == "server":
        st.write(f"Opening {selected_business} server webpage: {business_websites[selected_business]}")
