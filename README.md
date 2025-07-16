# Information Retrieval System 🚀

An AI-powered information retrieval system that allows users to upload PDF documents and ask questions about their content using Google's Gemini AI model. The system uses LangChain for document processing and FAISS for vector storage to provide accurate, context-aware responses.

## Features

- **PDF Document Upload**: Support for multiple PDF files
- **AI-Powered Q&A**: Ask questions about uploaded documents using Google Gemini AI
- **Vector Search**: Efficient document retrieval using FAISS vector database
- **Clean Interface**: Simple and intuitive Streamlit web interface
- **Real-time Processing**: Instant responses to user queries
- **Context-Aware**: Maintains conversation context for better responses

## Technology Stack

- **Python 3.8+**
- **Streamlit** - Web interface
- **LangChain** - Document processing and AI orchestration
- **Google Generative AI (Gemini)** - Language model for responses
- **FAISS** - Vector database for similarity search
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hm7mihiranga/Information_Retreval_System.git
   cd Information_Retreval_System
   ```

2. **Create a virtual environment**
   ```bash
   conda create -n genai python=3.8
   conda activate genai
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   
   To get a Google API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your `.env` file

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Upload PDF documents**
   - Use the sidebar to upload one or more PDF files
   - Click "Submit and Process" to process the documents

3. **Ask questions**
   - Type your question in the text input field
   - Get AI-powered answers based on your uploaded documents

## Project Structure

```
Information_Retreval_System/
├── app.py                          # Main Streamlit application
├── src/
│   ├── __init__.py
│   └── helper.py                   # Core functionality and AI integration
├── requirements.txt                # Python dependencies
├── setup.py                       # Package setup configuration
├── .env                           # Environment variables (not in repo)
├── README.md                      # Project documentation
└── research/
    └── trials.ipynb               # Research and experimentation notebook
```

## Core Components

### `app.py`
- Streamlit web interface
- File upload handling
- User interaction management

### `src/helper.py`
- PDF text extraction
- Text chunking and preprocessing
- Vector store creation using FAISS
- Conversational AI chain setup with Google Gemini

## API Configuration

The system uses Google's Generative AI models:
- **Embeddings**: `models/embedding-001`
- **Chat Model**: `gemini-1.5-flash`

## Requirements

See `requirements.txt` for the complete list of dependencies:
- python-dotenv
- google-generativeai
- langchain
- langchain-google-genai
- PyPDF2
- faiss-cpu
- streamlit
- langchain-community

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Hasitha Mihiranga**
- Email: hm.mihi7@gmail.com
- GitHub: [@hm7mihiranga](https://github.com/hm7mihiranga)

## Acknowledgments

- Google AI for providing the Gemini language model
- LangChain community for the excellent framework
- Streamlit for the web interface framework

---

*Built with ❤️ using Python and AI*