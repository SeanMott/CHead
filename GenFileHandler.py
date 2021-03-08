#genarates a file handler for Platforms and Header in C

import sys
import os

#args formate || progName platform
#example || python GenLogger.py Smok
#example || python GenLogger.py Glfix
#example || python GenLogger.py Gwafix
#example || python GenLogger.py Vulfix

progName = sys.argv[1]

#writes the Windows file handler C file
def WriteWindowFileHandler():
    os.makedirs("src/Platforms/Windows", exist_ok= True)
    file = open("src/Platforms/Windows/WindowsFileHandler.c", "w+")
    file.write("""//the windows implementation of the File Handler

#include <Util\FileHandler.h>

#include <string.h>
#include <stdio.h>

	//gets the contents of a file
	const char* """ + progName + """_FileHandler_ReadFile(const char* filepath)
	{
		FILE* file;
		char* text = 0;
		long length;

		file = fopen(filepath, \"rb\");
		if (!file)
		{
			LogData(\"""" + progName + """ Error: File Handler || Failed to open file at: %s\\n\", filepath);
			return NULL;
		}

		fseek(file, 0, SEEK_END);
		length = ftell(file);
		fseek(file, 0, SEEK_SET);
		text = calloc(length, length);
		if (text)
			fread(text, 1, length, file);

		fclose(file);

		return text;
	}

	//checks if two strings match
	bool """ + progName + """_FileHandler_StringMatch(const char* string1, const char* string2)
	{
		return (strcmp(string1, string2) == 0 ? true : false);
	}""")

#writes the Mac file handler C file
def WriteMacFileHandler():
    pass

#writes the Linux file handler C file
def WriteLinuxFileHandler():
    pass

#writes the file handler Header file
def WriteHeaderFileHandler():
    os.makedirs("includes/Util", exist_ok= True)
    file = open("includes/Util/FileHandler.h", "w+")
    file.write("""//defines a genaric File Handler

#ifndef FileHandler_h
#define FileHandler_h

#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

	//gets the contents of a file
	const char* """ + progName + """_FileHandler_ReadFile(const char* filepath);
	//checks if two strings match
	bool """ + progName + """_FileHandler_StringMatch(const char* string1, const char* string2);

#ifdef __cplusplus
}
#endif

#endif""")

#main entry || writes the file handler
WriteHeaderFileHandler()
WriteWindowFileHandler()
WriteMacFileHandler()
WriteLinuxFileHandler()