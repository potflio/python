from pytube import YouTube

def download_youtube_video(video_url, save_path):
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading '{yt.title}'...")
        stream.download(output_path=save_path)
        print(f"Download completed! Video saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



def download_audio(url, output_path='.'):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download the audio stream
        audio_stream.download(output_path=output_path)
        
        print(f"Audio downloaded successfully: {audio_stream.default_filename}")
        
    except Exception as e:
        print(f"Error: {e}")

video_url = input("Enter the URL:")  
print("Choose Your type\n")
print("1.video\n")
print("2.audio")
type = input("Choose the type:")
if type == "1":
    
    download_youtube_video(video_url, save_path = "videos")
else:
    download_audio(video_url, output_path='songs')
