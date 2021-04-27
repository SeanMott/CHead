//defines a Logger

#ifndef Logger_h
#define Logger_h

#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif

//redefine this for your prog
#define PROG_NAME ""

#define LogMessage(message) printf("%s\n", message);

#ifdef FATAL_LOG_ONLY

#define LogWarning(code, message)
#define LogError(code, message)
#define LogFatalError(code, message) printf("%s Fatal Error: %s || %s\n", PROG_NAME, code, message); getchar(); exit(1);

#define LogData(formate, ...)
#define LogFatalData(formate, ...) printf(formate, __VA_ARGS__); getchar(); exit(1);

#endif

#ifdef FATAL_LOG_DATA_ONLY

#define LogWarning(code, message)
#define LogError(code, message)
#define LogFatalError(code, message) exit(1);

#define LogData(formate, ...)
#define LogFatalData(formate, ...) printf(formate, __VA_ARGS__); exit(1);

#endif

#ifdef LOG_ALL

#define LogWarning(code, message) printf("%s Warning : %s || %s\n", PROG_NAME, code, message);
#define LogError(code, message) printf("%s Error : %s || %s\n", PROG_NAME, code, message);
#define LogFatalError(code, message) printf("%s Fatal Error: %s || %s\n", PROG_NAME, code, message); getchar(); exit(1);

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

#ifdef __cplusplus
}
#endif

#endif