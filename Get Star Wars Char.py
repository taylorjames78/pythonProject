import requests

def get_star_wars_character(character_id):
    # Define the API endpoint for the Star Wars API (SWAPI)
    api_url = f"https://www.swapi.tech/api/people/{character_id}"

    # Send a GET request to the SWAPI
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Access relevant information
        character_name = data['result']['properties']['name']
        birth_year = data['result']['properties']['birth_year']
        gender = data['result']['properties']['gender']


        # Print the information
        print(f"Character Name: {character_name}")
        print(f"Birth Year: {birth_year}")
        print(f"Gender: {gender}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    # Specify the character ID (Luke Skywalker's ID is '1' in this case)
    character_id = '1'

    # Call the function with the character ID
    get_star_wars_character(character_id)
