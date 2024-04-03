import streamlit as st

# Define a dictionary of business names and their corresponding webpages
business_websites = {
    "Business A": {
        "workstation": "https://google.com",
        "server": "https://www.google.com"
    },
    "Business B": {
        "workstation": "https://www.google.com",
        "server": "https://www.google.com"
    },
    "Business C": {
        "workstation": "https://www.google.com",
        "server": "https://www.google.com"
    }
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
    selected_url = business_websites[selected_business][selected_option]
    st.write(f"Opening {selected_business} {selected_option} webpage: {selected_url}", unsafe_allow_html=True)
