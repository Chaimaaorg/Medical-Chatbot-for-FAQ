# Medical Chatbot: Mental Health FAQ System Based on Google PaLM LLM and LangChain  

This is an end-to-end LLM project based on **Google Generative AI** and **LangChain**. We are building a **Q&A system** for a **Mental Health FAQ Chatbot** using a dataset from Kaggle. The dataset contains frequently asked questions related to mental health, and this system will provide a **Streamlit-based user interface** where users can ask questions and get accurate, context-aware answers.

## Project Highlights

- Utilizes the **Mental Health FAQ dataset** from Kaggle: [Mental Health FAQ Dataset](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot).
- Builds an LLM-based question-and-answer system to provide instant responses to mental health-related queries.
- Reduces the need for manual intervention by automating responses to common questions.
- Provides a user-friendly interface for seamless interaction.

## You Will Learn
- **LangChain + Google Generative AI**: Building an LLM-based Q&A system.
- **Streamlit**: Creating a simple and interactive UI.
- **Hugging Face Instructor Embeddings**: Generating text embeddings for semantic search.
- **FAISS**: Efficiently storing and retrieving embeddings using a vector database.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Chaimaaorg/Medical-Chatbot-for-FAQ
   ```

2. Navigate to the project directory:
   ```bash
   cd medical-chatbot
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Acquire an API key from [makersuite.google.com](https://makersuite.google.com/) and add it to the `.env` file:
   ```bash
   GOOGLE_API_KEY="your_api_key_here"
   ```

5. Download the **Mental Health FAQ dataset** from Kaggle and place it in the main directory.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. The web app will open in your browser.

   - To create a knowledge base of FAQs, click on the **Create Knowledge Base** button. This process may take some time, so please wait.
   - Once the knowledge base is created, a directory called `faiss_index` will be generated in your project folder.
   - You can now ask questions. Type your question in the input box and press **Enter**.

## Sample Questions
- What are the symptoms of depression?
- How can I manage anxiety?
- Is therapy effective for mental health issues?
- What should I do if I feel overwhelmed?
- Are there any self-care tips for mental well-being?

## Project Structure

- `main.py`: The main Streamlit application script.
- `langchain_helper.py`: Contains all the LangChain code for Q&A processing.
- `requirements.txt`: Lists the required Python packages for the project.
- `.env`: Configuration file for storing your Google API key.

