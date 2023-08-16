import requests

api_key = "521d9de5c2c14bd68d595796809c9622"


api_endpoint = "https://api.spoonacular.com/recipes/random"
params = {"apiKey": api_key,"number": 1  # Specify the number of random recipes you want to fetch
}

# Make the API request
response = requests.get(api_endpoint, params=params)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Process the API response
    api_data = response.json()
    # Extract and print recipe details
    if "recipes" in api_data and len(api_data["recipes"]) > 0:
        recipe = api_data["recipes"][0]
        print("Recipe Title:", recipe["title"])
        print("Recipe Instructions:", recipe["instructions"])
    else:
        print("No recipes found in the API response.")
else:
    print("API request failed with status code:", response.status_code)


