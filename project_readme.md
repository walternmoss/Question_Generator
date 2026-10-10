# ISU AI Assessment & Tagged Question Bank Generator

An intelligent, batch-capable web application built with **Streamlit** and the **Google GenAI SDK** (`google-genai`) that converts lecture slides (PDF/PPTX) and study guides into rigorously level-matched, difficulty-tagged question banks. 

Designed specifically for educators and researchers to quickly generate assessments or structured question banks for AI Socratic tutors and course management systems.

---

## Key Features

- **Batch Processing Queue**: Upload multiple source documents (PDF, PPTX, TXT, MD) simultaneously and download a packaged `.zip` archive of individual assessment files.
- **Granular Difficulty Distribution**: Precisely configure the number of *Easy*, *Medium*, and *Hard* questions per document.
- **Automatic Academic Level Matching**: Automatically analyzes source text to match the technical rigor and cognitive depth of the input material (e.g., matching upper-level undergraduate or graduate coursework).
- **Flexible Question Formats**: Choose from Short Answer, Multiple Choice (with customizable answer count), True/False, and Fill-in-the-Blank.
- **Structured Outputs**: Export as **Markdown with Metadata Tags** (optimized for custom AI Socratic tutor parsers), **Structured XML**, or **Plain Text**.
- **Answer Key Inclusion**: Option to automatically generate comprehensive answer keys.

---

## Project Structure

```text
isu-exam-generator/
├── app.py              # Streamlit interactive web interface
├── generator.py        # Gemini API prompt engine and document parser
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Prerequisites & Local Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/isu-exam-generator.git
   cd isu-exam-generator
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.9+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your Gemini API Key**:
   Get an API key from Google AI Studio and set it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

---

## Deploying to Streamlit Community Cloud

To share this tool securely across departments at Iowa State University:

1. Push your repository to GitHub.
2. Log in to [Streamlit Community Cloud](https://streamlit.io/cloud) and click **New app**.
3. Select your repository, branch (`main`), and main file path (`app.py`).
4. Under **App settings > Secrets**, add your Gemini API key so users don't have to enter their own:
   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```
5. Deploy!

---

## License

Distributed under the MIT License. See `LICENSE` for more information.