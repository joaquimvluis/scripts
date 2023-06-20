from freeplane import Mindmap, Node
import re
import os

txt_file_path= './example.txt'

with open(txt_file_path, 'r') as fp:
    lines = fp.readlines()

pattern = re.compile('\s{4}')
prev_level = 0
current_level = 0
map = []
for line in lines:
    if line == '':
        continue
    tabs = re.findall(pattern, line)
    current_level = prev_level + len(tabs)
    text = line.strip()
    if current_level > prev_level:
        pass


mindmap_path = os.environ['MINDMAP_PATH']

# load mind map
mindmap = Mindmap(mindmap_path)
print(mindmap)

root = mindmap.rootnode
