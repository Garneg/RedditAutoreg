# RedditAutoreg <img src="https://www.redditinc.com/assets/images/site/reddit-logo.png" height=32/>
Reddit auto registration python script makes signing up a bit easier and faster by using PyAutoGui library.
This branch contains additional code for more automation with [Windscribe VPN service](https://windscribe.com). 

*Note that it's not finished yet, you might have to replace screenshots to make it work*

## Dependencies
- PyAutoGui
- Pillow
- Windscribe Desktop App and CLI




#### If you got problems with the windscribe cli
- Go to utils.py and replace `C:\Program Files (x86)\Windscribe\windscribe-cli.exe` with the actual windscribe-cli.exe path
- Check if all locations from `windscribe_locations.txt` file are avaliable for you. You can do it with windscribe desktop app
