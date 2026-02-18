import os

def download_photo_gallery(url):
    print(f"🚀 Scraping gallery from: {url}")
    
    # -d tells it where to save (Downloads folder)
    # --no-mtime prevents it from messing with 'date modified'
    command = f'gallery-dl -d ~/Downloads --no-mtime "{url}"'
    
    status = os.system(command)
    
    if status == 0:
        print("✅ Gallery saved to your Downloads folder!")
    else:
        print("❌ Site blocked the automatic scraper.")
        print("💡 Try copying the 'Direct Image Link' (the one ending in .jpg) instead.")

# Test it with a Reddit Gallery or a Pinterest Link
test_url = "https://www.reddit.com/r/pics/comments/18v6g0k/a_cool_photo/"
download_photo_gallery(test_url)