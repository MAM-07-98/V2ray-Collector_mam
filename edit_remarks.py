import re
import sys

INPUT_FILE = "all_servers.txt"

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: File {INPUT_FILE} not found.")
    sys.exit(1)

if not lines:
    print(f"File {INPUT_FILE} is empty, no changes made.")
    sys.exit(0)

def has_remark(config):
    """Check if config already has a remark (anything after #)"""
    return '#' in config

def get_protocol(config):
    match = re.match(r'^(\w+)://', config)
    if match:
        return match.group(1).upper()
    return "UNKNOWN"

new_lines = []
for idx, line in enumerate(lines, start=1):
    line = line.strip()
    if not line:
        continue

    if has_remark(line):
        # اگر ریمارک داشت، دست نزن
        new_lines.append(line)
        continue

    # فقط برای لینک‌های بدون ریمارک، یکی اضافه کن
    protocol = get_protocol(line)
    new_remark = f"#{protocol}_Config_{idx}"
    new_line = f"{line}{new_remark}"
    new_lines.append(new_line)

with open(INPUT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f"✅ Added remarks to {len(new_lines)} configs (only those without existing remark)")