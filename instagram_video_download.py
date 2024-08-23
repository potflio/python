import requests
from bs4 import BeautifulSoup
import re

def get_instagram_reel_url(post_url):
    response = requests.get(post_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script', type="text/javascript")
        for script in scripts:
            if 'video_url' in script.text:
                json_data = re.findall(r'{"video_url":.*?"', script.text)[0]
                video_url = json_data.split('"video_url":"')[1].split('","')[0].replace('\\u0026', '&')
                return video_url
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
    return None

def download_video(video_url, filename):
    response = requests.get(video_url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"Video downloaded successfully: {filename}")

# Example usage
post_url = str(input("enter url link"))  # Replace with the Instagram Reels URL
video_url = get_instagram_reel_url(post_url)
if video_url:
    download_video(video_url, 'instagram_reel.mp4')
else:
    print("Could not find video URL.")
