tell application "iTerm"
	activate
	-- Create a new window or use the current one
	set newWindow to (create window with default profile)
	tell current session of newWindow
		write text "cd ~/Developer/imac-automation/08_audio_extractor && python3 audio_extractor.py"
	end tell
end tell