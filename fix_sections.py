
with open('sections.py', encoding='utf-8') as f:
    content = f.read()

marker = 'def render_cv() -> None:'
idx1 = content.find(marker)
idx2 = content.find(marker, idx1 + 1)

if idx2 == -1:
    print('ERROR: second render_cv not found')
else:
    new_content = content[:idx1] + content[idx2:]
    with open('sections.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done. Total lines:', new_content.count('\n'))
