# Doctor Xavi Consults

**Doctor Xavi Consults** is an AI-powered automated medical assistance project. The system interacts with users in multiple languages, providing diagnoses, medication recommendations, remedies, and disease prevention advice.

## Technologies Used

- **Semantic Kernel**: Used to integrate and manage AI function flows and custom plugins.
- **OpenAI GPT-4o**: The main AI model for processing natural language.
- **Chainlit**: Framework for managing real-time communication with users.
- **Python**: The primary programming language.
- **Translation Service**: For detecting and translating messages between different languages.

## Main Features

1. **Condition Diagnosis**: Allows users to describe their symptoms and receive an automated diagnosis.
2. **Medication Recommendation**: The system suggests medications based on the symptoms provided by the user.
3. **Remedy Suggestions**: Provides natural and conventional remedies to alleviate symptoms.
4. **Disease Prevention**: Gives advice on how to prevent common diseases.

## Project Structure

The project is structured into several modules:

- **main.py**: The main file that manages the application flow, including initializing the `Kernel` and configuring the medical plugin.
- **medical_plugin.py**: Contains the medical functions invoked depending on the user's request.
- **translation_service.py**: Service for detecting and translating messages between different languages.
- **chat_history.py**: A class that keeps the chat history throughout the conversation.

## Installation

### Prerequisites

- Python 3.7+
- Install dependencies from the `requirements.txt` file.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/John-Vivas/doctor-xavi-consults
cd doctor-xavi-consults
```
