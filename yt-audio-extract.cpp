#include <cstdlib>
#include <iostream>

int main(int argc, char** argv) {
    std::string argsString = "";
    const std::string space = " ";
    for (int i = 1; i < argc; i++) {
        argsString.append(argv[i] + space);
    }

    const std::string call = "python /bin/yt-audio-extract.py " + argsString;
    int returnCode = system(call.c_str());

    if (returnCode != 0)
    {
        std::cout << "Command execution failed or returned non-zero: " << returnCode << std::endl;
    }

    return 0;
}