# Testify_Granite
AI-Powered Testing Estimation and Automation Tool
About the Project
This project leverages cutting-edge AI models to revolutionize the software testing process. By integrating IBM Watson AI, Granite IBM's 34B-Code Instructor, and Hugging Face models with testing tools like Selenium, the tool estimates testing efforts (both manual and automated) and conducts various types of testing, including regression, sanity, smoke, and critical features. The tool also generates detailed test reports, providing valuable insights for Test Engineers, SDETs, Testing Managers, Developers, and Business Analysts.

Project Steps
Data Collection & Preprocessing

Collect relevant data from the website, web app, or mobile app provided by the user.
Preprocess the data to ensure it is ready for analysis and testing.
AI Model Integration

Integrate IBM Watson AI and Hugging Face models to analyze the application.
Use Granite IBM's 34B-Code Instructor model to guide and enhance the testing process, ensuring accuracy and thorough coverage.
These models work together to estimate the required testing efforts, both manual and automated.
Testing Types Implementation

Implement various types of testing, including:
Manual Testing: Manually assess critical features to ensure they function as expected.
Automated Testing: Utilize Selenium and AI guidance to automate testing tasks.
Regression Testing: Confirm that recent changes do not negatively impact existing functionalities.
Sanity Testing: Perform quick checks on basic functionalities to ensure stability.
Smoke Testing: Validate the overall stability of the application.
Critical Features Testing: Focus on the most crucial aspects of the application.
Test Report Generation

Generate comprehensive test reports that include test statuses, coverage, identified issues, and recommendations for improvement.
The reports are designed to be easily understood and actionable.
Deployment

Deploy the project on IBM Watson and Granite, hosting it using Streamlit for easy access and interaction.
How to Use It
Follow these steps to set up and use the AI-Powered Testing Estimation and Automation Tool:

1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/ai-testing-estimation.git
cd ai-testing-estimation
2. Install Dependencies
Ensure you have Python installed, then install the required packages:

bash
Copy code
pip install -r requirements.txt
3. Set Up API Keys for IBM Watson, Granite, and Hugging Face
Configure your environment with the necessary API keys:

Create a .env file in the root directory.
Add the following lines with your credentials:
bash
Copy code
WATSON_API_KEY=your_watson_api_key
WATSON_URL=your_watson_url
HF_API_KEY=your_huggingface_api_key
GRANITE_API_KEY=your_granite_api_key
GRANITE_MODEL=34b-code-instructor
4. Run the Application
Start the Streamlit application:

bash
Copy code
streamlit run app.py
5. Input the URL of the Application to Test
Once the application is running, input the URL of the website, web app, or mobile app you wish to test.
6. Select Testing Options
Choose the type of testing you want to conduct (manual, automated, regression, etc.).
The tool will perform the selected tests, guided by Granite IBM's 34B-Code Instructor, and provide real-time updates.
7. View and Analyze Test Reports
After the testing process is completed, detailed test reports will be generated.
Download and review these reports to identify issues and areas for improvement.
Contributing
We welcome contributions from the community. If you would like to contribute, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.

