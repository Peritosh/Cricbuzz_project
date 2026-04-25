import requests

BASE_URL = "https://cricbuzz-cricket.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": "5c8313213bmshf14e5f5a3be7fbfp1cb61cjsn53b7df6a57eb",  
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

def get_live_matches():
    url = f"{BASE_URL}/matches/v1/live"
    
    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code)
            return None

    except Exception as e:
        print("Error:", e)
        return None




def get_top_stats(stats_type="mostRuns"):
    url = f"{BASE_URL}/stats/v1/topstats/0"

    querystring = {
        "statsType": stats_type
    }

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params=querystring,
            timeout=10   
        )

        print("STATUS:", response.status_code)

        if response.status_code == 200:
            return response.json()
        else:
            print("API ERROR:", response.text) 
            return None

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return None