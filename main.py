import requests
from bs4 import BeautifulSoup

def download_instagram_profile_picture(username):
    # Construct the profile URL
    url = f"https://www.instagram.com/{username}/"

    # Send a GET request to the profile URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the profile picture URL
        profile_picture_url = soup.find('meta', property='og:image')['content']

        # Download the profile picture
        response = requests.get(profile_picture_url)
        if response.status_code == 200:
            with open(f"{username}_profile_picture.jpg", "wb") as f:
                f.write(response.content)
                print("Profile picture downloaded successfully.")
        else:
            print("Failed to download profile picture.")
    else:
        print("Profile not found or error occurred.")

# Example usage:
username = "example_username"
download_instagram_profile_picture(username)
