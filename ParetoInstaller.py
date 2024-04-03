import streamlit as st
import base64

# Create a dictionary of business names and their corresponding options
business_options_dict = {
    "LavalTool": {
        "Workstation Plant 1": "[1](https://api.paretosupport.com/clients/d8e47500-b39c-4e1f-b62b-d265f0af13ef/deploy/)",
        "Workstation Plant 2": "[1](https://api.paretosupport.com/clients/f3c7d97a-d198-49a7-9138-57de0921dd96/deploy/)",
        "Server": "[2](https://api.paretosupport.com/clients/42fcf95e-37b3-40ae-81b4-8d75fbcae718/deploy/)"
    },
    "Business B": {
        "Workstation": "[3](https://example.com/businessB_workstation.exe)",
        "Server": "[4](https://example.com/businessB_server.exe)"
    },
    # Add more business names and options as needed
}

# Display the first dropdown menu for selecting a business
selected_business = st.selectbox("Select a business", list(business_options_dict.keys()))

# Display the second dropdown menu for selecting workstation or server
selected_option = st.selectbox("Select an option", list(business_options_dict[selected_business].keys()))

# Define a function to create the download link
def create_download_link(url, filename):
    with st.spinner("Generating download link..."):
        # You can modify this part based on your file format (e.g., .exe)
        href = f'<a href="{url}" download="{filename}"><button>Click here to download</button></a>'
        return href

# Get the selected URL based on the chosen business and option
selected_url = business_options_dict.get(selected_business, {}).get(selected_option, "")

# Display the download button
if selected_url:
    st.markdown(create_download_link(selected_url, f"{selected_business}_{selected_option}.exe"), unsafe_allow_html=True)
else:
    st.warning("Please select a business and an option from the dropdowns.")
