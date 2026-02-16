 tell application "iTerm"
    if (count of windows) is 0 then
        create window with default profile
    end if
    tell current session of current window
        write text "cd ~/Developer/imac-automation && python3 yt_player.py"
    end tell
end tell
