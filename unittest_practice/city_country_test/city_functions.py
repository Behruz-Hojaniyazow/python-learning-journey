def city_country(city: str, country: str, population='') -> str:
    
    if population:
        full_address = f"{city.strip()} - {country.strip()}"
        
    else:
        full_address = f"{city.strip()}, {country.strip()}"
    
    return full_address.title()