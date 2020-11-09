import json
from pprint import pprint

def open_file(file):
  with open(file) as f:
    data = json.load(f)
  return data

def picking(data):
  counters = {}
  for item in data['rss']['channel']['items']:
    for word in item['description'].lower().split():
      if len(word) < 6:
        continue
      if word not in counters:
        counters[word] = 1
      else:
        counters[word] += 1
  return counters

def top(counters):
  return sorted(counters.items(), key=lambda i: i[1], reverse=True)[:10]
  
pprint(top(picking(open_file('newsafr.json'))))