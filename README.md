# Semantic Search Engine

This project leverages a pre-trained DistilBERT model to implement a semantic search system. It also includes automated testing using Selenium and the unittest framework.

## Project Structure :

- **`requirements.txt`**: Contains the Python dependencies for the project.
- **`search.ipynb`**: Jupyter Notebook for experimenting with the semantic search functionality and also includes the Streamlit app.
- **`simplewiki-2020-11-01.jsonl`**: Dataset file in JSONL format.
- **`test.py`**: Script for testing the application.

## Setup Instructions :

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```markdown
      streamlit run app.py
   ```
   **Note**: Before starting the application, ensure that you have executed all the cells in the `search.ipynb` file sequentially. This step is crucial for initializing the necessary components for the application to function correctly.

## Testing :

In a new terminal, run the test script:
   ```sh
   python test.py
   ```
**Note**: Ensure that the Streamlit app is running. You will also need to update the `XPATH`. To do this, inspect the running Streamlit app, copy the `XPATH`, and paste it into the appropriate location.

