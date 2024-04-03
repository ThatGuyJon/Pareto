import streamlit as st
import base64

# Create a dictionary of business names and their corresponding options
business_options_dict = {
    "Business A": {
        "Workstation": "1",
        "Server": "2"
    },
    "Business B": {
        "Workstation": "3",
        "Server": "4"
    },
    # Add more business names and options as needed
}

# Display the first dropdown menu for selecting a business
selected_business = st.selectbox("Select a business", list(business_options_dict.keys()))

# Display the second dropdown menu for selecting workstation or server
selected_option = st.selectbox("Select an option", list(business_options_dict[selected_business].keys()))

# Define a function to create the styled download button
def create_styled_button(url, filename):
    with st.spinner("Generating download link..."):
        # You can customize the button style using CSS
        button_style = """
            <style>
                .download-button {
                    background-color: #f7f7f7;
                    border: none;
                    color: black;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    border-radius: 5px;
                }
            </style>
        """
        href = f'<a href="{url}" download="{filename}" class="download-button">Download {filename}</a>'
        return button_style + href

# Get the selected URL based on the chosen business and option
selected_url = business_options_dict.get(selected_business, {}).get(selected_option, "")

# Display the styled download button
if selected_url:
    st.markdown(create_styled_button(selected_url, f"{selected_business}_{selected_option}.exe"), unsafe_allow_html=True)
else:
    st.warning("Please select a business and an option from the dropdowns.")
