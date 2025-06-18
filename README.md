# 📝 AI Blog Generation App using Hugging Face & Gemini

This project demonstrates blog generation using two powerful Large Language Models (LLMs):
- 🤗 **Hugging Face Transformers** (cached model loading)
- 🔮 **Google Gemini API** (real-time, fast predictions)

---

## 🚀 Key Highlights

- ✍️ **Generates blogs** based on user input topic, desired word count, and writing style
- 🧠 **Uses two LLMs**: 
  - Hugging Face model (local transformer-based)
  - Google Gemini (cloud-based, via API)
- ⏳ **Performance Comparison**:
  - **Hugging Face**: Initially takes **1–2 minutes** to load the model and generate the first output. Once cached, it's faster.
  - **Gemini**: Delivers output in **3–4 seconds** using the `gemini-1.5-flash` or `gemini-2.5-pro` model through API calls.

---

## 🧰 Technologies Used

- Python
- Streamlit (UI)
- Hugging Face Transformers (`text-generation` models)
- Google Generative AI (`gemini-1.5-flash` / `gemini-2.5-pro`)
- Langchain for LLM integration

---

## 🖥️ How to Run Locally

### ✅ Prerequisites

- Python 3.9+
- Hugging Face API Token (for private models, if used)
- Google Gemini API Key

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/blog-generation-app.git
cd blog-generation-app

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

```
🔑 Set Up API Keys
Method 1: Using .env File
Create a .env file in the root directory and add:
GOOGLE_API_KEY=your_google_gemini_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

If you're using .env, install python-dotenv:
pip install python-dotenv

Method 2: Using Environment Variables (Terminal)
# For Linux/macOS
export GOOGLE_API_KEY=your_google_gemini_api_key
export HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
:: For Windows CMD
set GOOGLE_API_KEY=your_google_gemini_api_key
set HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

▶️ Run the App
For Gemini version (faster):
streamlit run app_gemini.py

For Hugging Face version:
streamlit run app.py

Open browser at: http://localhost:8501



