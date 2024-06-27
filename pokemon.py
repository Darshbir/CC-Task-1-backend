import requests
import sys
import shutil

def fetch_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().replace(' ','-')}"
    #replace just for mr mime and tapu koko:)
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(f"Name: {data['name'].capitalize()}")
            print(f"National Number: {data['id']}")
            print("Type")
            for type in data['types']:
                print(f" -{type['type']['name'].capitalize()}")
            print("Abilities:")
            for ability in data['abilities']:
                print(f" -{ability['ability']['name'].capitalize()}")

            print(f"Height: {data['height']/10} m")
            print(f"Weight: {data['weight']/10} Kg")

            print("\nBase Stats:")
            sum = 0
            for stat in data['stats']:
                sum+=stat['base_stat']
                print(f"{stat['stat']['name'].capitalize().replace('-',' ')}: {stat['base_stat']}")
            print(f"Total: {sum}")
            image_url = data['sprites']['front_default']
            save_path = "sprite.png"
            response1 = requests.get(image_url, stream=True)
            if response1.status_code == 200:
                with open(save_path, 'wb') as file:
                    shutil.copyfileobj(response1.raw, file)
                print(f"Image successfully downloaded: {save_path}")
            else:
                print(f"Failed to download image. Status code: {response1.status_code}")
    
        elif response.status_code == 400:
            print(f"Error: Invalid Pokemon name '{pokemon_name}'")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pokemon.py <pokemon_name>\n#Edit: for 2 letter pokemon names usage is: python pokemon.py \"pokemon_name\"")
        sys.exit(1)
    
    pokemon_name = ' '.join(sys.argv[1:])
    fetch_data(pokemon_name)