import requests

# Replace these with your own keys
google_api_key = "your_google_api_key"
bing_api_key = "your_bing_api_key"

def search_google(query, api_key):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&q={query}&num=10&start=1"
    response = requests.get(url)
    return response.json()

def search_bing(query, api_key):
    url = f"https://api.bing.microsoft.com/v7.0/search?q={query}&count=10&offset=0"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    query = input("Enter your search query: ")
    google_results = search_google(query, google_api_key)
    bing_results = search_bing(query, bing_api_key)

    # Combine the results from both APIs into a single list
    combined_results = google_results["items"] + bing_results["webPages"]["value"]

    # Print the search results
    for result in combined_results:
        print(result["title"])
        print(result["link"])
        print()

if __name__ == "__main__":
    main()