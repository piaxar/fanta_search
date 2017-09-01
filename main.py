import os
import re

db_path = './dataset'
prog = re.compile('^[*]+$')

def main():
    words = []
    for file in os.listdir(db_path):
        print (file)
        filepath = os.path.join(db_path, file)
        f = open(filepath, 'r')
        if (file!='.DS_Store' and file!='preprocessed_docs'):
            m_file = list(f)
            for foo in m_file:
                m_word = foo.split()
                for fu in m_word:
                    words.append(fu)
        f.close()

    filepath = os.path.join(db_path, 'preprocessed_docs')
    f = open(filepath, 'w')
    docs = []
    new_doc = []
    for word in words:
        new_doc.append(word)
        if word == 'Document':
            new_doc.remove(word)
            docs.append(new_doc)
            new_doc = []
        if prog.match(word):
            new_doc.remove(word)
    docs.append(new_doc)
    for doc in docs:
        for word in doc:
            f.write(word+"#")
        f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
