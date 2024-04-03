import streamlit as st

# Define a dictionary of business names and their corresponding webpages
business_websites = {
    "Business A": {
        "workstation": "https://google.com",
        "server": "Business A Server"
    },
    "Business B": {
        "workstation": "Business B Workstation",
        "server": "Business B Server"
    },
    "Business C": {
        "workstation": "Business C Workstation",
        "server": "Business C Server"
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
selected_url = business_websites[selected_business][options[selected_option]]
st.link_button(f"Open {selected_business} {selected_option} webpage", selected_url)
