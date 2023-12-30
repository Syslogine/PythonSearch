import requests
import json
import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace these with your own Google API key and Programmable Search Engine ID
GOOGLE_API_KEY = "your_google_api_key"
SEARCH_ENGINE_ID = "your_search_engine_id"

def is_valid_google_key(api_key):
    return api_key and api_key.startswith("AIza")

def check_api_keys():
    print("Enabled APIs:")
    if is_valid_google_key(GOOGLE_API_KEY):
        print("Google Custom Search API: Enabled")
    else:
        print("Google Custom Search API: Disabled (API key not provided or invalid)")

def search_google(query, api_key, cx):
    if not is_valid_google_key(api_key):
        print("Invalid or missing Google API key. Exiting.")
        return {}

    try:
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}&num=10&start=1"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        # Check for a 400 Bad Request error
        if response.status_code == 400:
            print(f"Error in Google search: {response.status_code} Bad Request")
            print(response.text)  # Print the raw response content
            return {}

        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error in Google search: {e}")
        return {}

def print_results(results):
    # Print the search results
    if not results or 'items' not in results:
        print("No search results found.")
        return

    for result in results['items']:
        print(result.get("title", ""))
        print(result.get("link", ""))
        print()

def write_to_json(results, filename="search_results.json"):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=2)

def main():
    check_api_keys()  # Display information about the enabled API

    if not is_valid_google_key(GOOGLE_API_KEY):
        print("Google API key is not valid. Exiting.")
        return

    query = input("Enter your search query: ")

    google_results = search_google(query, GOOGLE_API_KEY, SEARCH_ENGINE_ID)

    if not google_results:
        print("No search results found.")
        return

    print_results(google_results)

    # Write results to a JSON file
    write_to_json(google_results)
    print(f"Search results have been saved to 'search_results.json'.")

if __name__ == "__main__":
    main()
