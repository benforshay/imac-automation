import os

def download_any_media(url):
    # Determine if it's likely a video (YouTube/Vimeo) or an image
    if "youtube.com" in url or "vimeo.com" in url:
        print("🎥 Video detected. Using yt-dlp...")
        command = f'yt-dlp -P ~/Downloads "{url}"'
    else:
        print("📸 Image/Gallery detected. Using curl fallback...")
        # This uses the 'test_output.jpg' name we proved earlier
        command = f'curl -L "{url}" -o ~/Downloads/downloaded_media.jpg'
    
    os.system(command)

# You can change this URL to anything!
link_from_browser = "https://i.redd.it/xj4n86f4yv9c1.jpeg"
download_any_media(link_from_browser)