import streamlit as st

# Create a dictionary of business names and their corresponding URLs
business_options_dict = {
    "Business A": {
        "Workstation": "https://example.com/businessA_workstation",
        "Server": "https://example.com/businessA_server"
    },
    "Business B": {
        "Workstation": "https://example.com/businessB_workstation",
        "Server": "https://example.com/businessB_server"
    },
    # Add more business names and URLs as needed
}

# Display the first dropdown menu for selecting a business
selected_business = st.selectbox("Select a business", list(business_options_dict.keys()))

# Display the second dropdown menu for selecting workstation or server
selected_option = st.selectbox("Select an option", ["Workstation", "Server"])

# Get the selected URL based on the chosen business and option
selected_url = business_options_dict.get(selected_business, {}).get(selected_option, "")

# Display the link to the selected webpage
if selected_url:
    st.markdown(f"Visit the {selected_option} page for {selected_business}: {selected_option} Webpage")
else:
    st.warning("Please select a business and an option from the dropdowns.")
