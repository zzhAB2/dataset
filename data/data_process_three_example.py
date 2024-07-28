

import json
from tqdm import tqdm
import codecs

rel_set = set()

all_data= []
train_data = []
dev_data = []
test_data = []

len1=0
count=0
n=600

with open('all_data.json',encoding='utf-8') as f:
    for l in tqdm(f):
        a = json.loads(l)
        if not a['spo_list']:
            continue
        line = {
                'text': a['text'].lstrip('\"').strip('\r\n').rstrip('\"'),
                'triple_list': [(i['subject'], i['predicate'], i['object']) for i in a['spo_list'] if i['predicate'] != 'None']
               }
        if not line['triple_list']:
            continue
        all_data.append(line)
        for rm in a['spo_list']:
            if rm['predicate'] != 'None':
                rel_set.add(rm['predicate'])

        if len(line['text']) > n:
            print(line['text'])
            count += 1
        if len(line['text']) > len1:
            len1 = len(line['text'])
print(len(all_data))
print(len1)
print(count)
print('----------------------------------------')

len1=0
count=0
with open('train_data.json',encoding='utf-8') as f:
    for l in tqdm(f):
        a = json.loads(l)
        if not a['spo_list']:
            continue
        line = {
                'text': a['text'].lstrip('\"').strip('\r\n').rstrip('\"'),
                'triple_list': [(i['subject'], i['predicate'], i['object']) for i in a['spo_list'] if i['predicate'] != 'None']
               }
        if not line['triple_list']:
            continue
        train_data.append(line)
        for rm in a['spo_list']:
            if rm['predicate'] != 'None':
                rel_set.add(rm['predicate'])

        if len(line['text']) > n:
            print(line['text'])
            count += 1
        if len(line['text']) > len1:
            len1 = len(line['text'])

print(len(train_data))
print(len1)
print(count)

print('----------------------------------------')
len1=0
count=0
with open('dev_data.json',encoding='utf-8') as f:
    for l in tqdm(f):
        a = json.loads(l)
        if not a['spo_list']:
            continue
        line = {
                'text': a['text'].lstrip('\"').strip('\r\n').rstrip('\"'),
                'triple_list': [(i['subject'], i['predicate'], i['object']) for i in a['spo_list'] if i['predicate'] != 'None']
               }
        if not line['triple_list']:
            continue
        dev_data.append(line)
        for rm in a['spo_list']:
            if rm['predicate'] != 'None':
                rel_set.add(rm['predicate'])

        if len(line['text']) > n:
            print(line['text'])
            count += 1
        if len(line['text']) > len1:
            len1 = len(line['text'])
print(len(dev_data))
print(len1)
print(count)

print('----------------------------------------')
len1=0
count=0
with open('test_data.json',encoding='utf-8') as f:
    for l in tqdm(f):
        a = json.loads(l)
        if not a['spo_list']:
            continue
        line = {
                'text': a['text'].lstrip('\"').strip('\r\n').rstrip('\"'),
                'triple_list': [(i['subject'], i['predicate'], i['object']) for i in a['spo_list'] if i['predicate'] != 'None']
               }
        if not line['triple_list']:
            continue
        test_data.append(line)
        for rm in a['spo_list']:
            if rm['predicate'] != 'None':
                rel_set.add(rm['predicate'])


        if len(line['text']) > n:
            print(line['text'])
            count += 1
        if len(line['text']) > len1:
            len1 = len(line['text'])
print(len(test_data))
print(len1)
print(count)

id2predicate = {i:j for i,j in enumerate(sorted(rel_set))}
predicate2id = {j:i for i,j in id2predicate.items()}



with codecs.open('rel2id.json', 'w', encoding='utf-8') as f:
    json.dump([id2predicate, predicate2id], f, indent=4, ensure_ascii=False)

with codecs.open('all_triples.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=4, ensure_ascii=False)

with codecs.open('train_triples.json', 'w', encoding='utf-8') as f:
    json.dump(train_data, f, indent=4, ensure_ascii=False)

with codecs.open('dev_triples.json', 'w', encoding='utf-8') as f:
    json.dump(dev_data, f, indent=4, ensure_ascii=False)

with codecs.open('test_triples.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, indent=4, ensure_ascii=False)