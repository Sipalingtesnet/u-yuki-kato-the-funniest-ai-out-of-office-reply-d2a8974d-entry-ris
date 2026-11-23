import os

LINE = "Out of office. I've gone to find myself. If I find a better version, I'll be back. If not, this is goodbye."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)