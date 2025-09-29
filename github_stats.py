# github_stats.py

import requests

GITHUB_API_URL = "https://api.github.com/users/{username}/repos"

def get_github_repos(username):
    """Fetches and returns a list of repositories for a given GitHub username."""
    
    url = GITHUB_API_URL.format(username=username)
    print(f"Fetching data from: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"✅ Successfully found {len(repos)} repositories!")
        return repos
    else:
        print(f"❌ Error: Could not fetch data (Status Code: {response.status_code})")
        return []

def main():
    username = input("Enter your GitHub username: ")
    repos = get_github_repos(username)
    
    # --- NEW: Handle the case where there are no repos ---
    if not repos:
        print("🤔 It looks like you don't have any public repositories yet.")
        print("   No problem! This is a great start for your coding journey.")
        print("   This 'personal-dashboard' will be your first one!")
        return  # Exit the function early
    
    # Only run this part if there ARE repositories
    print(f"\n--- Your Last {min(5, len(repos))} Repositories ---")
    for repo in repos[:5]:
        print(f"- {repo['name']}")
        print(f"  (Created: {repo['created_at'][:10]})")
        print(f"  URL: {repo['html_url']}")
        print()

if __name__ == "__main__":
    main()