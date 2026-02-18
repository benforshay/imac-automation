tell application "iTerm"
	activate
	if (count of windows) is 0 then
		create window with default profile
	end if
	tell current session of current window
		write text "cd ~/Developer/imac-automation/01_mpv_trigger && python3 yt_player.py"
	end tell
end tell