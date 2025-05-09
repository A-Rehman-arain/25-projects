import requests
from urllib.parse import urlparse

def extract_github_username(url):
    """Extract the username from a valid GitHub URL."""
    try:
        parsed = urlparse(url)
        path_parts = [part for part in parsed.path.split('/') if part]

        # If URL is valid, the first part will be the username
        if path_parts and len(path_parts) > 1 and path_parts[1] == 'repos':
            return None  # Reject repository URL
        if path_parts:
            return path_parts[0]  # Username is the first part
        return None
    except Exception as e:
        return None

def get_github_user_data(username):
    """Fetch the GitHub user data using GitHub's API."""
    api_url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Will raise an HTTPError if the response is not 2xx
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

def display_user_info(data):
    """Display user data in a readable format."""
    if "error" in data:
        print(f"\n❌ {data['error']}")
        return

    print("\n✅ GitHub Profile Info:")
    print("------------------------")
    print(f"👤 Username      : {data.get('login', 'N/A')}")
    print(f"🧑 Name          : {data.get('name', 'Not set')}")
    print(f"📄 Bio           : {data.get('bio', 'Not set')}")
    print(f"📸 Profile Image : {data.get('avatar_url')}")
    print(f"📦 Public Repos  : {data.get('public_repos')}")
    print(f"👥 Followers     : {data.get('followers')}")
    print(f"🔗 Profile URL   : {data.get('html_url')}\n")

def main():
    """Main function to interact with the user."""
    print("🔍 GitHub Profile Image & Info Extractor")
    print("----------------------------------------")
    
    # Get input from the user
    url = input("Enter GitHub profile URL: ").strip()
    
    # Ensure the URL has a valid format
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Extract the username
    username = extract_github_username(url)
    if not username:
        print("\n❌ Could not extract a valid GitHub username from the URL.")
        return

    # Get GitHub user data
    user_data = get_github_user_data(username)
    
    # Display user information
    display_user_info(user_data)

if __name__ == "__main__":
    main()
