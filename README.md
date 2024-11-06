# ResearchAgent
Research using Swarm Agents

## Overview

ResearchAgent is a simple template tool designed to facilitate research using Swarm Agents. It leverages advanced Groq and Local LLMs to search the web, analyze findings, and generate comprehensive articles based on the gathered information.

## Features

- **Web Search Integration:** Fetches the latest news and articles based on user queries.
- **AI-Powered Analysis:** Automatically deduplicates and synthesizes research findings.
- **Article Generation:** Transforms analyzed data into polished, publication-ready articles.
- **Streamlit Interface:** Provides an interactive web interface for easy use.

## Installation

### Prerequisites

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/)
- [Microagent](https://github.com/microagent/microagent) i.e OpenAI Swarm
- Other dependencies listed in `requirements.txt`

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ResearchAgent.git
   cd ResearchAgent
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.
   - Add necessary environment variables as required.

## Usage

1. **Run the Application**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the Interface**
   - Enter your research query in the text input field.
   - Click on "Generate Article" to fetch, analyze, and generate a comprehensive article based on your query.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).