import os
import re
import json

db_path = './dataset'
asterixes = re.compile('^[*]+$')
spaces = re.compile(r"\s*\n")
file_name = re.compile('LISA[0-9][.]+')

docs = []
#iterate over documents in file
for file in os.listdir(db_path):
    filepath = os.path.join(db_path, file)
    f = open(filepath, 'r')

    #check if file is relevant
    if file_name.match(file):
        print (file)
        m_file = list(f)

        new_doc = {}
        docID = 0
        docName = ''
        docCont = ''
        is_num = False      # is line contains doc ID
        is_name_next = False     # is line contains doc Name
        is_cont_next = False     # is line contains doc Content

        #iterate over document
        for m_line in m_file:
            # try to extract docID
            if m_line[0:8] == 'Document':
                is_num = True
                docID = int((m_line.split())[1])
                continue

            if is_num and spaces.match(m_line):
                is_num = False
                is_cont_next = True
                continue

            if is_num:
                docName += m_line[:-1] + ' ' # remove new_line and add space
                continue

            if asterixes.match(m_line):
                is_cont_next = False
                print(docID)
                new_doc.update({'docID':docID})
                new_doc.update({'docName':docName})
                new_doc.update({'docCont':docCont})
                docs.append(new_doc)
                new_doc = {}
                docName = ''
                docCont = ''
                continue

            if is_cont_next:
                docCont += m_line[:-1] + ' ' # remove new_line and add space
                continue
    f.close()

output_f = open('./dataset.json', 'w')
output_f.write(json.dumps(docs))
output_f.close
