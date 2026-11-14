# WealthWise RAG Assistant

An internal knowledge assistant foundation for a retail bank's wealth division.

## Project Structure

* data/: Local documents used by the RAG application.
* src/: Application source code.
* prompts/: AI system prompts and templates.
* outputs/: Generated outputs and results.

## Prerequisites

* Python 3.13+
* Git

## Setup Instructions

### 1\. Clone the repository

git clone https://github.com/anushkapoonia07/S47-0110-wealthwise-rag-assistant.git

cd S47-0110-wealthwise-rag-assistant

### 2\. Create a virtual environment

python -m venv .venv

### 3\. Activate the environment (Windows)

.venv\\Scripts\\activate

### 4\. Install dependencies

python -m pip install -r requirements.txt

### 5\. Configure environment variables

Copy-Item .env.example .env

Add your own API configuration to the local .env file.

Never commit your real .env file or API key.

### 6\. Verify the installation

python -c "import openai, chromadb, dotenv; print('Environment setup successful!')"

## Clean Setup Verification



Verified successfully in a fresh virtual environment

using Python 3.13.0.



\- Dependencies installed using requirements.txt.

\- OpenAI, ChromaDB and python-dotenv imports verified.

\- Fresh environment setup completed successfully.

\- No API keys or secrets committed to the repository.



Security

* API keys are stored in local environment variables.
* The .env file is excluded through .gitignore.
* Virtual environments and local document data are not committed.
