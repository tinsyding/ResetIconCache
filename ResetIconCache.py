# Python程序，用于创建用于删除图标缓存的批处理文件

# 提示用户输入用户名）
username = input("请输入你的计算机用户名：")

# 带有用户名占位符的文本模板
batch_text = """
@echo off
echo Deleting Icon Cache...
del /f /q "C:\\Users\\[username]\\AppData\\Local\\IconCache.db"
echo Restarting Explorer...
taskkill /f /im explorer.exe
start explorer.exe
echo Done.
"""

# 将占位符替换为用户输入的用户名
batch_text = batch_text.replace("[username]", username)

# 将修改后的文本保存为'icon.bat'
with open("icon.bat", "w") as file:
    file.write(batch_text)