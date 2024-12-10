@echo off
setlocal enabledelayedexpansion

echo Select the platform to download video from:
echo 1. YouTube
echo 2. bilibili
set /p platform="Enter the number (1 or 2): "

if "%platform%"=="1" (
    set /p url="Please input the YouTube URL: "
    echo YouTube URL: !url!
    yt-dlp -f best -o "%%(title)s.%%(ext)s" "!url!"
) else if "%platform%"=="2" (
    set /p url="Please input the Bilibili URL: "
    echo Bilibili URL: !url!
    yt-dlp -f "bv*[height<=1080]+ba/b" -o "%%(title)s.%%(ext)s" --cookies-from-browser firefox --concurrent-fragments 8 --extractor-retries 3 "!url!"
) else (
    echo Invalid selection. Exiting...
)

pause