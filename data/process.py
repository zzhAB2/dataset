
import json
from torch import nn
c=nn.BatchNorm3d
import pandas as pd
count1=0
with open('Normal_triples.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for idx, d in enumerate(data):
        pattern = d['triple_list']
        count1+=len(pattern)
    print(f'Normal:',count1)

count2=0
with open('EPO_triples.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for idx, d in enumerate(data):
        pattern = d['triple_list']
        count2+=len(pattern)
    print(f'EPO:',count2)

count3=0
with open('SEO_triples.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for idx, d in enumerate(data):
        pattern = d['triple_list']
        count3+=len(pattern)
    print(f'SEO:',count3)

count4=0
with open('SOO_triples.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for idx, d in enumerate(data):
        pattern = d['triple_list']
        count4+=len(pattern)
    print(f'SOO:',count4)

# c=[]
# with open('train_triples.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     for idx, d in enumerate(data):
#         pattern = d['triple_list']
#         for i in pattern:
#             c.append(i)
# with open('all_triples_notext.json', 'w', encoding='utf-8') as f:
#     f.write(str(c))
