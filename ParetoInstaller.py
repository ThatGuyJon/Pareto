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

# Define a function to create the styled download button
def create_styled_button(url):
    with st.spinner("Generating download link..."):
        # You can customize the button style using CSS
        button_style = """
            <style>
                .open-button {
                    background-color: #f0f2f6;
                    border: none;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    border-radius: 5px;
                }
            </style>
        """
        href = f'<a href="{url}" target="_blank" class="open-button">Open {business_name}</a>'
        return button_style + href

# Get the selected URL based on the chosen business and option
selected_url = business_options_dict.get(selected_business, {}).get(selected_option, "")

# Display the link to the selected webpage
if selected_url:
    st.markdown(create_styled_button(selected_url,f"Open page"))
else:
    st.warning("Please select a business and an option from the dropdowns.")
