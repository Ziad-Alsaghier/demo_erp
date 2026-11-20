import os
import re

files_to_check = ['index.html']
for root, dirs, files in os.walk('.'):
    if '_archive' in root: 
        continue
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            files_to_check.append(os.path.join(root, f).replace('\\', '/'))

print(f"Checking {len(files_to_check)} HTML files...")
errors = 0
checked_count = 0

for file_path in files_to_check:
    dir_name = os.path.dirname(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    for link in links:
        if link.startswith(('http://', 'https://', '#', 'javascript:', 'mailto:', 'data:')):
            continue
        clean_link = link.split('?')[0].split('#')[0]
        if not clean_link:
            continue
        resolved = os.path.normpath(os.path.join(dir_name, clean_link))
        checked_count += 1
        if not os.path.exists(resolved):
            print(f"BROKEN LINK in {file_path}: {link} -> {resolved}")
            errors += 1

print(f"Verification complete: checked {checked_count} relative links across {len(files_to_check)} files.")
if errors == 0:
    print("SUCCESS: 100% of internal links, styles, and scripts exist!")
else:
    print(f"FAILURE: {errors} broken links detected.")
