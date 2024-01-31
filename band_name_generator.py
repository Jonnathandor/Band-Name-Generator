def band_name_generator():
    print("Welcome to the Band Name Generator!")
    user_name = input("What's your name ")
    print(f"Hello, {user_name}! Let's create a unique band name for you.")

    city_name = input("What's the name of the city you grew up in? ")
    pet_name = input("What's the name of your pet? ")

    band_name = city_name + " " + pet_name
    print(f"Your band name could be: {band_name}")

if __name__ == "__main__":
    band_name_generator()

