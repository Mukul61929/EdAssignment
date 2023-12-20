import json

indian_states = {
    'West Bengal': 'Kolkata',
    'Jharkhand': 'Ranchi',
    'Maharashtra': 'Mumbai',
    'Tamil Nadu': 'Chennai',
    'Orrisa': 'Bhubneswar',
    'Bihar': 'Patna',
    'Rajasthan': 'Jaipur',
    
}

# Write the dictionary to a JSON file
json_file_path = 'indian_states.json'
with open(json_file_path, 'w') as file:
    json.dump(indian_states, file, indent=2)

print(f"The information has been written to {json_file_path}.")

