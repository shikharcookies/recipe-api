import requests

api_key = "521d9de5c2c14bd68d595796809c9622"

search_endpoint = "https://api.spoonacular.com/recipes/complexSearch"
params = {
    "apiKey": api_key,
    "query": "chicken",
    "number": 5
}

response = requests.get(search_endpoint, params=params)

if response.status_code == 200:
    api_data = response.json()
    if "results" in api_data:
        for recipe in api_data["results"]:
            print("Recipe Title:", recipe["title"])
            print("Recipe ID:", recipe["id"])
            print("Image URL:", recipe["image"])
            print("Instructions:")

            # Fetch detailed recipe information using recipe ID
            recipe_id = recipe["id"]
            recipe_info_endpoint = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
            recipe_info_params = {
                "apiKey": api_key,
            }
            recipe_info_response = requests.get(recipe_info_endpoint, params=recipe_info_params)

            # Check if the recipe information request was successful (HTTP status code 200)
            if recipe_info_response.status_code == 200:
                # Process the recipe information
                recipe_info = recipe_info_response.json()
                print(recipe_info["instructions"])
                print("-" * 50)
            else:
                print("Failed to fetch recipe information. Status code:", recipe_info_response.status_code)
    else:
        print("No recipes found in the API response.")
else:
    print("API request failed with status code:", response.status_code)
