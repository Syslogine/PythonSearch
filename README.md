# PythonSearch

This Python script utilizes the Google Custom Search API to perform searches and retrieve results. The script is designed to be customizable and easy to use.

## Prerequisites

- Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Getting Started

1. Clone this repository or download the script directly.

    ```bash
    git clone https://github.com/yarpii/PythonSearch.git
    ```

2. Navigate to the project directory:

    ```bash
    cd PythonSearch
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Obtain Google API Key:**
   
   Obtain a Google API key by following the [Google Cloud Console documentation](https://cloud.google.com/docs/authentication/api-keys).

2. **Create a Programmable Search Engine:**

   - Go to [Google Programmable Search Control Panel](https://programmablesearchengine.google.com/about/).
   - Create a Programmable Search Engine and note down the Search Engine ID.

3. **Configure the Script:**

   Open the script (`PythonSearch.py`) in a text editor and replace the placeholders with your Google API key and Programmable Search Engine ID.

    ```python
    GOOGLE_API_KEY = "your_google_api_key"
    SEARCH_ENGINE_ID = "your_search_engine_id"
    ```

## Usage

1. Run the script:

    ```bash
    python PythonSearch.py
    ```

2. Enter your search query when prompted.

3. View the search results in the console.

4. Optionally, the results are saved in a `search_results.json` file.

## Troubleshooting

- **API Key Issues:**
  If you encounter issues with the API key, double-check its validity and ensure it has the necessary permissions.

- **Search Engine Configuration:**
  Ensure that your Programmable Search Engine is properly configured, and the ID is correctly set in the script.

- **Quota and Billing:**
  Check your API usage in the [Google Cloud Console](https://console.cloud.google.com/), including quotas and billing information.

## Contributing

If you have suggestions, improvements, or want to contribute to the script, feel free to submit issues or pull requests on the [GitHub repository](https://github.com/yourusername/PythonSearch).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
