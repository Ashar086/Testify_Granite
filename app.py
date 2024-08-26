import streamlit as st
from estimation import estimate_testing_resources
from automation import generate_automation_scripts
from critical_functionality import test_critical_functionality
from regression_testing import run_regression_tests
from test_report import generate_test_report
from sanity_check import perform_sanity_check
from performance_testing import perform_performance_test
def main():
    st.title("Testify - Automated Testing Tool")

    url = st.text_input("Enter the URL to be tested")
    
    if st.button("Estimate Testing Resources"):
        st.write(estimate_testing_resources(url))
    
    if st.button("Generate Automation Test Scripts"):
        st.write(generate_automation_scripts(url))
    
    if st.button("Test Critical Functionalities"):
        st.write(test_critical_functionality(url))
    
    if st.button("Run Regression Tests"):
        st.write(run_regression_tests(url))
    
    if st.button("Generate Test Report"):
        st.write(generate_test_report(url))
    
    if st.button("Perform Sanity Check"):
        st.write(perform_sanity_check(url))
    
    if st.button("Perform Performance Test"):
        st.write(perform_performance_test(url))

if __name__ == "__main__":
    main()
