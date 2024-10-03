# Confidential Document Retrieval Agent

## Introduction
Welcome to the *Confidential Document Retrieval Agent*! This project is a sample chatbot powered by a Large Language Model (LLM) ReAct agent, implemented with Langchain. It's designed as an educational tool for security researchers, developers, and enthusiasts to understand and experiment with prompt injection attacks in ReAct agents.

The project focuses on **Thought/Action/Observation injection** techniques in AI-driven applications.

![Confidential Demo](static/confidential-demo.gif)

## Features
- Simulates a vulnerable chatbot environment for confidential document access.
- Allows for prompt injection experimentation.
- Provides a ground for learning prompt injection vectors.

## Installation

### Python Environment Setup

To get started, set up your Python environment by following these steps:

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Running the Application
Before running the application, add a valid OpenAI API key to the `.env` file (create it by copying the env.list template).

To run the application:

```sh
streamlit run main.py
```

## Docker Image
To build and run the Docker image:

```sh
docker build -t confidential-doc-retrieval .

# Populate the env.list with necessary environment variables (e.g., OpenAI API key), then run:
docker run --env-file env.list -p 8501:8501 confidential-doc-retrieval
```

## Usage
Interact with the vulnerable chatbot to test prompt injection by issuing commands and observing responses.

## Security Considerations
This project is intentionally vulnerable to demonstrate the importance of securing AI-driven applications against prompt injection attacks. In a production environment, ensure proper security measures are implemented.

## Conclusion
The Confidential Document Retrieval Agent serves as an educational tool to understand the vulnerabilities associated with prompt injection in AI-driven applications. By experimenting with both normal and hacking flows, developers and security researchers can gain insights into securing such systems effectively.

Feel free to contribute, experiment, and enhance the security mechanisms to prevent such vulnerabilities in real-world applications.