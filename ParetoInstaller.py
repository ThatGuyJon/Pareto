import streamlit as st

# Define a dictionary of business names and their corresponding webpages
business_websites = {
    "Business A": {
        "workstation": "[Business A Workstation](https://www.businessa-workstation.com)",
        "server": "[Business A Server](https://www.businessa-server.com)"
    },
    "Business B": {
        "workstation": "[Business B Workstation](https://www.businessb-workstation.com)",
        "server": "[Business B Server](https://www.businessb-server.com)"
    },
    "Business C": {
        "workstation": "[Business C Workstation](https://www.businessc-workstation.com)",
        "server": "[Business C Server](https://www.businessc-server.com)"
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
if st.link_button("Open Webpage"):
    selected_url = business_websites[selected_business][selected_option]
