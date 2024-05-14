import requests

def search_food(query, api_key):
    """
    Search for foods using the USDA Food Central API.

    Args:
        query (str): The search query.
        api_key (str): Your API key for accessing the USDA Food Central API.

    Returns:
        dict: A dictionary containing the search results.
    """
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        "query": query,
        "api_key": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None