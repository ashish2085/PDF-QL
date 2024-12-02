# PDF Query Language 🧙🏻‍♀️

This is a Streamlit-based web application that allows users to query information from uploaded PDF files using Google Gemini AI. The app uses Natural Language Processing (NLP) to extract relevant data and answer user queries.

---

## 🚀 Features

- Upload and process multiple PDFs.
- Ask questions based on the uploaded documents.
- Google Gemini AI-powered responses.
- Maintain chat history for continuous interaction.
- Set up your API key via the UI.

---

## 🛠️ Setup Instructions

### Prerequisites

1. **Python**: Ensure you have Python 3.9+ installed.
2. **Google Gemini API Key**: Obtain an API key from [Google AI Developer Console](https://ai.google.dev/gemini-api/docs/api-key).
3. **Git**: Installed to clone the repository.

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-query-language.git
cd pdf-query-language
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment:

On Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
Install the required Python packages:

```bash

pip install -r requirements.txt
```
### 4. Set Up Your API Key
You can set the API key in two ways:

Through Environment Variables:

Export your API key as an environment variable:
```bash

export API_KEY="your_google_gemini_api_key"
```
### Through the UI:

Start the app and input your API key in the sidebar.
🚦 Running the Application Locally
Run the Streamlit app with:

```bash

streamlit run app.py
```
This will start the application locally, and you can access it in your browser at http://localhost:8501.

### 🧪 Testing the Application
Upload PDFs:

Drag and drop your PDF files into the sidebar.
Process PDFs:

Click the "Process" button to prepare the documents for querying.
Ask Questions:

Enter a question in the text box, and the app will respond based on the content of the PDFs.
View Chat History:

Interact with the app continuously, and your previous questions and answers will be displayed under "Chat History."
🐳 Docker Setup (Optional)
You can run this application in a Docker container.

Build the Docker Image:

```bash

docker build -t pdf-query-language .
```
Run the Docker Container:

```bash

docker run -p 8501:8501 pdf-query-language
```
Access the app at http://localhost:8501.

📂 Project Structure
```plaintext

.
├── app.py                 # Main Streamlit application
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── images/                # Static images for the app
```
📝 Notes
Google Gemini API Key:

Obtain the API key from the Google AI Developer Console.
Ensure the API key has the necessary permissions to use Gemini services.
Dependencies:

The app uses the langchain, google.generativeai, PyPDF2, and streamlit packages.
🙌 Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

💡 Acknowledgements
Built with ❤️ by Ashish Kumar.
Powered by Google Gemini AI.
Inspired by the need to make document querying seamless.
csharp
Copy code

### Steps to Publish:
- Save this as `README.md` in the root directory of your project.
- Push it to your GitHub repository with the following commands:
  ```bash
  git add README.md
  git commit -m "Add README.md"
  git push origin main
  ```



