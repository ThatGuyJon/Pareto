import streamlit as st

# Define a dictionary of business names and their corresponding webpages
business_websites = {
    "Laval Tool": {
        "workstation": "https://api.paretosupport.com/clients/d8e47500-b39c-4e1f-b62b-d265f0af13ef/deploy/",
        "server": "https://api.paretosupport.com/clients/42fcf95e-37b3-40ae-81b4-8d75fbcae718/deploy/"
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
