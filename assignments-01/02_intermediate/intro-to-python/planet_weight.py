def calculate_weight(earth_weight, planet):
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    if planet in gravity_factors:
        return round(earth_weight * gravity_factors[planet], 2)
    else:
        return None

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")
    
    planetary_weight = calculate_weight(earth_weight, planet)
    
    if planetary_weight is not None:
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the list.")

if __name__ == "__main__":
    main()