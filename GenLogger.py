#genarates a C/C++ logger

import sys
import os

#args formate || define name for configs, prog name for logging
#example || python GenLogger.py SMOK Smok
#example || python GenLogger.py GL Glfix

defineName = sys.argv[1]
progName = sys.argv[2]

os.makedirs("includes", exist_ok= True)
log = open("includes/Logger.h", "w+")
log.write("//defines a logger for " + progName + """

#ifndef Logger_h
#define Logger_h

#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>

#define LogMessage(message) printf(\"%s\\n\", message);

#ifdef """ + defineName + """_RELEASE

#define LogWarning(code, message)
#define LogError(code, message)
#define LogFatalError(code, message) printf(\"""" + progName + """ Fatal Error: %s || %s\\n\", code, message); getchar(); exit(1);

#define LogData(formate, ...)
#define LogFatalData(formate, ...) printf(formate, __VA_ARGS__); getchar(); exit(1);

#endif

#ifdef """ + defineName + """_DIST

#define LogWarning(code, message)
#define LogError(code, message)
#define LogFatalError(code, message) exit(1);

#define LogData(formate, ...)
#define LogFatalData(formate, ...) printf(formate, __VA_ARGS__); exit(1);

#endif

#ifdef """ + defineName + """_DEBUG

#define LogWarning(code, message) printf(\"""" + progName + """ Warning : %s || %s\\n", code, message);
#define LogError(code, message) printf(\"""" + progName + """ Error : %s || %s\\n", code, message);
#define LogFatalError(code, message) printf(\"""" + progName + """ Fatal Error: %s || %s\\n", code, message); getchar(); exit(1);

#define LogData(formate, ...) printf(formate, __VA_ARGS__);
#define LogFatalData(formate, ...) printf(formate, __VA_ARGS__); getchar(); exit(1);

#endif

#ifndef LogWarning(code, message)
#define LogWarning(code, message)
#endif
#ifndef LogError(code, message)
#define LogError(code, message)
#endif
#ifndef LogFatalError(code, message)
#define LogFatalError(code, message)
#endif
#ifndef LogData(formate, ...)
#define LogData(formate, ...)
#endif
#ifndef LogFatalData(formate, ...)
#define LogFatalData(formate, ...)
#endif

#endif""")