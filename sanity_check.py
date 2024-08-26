import streamlit as st

def perform_sanity_check(url):
    st.write(f"Performing sanity check for {url}...")
    # Python code for sanity check
    st.code("""
    import requests

    def sanity_check(url):
        response = requests.get(url)
        if response.status_code == 200:
            print("Sanity check passed")
        else:
            print("Sanity check failed")
    """, language='python')
