import requests
import os

# NASA's Astronomy Picture of the Day API
URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def fetch_space_photo():
    print("🚀 Connecting to NASA...")
    try:
        response = requests.get(URL)
        response.raise_for_status() 
        
        data = response.json()
        img_url = data.get("url")
        
        # Clean the title for a safe filename
        title = data.get("title").replace(" ", "_").replace(":", "")
        filename = f"{title}.jpg"
        
        # Target your Downloads folder dynamically
        download_path = os.path.expanduser(f"~/Downloads/{filename}")
        
        print(f"📡 Found: {data.get('title')}")
        
        # Download the image binary data
        img_data = requests.get(img_url).content
        with open(download_path, 'wb') as f:
            f.write(img_data)
        
        print(f"✅ Success! Saved to Downloads as: {filename}")
        
        # THE FIX: We wrap the path in double quotes so apostrophes don't break the shell
        os.system(f'open -R "{download_path}"')
        
    except Exception as e:
        print(f"❌ Hiccup! Something went wrong: {e}")

if __name__ == "__main__":
    fetch_space_photo()