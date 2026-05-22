# ЮНУСОВ ПАВЕЛ ИИАД 1
import sys
import platform

os_name = platform.system()

python_version = sys.version

info_line = f"OS info is {os_name} Python version is {python_version}"

with open("os_info.txt", "w", encoding="utf-8") as file:
    file.write(info_line)

print("Файл os_info.txt успешно создан!")
