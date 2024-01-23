import sys
import os

version = "0.1.0"

class YT_Download_Error(Exception):
    def __init__(self, args):
        super().__init__(args)

def checkDeltaFiles(startFiles, endFiles):
    newFiles = []
    for j in endFiles:
        if j not in startFiles:
            newFiles.append(j)
                    
    return newFiles

def main():
    args = sys.argv[1:]
    
    j = -1
    input = ""
    file = ""
    format = "mp3"
    rename = True
    help = False
    
    debug = False
    
    for i in args:
        if j > -1:            
            if args[j] in [ '-i', '--input' ]:
                input = i
            elif args[j] in [ '-f', '--file' ]:
                file = i
            elif args[j] == '--format':
                format = i
                
        if i == '--debug': debug = True
        if i == '--no-rename': rename = False
        if i in [ '--help', '-h' ]: help = True
        
        j += 1
        
    if help:
        print(f"""

YouTube Audio extractor by AShadedBlobfish (v{version})

Requires yt-dlp. Ensure it is installed and on path


Usage:

yt-audio-extract [args]

Arguments:

-i link | --input link		Download and extract audio from video or playlist link
-f file | --file file		Download and extract audio from multiple videos or playlist contained in a file (seperated by line breaks)
--debug				Run in debug mode
--format format			Passed to yt-dlp to determine the output format of the audio files (defaults to .mp3)
--no-rename			Do not rename files (leave their auto-generated filenames from yt-dlp)
-h | --help			Show this help
""")
        return    
        
    if not debug: sys.tracebacklimit = 0
    
    # Input validation and exception handling
    
    base_message = [ "\n\n\nExpected exactly one of the following (", " received):\nSingle video: -i <link>\nMultiple videos: -f <file> where <file> is the path to a file containing video links separated by line breaks\n"]
    
    if input == "" and file == "":
        raise YT_Download_Error(base_message[0] + "None" + base_message[1])
    elif input != "" and file != "":
        raise YT_Download_Error(base_message[0] + "2" + base_message[1])
    elif input == "":
        mode = 'f'
    elif file == "":
        mode = 'i'
    else:
        raise YT_Download_Error("\n\n\n\n")
    
    
    
    if mode == 'f':
        File = open(file)
        lines = File.readlines()
        links = []
        for i in lines:
            links.append(i[:-1])
        
        for i in links:
            initialFiles = os.listdir()
            os.system(f"yt-dlp {i} -x --audio-format {format}")
            files = os.listdir()
            
            if rename:
                newFiles = checkDeltaFiles(initialFiles, files)

                if len(newFiles) == 1:
                    os.rename(newFiles[0], newFiles[0][:-(14+(len(format))+1)] + f".{format}")
                else:
                    for k in newFiles:
                        if k[-(len(format) + 14)] == "[" and k[-(len(format) + 2):] == f"].{format}":
                            os.rename(k, k[:-(14+(len(format))+1)] + f".{format}")
            
            
    elif mode == 'i':
        initialFiles = os.listdir()
        os.system(f"yt-dlp {input} -x --audio-format {format}")
        files = os.listdir()
        
        if rename:
            newFiles = newFiles = checkDeltaFiles(initialFiles, files)

            if len(newFiles) == 1:
                os.rename(newFiles[0], newFiles[0][:-(14+(len(format))+1)] + f".{format}")
            else:
                for k in newFiles:
                    if k[-(len(format) + 14)] == "[" and k[-(len(format) + 2):] == f"].{format}":
                        os.rename(k, k[:-(14+(len(format))+1)] + f".{format}")
        
    

    
if __name__ == "__main__":
    main()
