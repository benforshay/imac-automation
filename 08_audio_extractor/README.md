# 08_audio_extractor: Universal Audio Extraction Tool

## 🚀 The Problem
I needed a streamlined, high-fidelity way to harvest audio assets for my Navidrome server and personal archive without manually dealing with complex CLI flags for every new source (YouTube, local video, etc.).

## 🛠 The Solution
A hybrid automation bridge that combines the raw power of **Python** and **FFmpeg** with the accessibility of the **macOS UI (AppleScript)**. This allows for "One-Click" extraction while maintaining total control over the audio quality.

### Key Components:
- **`extract.py`**: The core engine. Handles the logic for identifying the source, defining the bitrates, and executing the `ffmpeg` conversion.
- **`SoundExtractor.scpt`**: The UI Bridge. An AppleScript that triggers the Python logic via a dedicated system button, making the tool accessible to non-technical "Civilian" workflows.

## ⚙️ Technical Specs
- **Logic:** Python 3.x
- **Engine:** FFmpeg (handling conversion and metadata)
- **UI:** AppleScript / macOS System Services
- **Format Support:** Universal (converts any video source to high-quality audio)

## 📂 Project Structure
- `extract.py`: Python automation logic.
- `extractor.scpt`: AppleScript UI trigger.
- `README.md`: Project documentation.