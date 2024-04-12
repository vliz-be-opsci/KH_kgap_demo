import requests
import json
import pandas as pd

# read ROR urls
df = pd.read_csv('data/ror_info/KH_rorIDs.csv')

for url in df['RorUrl']:
    # get ID & format into correct URL
    ror_id = url.split('/')[-1]
    base_url = f'https://api.ror.org/organizations/{ror_id}'
    # Make request
    response = requests.get(base_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Load JSON data from the response
        json_data = response.json()
        # write JSON data to file
        with open("./data/ror_info/json/" + ror_id + '.json', 'w') as file:
            json.dump(json_data, file)
    else:
        print(f"Failed to retrieve JSON data for {base_url}. Status code: {response.status_code}")