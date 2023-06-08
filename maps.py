import googlemaps
import mtranslate
import json

# Set up the Google Maps API client
gmaps = googlemaps.Client(key='AIzaSyB4r4HwJsKgA65MmDCwx0SpWQ50XQAqtT0')

def geocode_address(address):
    # Perform geocoding request
    try:
        geocode_result = gmaps.geocode(address)
    except:
        print(f"Could not geocode address: {address}")
        geocode_result = None
    
    # Extract the coordinates from the geocoding result
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return (latitude, longitude)
    else:
        return None

def translate_text(text, target_language):
    translation = mtranslate.translate(text, target_language, 'auto')
    return translation

def translate_directions_data(directions_data, target_language):
    translated_directions = {}
    for key, value in directions_data.items():
        if key == 'instructions':
            translated_instructions = []
            for instruction in value:
                translated_instruction = translate_text(instruction, target_language)
                translated_instructions.append(translated_instruction)
            translated_directions[key] = translated_instructions
        else:
            translated_value = translate_text(value, target_language)
            translated_directions[key] = translated_value
    return translated_directions

def get_bus_directions(starting_station, destination_station):
    # Geocode the starting and destination stations to get their coordinates
    starting_location = geocode_address(starting_station)
    destination_location = geocode_address(destination_station)
    
    if starting_location is None or destination_location is None:
        return None

    # Perform directions request with language parameter
    directions_result = gmaps.directions(starting_location,
                                         destination_location,
                                         mode='transit',
                                         language='he')

    # Parse the directions and extract the relevant information
    instructions = []
    for step in directions_result[0]['legs'][0]['steps']:
        instruction = step['html_instructions']
        transit_details = step.get('transit_details')
        if transit_details:
            bus_number = transit_details['line'].get('short_name', '')
            if not bus_number:
                bus_number = transit_details['line'].get('name', '')
            instruction = f"Take bus {bus_number} - {instruction}"
        instructions.append(instruction)

    # Calculate the total distance and duration
    distance = directions_result[0]['legs'][0]['distance']['text']
    duration = directions_result[0]['legs'][0]['duration']['text']

    # Construct the directions data dictionary
    directions_data = {
        'instructions': instructions,
        'distance': distance,
        'duration': duration
    }

    return directions_data

# Example usage
#starting_station = "Tel Aviv Central Bus Station"
#destination_station = "Tel Aviv University Bus Station"

def get_bus_directions_in_english(starting_station, destination_station):
    directions = get_bus_directions(starting_station, destination_station)
    if directions is not None:
        # Translate the directions data to English
        translated_directions = translate_directions_data(directions, 'en')
        directions_json = json.dumps(translated_directions)
        return directions_json#print(directions_json)
    else:
        return "There is definitely no route available for this path at this time of day."
        #print("Invalid starting or destination station.")
