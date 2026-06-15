import re

INPUT_FILE = "all_servers.txt"

def clean_line(line: str) -> str:
    # 1. &amp; -> &
    line = line.replace("&amp;", "&")
    # 2. حذف & اضافه قبل از #
    line = re.sub(r'&+#', '#', line)
    # 3. حذف پارامترهای خالی مثل ?path=# , ?path=/?ed=2560&# و ... 
    line = re.sub(r'\?[^=#]*=#', '#', line)
    # 4. حذف ? تنهای قبل از #
    line = re.sub(r'\?#', '#', line)
    return line

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("all_servers.txt not found")
    exit(0)

cleaned = [clean_line(line) for line in lines]

with open(INPUT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(cleaned))

print(f"✅ Cleaned {len(cleaned)} configs")