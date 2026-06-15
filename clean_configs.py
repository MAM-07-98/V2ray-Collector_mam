import re

INPUT_FILE = "all_servers.txt"
OUTPUT_FILE = "all_servers.txt"  # بازنویسی همان فایل

def clean_line(line: str) -> str:
    # جایگزینی &amp; با &
    line = line.replace("&amp;", "&")
    # حذف & اضافه قبل از # (مثلاً security=none&# -> security=none#)
    line = re.sub(r'&+#', '#', line)
    return line

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("all_servers.txt not found")
    exit(0)

cleaned = [clean_line(line) for line in lines]

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(cleaned))

print(f"✅ Cleaned {len(cleaned)} configs (replaced &amp; with &, removed stray & before #)")