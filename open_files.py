import json
import random


with open('data/term_merch.json', 'r') as file:
    json_data = file.read()
    
term = json.loads(json_data)
terminal = random.choice(term)

