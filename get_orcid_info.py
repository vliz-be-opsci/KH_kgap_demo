import requests
from rdflib import Graph
import pandas as pd

# Function to write json-ld from a url to a file:
def get_orcid_jsonld(url: str) -> None:
    # get OrcID
    orcid = url.split("/")[-1]
    # make request
    response = requests.get(url, headers={"Accept": "application/ld+json"})
    if response.status_code == 200:
        # Parse response into the RDF graph & serialize it back to json-ld format
        g = Graph()
        g.parse(data=response.json(), format='json-ld')
        response_jsonld = g.serialize(format='json-ld')
        # Write the JSON-LD data to a file
        with open("./data/orcid_info/jsonld/" + orcid + '.jsonld', 'w') as file:
            file.write(response_jsonld)
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return None

# Function to write turtle from a url to a file:
def get_orcid_ttl(url: str) -> None:
    # get OrcID
    orcid = url.split("/")[-1]
    # make request
    response = requests.get(url, headers={"Accept": "text/turtle"})
    if response.status_code == 200:
        # write response to file
        with open("./data/orcid_info/ttl/" + orcid + '.ttl', 'w') as file:
                file.write(str(response.text))
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return None


# Execute functions:
kh_data = pd.read_csv('data/orcid_info/KH_participantOrcIDs.csv')
for url in kh_data['OrcID']:
    get_orcid_jsonld(url)
    get_orcid_ttl(url)
