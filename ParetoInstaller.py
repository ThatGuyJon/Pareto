import streamlit as st
import webbrowser

# Define a dictionary of business names and their corresponding webpages
business_websites = {
    "Business A": {
        "workstation": "https://www.businessa-workstation.com",
        "server": "https://www.businessa-server.com"
    },
    "Business B": {
        "workstation": "https://www.businessb-workstation.com",
        "server": "https://www.businessb-server.com"
    },
    "Business C": {
        "workstation": "https://www.businessc-workstation.com",
        "server": "https://www.businessc-server.com"
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

# Link button to open the selected webpage
st.link_button("Go to gallery", "https://streamlit.io/gallery")
