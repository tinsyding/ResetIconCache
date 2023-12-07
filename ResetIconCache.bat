
@echo off
echo Deleting Icon Cache...
del /f /q "C:\Users\[yourusername]\AppData\Local\IconCache.db"
echo Restarting Explorer...
taskkill /f /im explorer.exe
start explorer.exe
echo Done.