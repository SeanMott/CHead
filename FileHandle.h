//defines a file handler plus some string control

#ifndef FileHandle_h
#define FileHandle_h

#ifdef __cplusplus
extern "C" {
#endif

#include "Logger.h"

#include <string.h>
#include <stdio.h>
#include <stdbool.h>

//opens a file
const char* FileHandle_OpenFile(const char* filepath);
//writes a file

//checks if a string is the same as the other
bool FileHandle_StringMatch(const char* str1, const char* str2);
//return the end of a string || taken from NetHack || Link: https://github.com/NetHack/NetHack/blob/NetHack-3.7/src/hacklib.c
char* FileHandle_GetEndOfString(register char* str);
//concats a char to a string (it's adorable) || taken from NetHack || Link: https://github.com/NetHack/NetHack/blob/NetHack-3.7/src/hacklib.c
char* FileHandle_StrKitten(char* str, char c);

//differnt builds
#define Window_Build

const char* FileHandle_OpenFile(const char* filepath)
{
    FILE* file;
	char* text = 0;
	long length;

	file = fopen(filepath, "rb");
	if (!file)
	{
		LogData("Error: File Handler || Failed to open file at: %s\n", filepath);
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

//writes a file

bool FileHandle_StringMatch(const char* str1, const char* str2)
{
    return (strcmp(str1, str2) == 0 ? true : false);
}

char* FileHandle_GetEndOfString(register char* str)
{
    while (*str)
        str++;
    return str;
}

char* FileHandle_StrKitten(char* str, char c)
{
    char *p = FileHandle_GetEndOfString(str);

    *p++ = c;
    *p = '\0';
    return str;
}

#endif

#define Mac_Build
#endif

#define Linux_Build
#endif

#ifdef __cplusplus
}
#endif

#endif