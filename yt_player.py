import subprocess
import time
import sys

# Starts the music
url = "https://www.youtube.com/watch?v=v2NjCGVxA8I"
player = subprocess.Popen(["mpv", "--no-video", url])

print("RUNNING. Press Ctrl+C or Close Terminal to stop music.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    player.terminate()
    sys.exit()
finally:
    player.kill() # The final 'Shut Up' command







#
