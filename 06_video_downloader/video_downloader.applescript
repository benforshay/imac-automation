set theURL to display dialog "Paste Video URL:" default answer ""
set targetURL to text returned of theURL

tell application "iTerm"
    activate
    set newWindow to (create window with default profile)
    tell current session of newWindow
        -- This version has NO numbering logic, just clean names
        write text "yt-dlp -f 'bestvideo+bestaudio/best' --merge-output-format mp4 -o '~/Downloads/%(title)s.%(ext)s' " & quoted form of targetURL
    end tell
end tell
