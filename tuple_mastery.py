flight_itineraries = [("Bob", "Tokyo", "San Francisco"), 
                      ("Alice", "New York", "London")]

def format_itineraries(itineraries):
    formatted_itineraries = []
    for index, (traveler_name, origin, destination) in enumerate(itineraries,1):
        itinerary = f"Itinerary {index}: {traveler_name} - from {origin} to {destination}"
        formatted_itineraries.append(itinerary)
        return(formatted_itineraries)
    
format = format_itineraries(flight_itineraries)
print (format)
