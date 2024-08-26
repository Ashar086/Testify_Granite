import streamlit as st
import requests

# Step 1: Exchange API Key for Access Token
apikey = "6NV9V90_cdLLarB6FhcN5lQh2JVYf50mUfQ8C4KHNby3"  # Replace with your new IBM Cloud API key
auth_url = "https://iam.cloud.ibm.com/identity/token"

auth_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

auth_data = {
    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
    "apikey": apikey
}

auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)

if auth_response.status_code == 200:
    access_token = auth_response.json()["access_token"]
else:
    st.error(f"Failed to retrieve access token: {auth_response.text}")
    st.stop()

# Title of the Streamlit app
st.title("IBM Watson Software Testing Engineer")

# User input for the text generation prompt
user_input = st.text_area("Enter a Correct URL:", value="")

# IBM Watson API request parameters
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
body = {
    "input": f"""<|system|>{user_input}<|assistant|>""",
    "parameters": {
        "decoding_method": "sample",
        "max_new_tokens": 900,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1,
        "repetition_penalty": 1.05
    },
    "model_id": "ibm/granite-13b-chat-v2",
    "project_id": "e0a23064-936a-4f9e-86ee-4d74cc61270d"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Step 2: Generate text using IBM Watson when the button is clicked
if st.button("Generate Response"):
    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        data = response.json()

        # Accessing the 'generated_text' from the first result in 'results'
        if 'results' in data and len(data['results']) > 0:
            generated_text = data['results'][0]['generated_text']
            st.write("**IBM Watson Output:**")
            st.write(generated_text)
        else:
            st.error("No results found in the response.")
    else:
        st.error(f"Error {response.status_code}: {response.text}")
