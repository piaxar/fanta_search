import json
docs = []

# open dataset
with open('dataset.json') as data_file:
    docs = json.load(data_file)

while True:
    doc = int(input("docID: "))
    print (docs[doc-1])
