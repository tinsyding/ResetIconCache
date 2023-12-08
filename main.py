username = input("Please enter your computer username: ")

batch_text = """
@echo off
echo Deleting Icon Cache...
del /f /q "C:\\Users\\[yourusername]\\AppData\\Local\\IconCache.db"
echo Restarting Explorer...
taskkill /f /im explorer.exe
start explorer.exe
echo Done.
"""

batch_text = batch_text.replace("[yourusername]", username)

with open("main.bat", "w") as file:
    file.write(batch_text)