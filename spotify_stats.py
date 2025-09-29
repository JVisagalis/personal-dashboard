print("🚀 Testing Spotify API connection...")

import requests
import base64

# Your Spotify credentials
CLIENT_ID = "9e4ea15621f24d2abd92bf387923fd91"
CLIENT_SECRET = "d683cc609c864d29b9b8f698cdfcd2d8"

def test_spotify_auth():
    print("1. Encoding credentials...")
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()
    print("   ✅ Credentials encoded")
    
    print("2. Requesting access token from Spotify...")
    try:
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            headers={
                "Authorization": f"Basic {auth_base64}",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={"grant_type": "client_credentials"},
            timeout=10
        )
        
        print(f"3. Spotify response: {response.status_code}")
        
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data['access_token']
            print("   🎉 SUCCESS! Got Spotify access token")
            print(f"   Token: {access_token[:20]}...")
            return access_token
        else:
            print(f"   ❌ Failed to get token: {response.status_code}")
            print(f"   Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"   💥 Request failed: {e}")
        return None

def test_spotify_search(token):
    print("4. Testing Spotify search...")
    try:
        response = requests.get(
            "https://api.spotify.com/v1/search",
            headers={"Authorization": f"Bearer {token}"},
            params={"q": "Daft Punk", "type": "track", "limit": 3},
            timeout=10
        )
        
        print(f"5. Search response: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            tracks = data['tracks']['items']
            print("   🎵 SUCCESS! Found tracks:")
            for track in tracks:
                print(f"   - {track['name']} by {track['artists'][0]['name']}")
        else:
            print(f"   ❌ Search failed: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"   💥 Search failed: {e}")

if __name__ == "__main__":
    token = test_spotify_auth()
    if token:
        test_spotify_search(token)
    print("🏁 Test complete")