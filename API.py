import requests

# Function to fetch the person data
def fetch_person_data():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['results'][0]

def fetch_business_proposal():
    url = "https://itsthisforthat.com/api.php?json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return f"{data['this']} for {data['that']}"

def fetch_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return f'"{data["slip"]["advice"]}"'