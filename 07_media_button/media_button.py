import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

def download_media(url):
    # Only try to download if it's a real web link
    if not url or not url.startswith("http"):
        messagebox.showerror("Error", "Please paste a valid URL (starting with http)")
        return

    try:
        print(f"--- Trying gallery-dl for images: {url} ---")
        subprocess.run(["gallery-dl", url], check=True)
    except:
        print("Not a gallery. Trying yt-dlp for video...")
        subprocess.run(["yt-dlp", url])

# This creates the hidden main window and the popup box
root = tk.Tk()
root.withdraw() 

# This is your "Button" popup
user_url = simpledialog.askstring("Media Button", "Paste the URL you want to download:")

if user_url:
    download_media(user_url.strip())