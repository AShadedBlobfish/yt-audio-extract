if [[ $EUID > 0 ]]
    then echo "Error: Root permissions are required to write to /usr/bin directory. Please run script as root to install to path"
    exit
fi

cp yt-audio-extract /usr/bin/yt-audio-extract
cp yt-audio-extract.py /usr/bin/yt-audio-extract.py

echo "Installed successfully. Run 'yt-audio-extract --help' for usage instructions"