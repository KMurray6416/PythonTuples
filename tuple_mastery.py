flight_itineraries = ("Bob", "Tokyo", "San Francisco"),("Alice", "New York", "London")
def format_itineraries(itineraries):
    formatted_itineraries = []
    for element in itineraries:
        if element:
            for index, itinerary in enumerate(itineraries):
                traveler_name,origin,destination =itinerary
                itineraries = f"Itinerary {index + 1}: {traveler_name} - from {origin} to {destination}"
                formatted_itineraries.append(itineraries)
        return"\n".join(formatted_itineraries)
    
formatted = format_itineraries(flight_itineraries)
print(formatted)