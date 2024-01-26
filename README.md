# YouTube audio extract

A python script for Linux designed to make the process of downloading and extracting audio from large amounts of videos with yt-dlp easier.

The script can take a link to a video or playlist as input and pass the arguments to yt-dlp, as well as renaming the files afterwards to be the same as the video's title (Removing the video ID added automatically by yt-dlp).
It can also take a file containing links to videos or playlists and pass each link to yt-dlp iteratively for efficient mass downloading.

## Dependencies

- Python >3.10.0
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- GCC (if installing as a binary)

## Installation
### Option 1: Install as an executable binary (requires GCC)

1. Clone this repository    
`git clone https://github.com/AShadedBlobfish/yt-audio-extract`

2. Navigate to folder    
`cd yt-audio-extract`

3. Run install script as root (root permissions are required to write to /usr/bin)    
`sudo ./install.sh`

### Option 2: Run script outside of bin folder

1. Clone this repository    
`git clone https://github.com/AShadedBlobfish/yt-audio-extract`

2. Execute script using the following command    
`python [path to yt-audio-extract directory]/yt-audio-extract.py`
