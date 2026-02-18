import os

# 1. Path to a text file where you'll paste your links
LINKS_FILE = "links_to_scrape.txt"

def bulk_scrape():
    # Create the text file if it doesn't exist yet
    if not os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, 'w') as f:
            f.write("# Paste your links here, one per line\n")
        print(f"Created {LINKS_FILE}. Paste your links there and run again!")
        return

    # Run gallery-dl using the text file as the source
    # -i reads from a file, -d saves to Downloads
    print(f"🕵️‍♂️ Scanning {LINKS_FILE} for image galleries...")
    command = f'gallery-dl -i {LINKS_FILE} -d ~/Downloads'
    
    os.system(command)
    print("\n✅ Bulk scrape finished. Check your Downloads folder!")

if __name__ == "__main__":
    bulk_scrape()