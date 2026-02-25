import yt_dlp
import os

def download_audio():
    # Junior Sysadmin Tip: Always prompt clearly so the user knows what to do
    video_url = input("Paste the video URL: ")
    
    # This '~' shortcut makes the script 'portable' between your iMac and Laptop
    download_path = os.path.expanduser("~/Downloads")
    
    # Check if the directory exists (a good safety ritual!)
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Configuration for yt-dlp to extract high-quality MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False, # Set to True if you want a cleaner terminal output
    }

    try:
        print(f"\nTargeting folder: {download_path}")
        print("Starting extraction... please wait.")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            
        print(f"\nMission Accomplished! Your audio is in: {download_path}")
    except Exception as e:
        # Catching errors gracefully is a core sysadmin ritual
        print(f"Extraction failed: {e}")

if __name__ == "__main__":
    download_audio()