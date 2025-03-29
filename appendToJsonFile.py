import json

def append(data, filename):
    try:
        # Open file in read mode
        with open(filename, 'r') as f:
            # Load existing data
            existing_data = json.load(f)
            
        # Add new data
        if isinstance(existing_data, list):
            existing_data.append(data)
        elif isinstance(existing_data, dict):
            if 'items' not in existing_data:
                existing_data['items'] = []
            existing_data['items'].append(data)
        else:
            raise ValueError("Invalid JSON structure")
            
        # Write back to file
        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)
            
    except FileNotFoundError:
        # Create new file if it doesn't exist
        with open(filename, 'w') as f:
            json.dump([data], f, indent=4)  