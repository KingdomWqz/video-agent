echo "Select the platform to download video from:"
echo "1. YouTube"
echo "2. bilibili"
read -p "Enter the number (1 or 2): " platform

if [ "$platform" == "1" ]; then
    read -p "Please input the YouTube URL: " url
    echo "YouTube URL: $url"
    ./yt-dlp_macos -f best -o "%(title)s.%(ext)s" "$url"
elif [ "$platform" == "2" ]; then
    read -p "Please input the Bilibili URL: " url
    echo "Bilibili URL: $url"
    ./yt-dlp_macos -f "bv*[height<=1080]+ba/b" -o "%(title)s.%(ext)s" --cookies-from-browser firefox --concurrent-fragments 8 --extractor-retries 3 "$url"
else
    echo "Invalid selection. Exiting..."
fi

# Pause to allow user to see the output before the script exits
read -p "Press any key to continue..."