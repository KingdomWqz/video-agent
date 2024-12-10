@echo off
set /p url="Please input the youtube url: "
yt-dlp -f best -o "%%(title)s.%%(ext)s" "%url%"
pause