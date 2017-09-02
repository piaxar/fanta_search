import json
import re
import time

from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer

# global var-s
stemmer = EnglishStemmer()

def tokenize(word_list):
    for i in range(len(word_list)):
        word_list[i] = re.sub('[^0-9a-zA-Z]+', '', word_list[i])

def stopwords_rem(word_list):
    return [word for word in word_list if word not in stopwords.words('english')]

def stem(word_list):
    for i in range (len(word_list)):
        word_list[i] = stemmer.stem(word_list[i])

def add_to_index(word_list, docID, index):
    for word in word_list:
        if not index.get(word):
            index[word] = []
        index[word].append(docID)



def main():
    docs = []
    index = {}

    # open dataset
    with open('dataset.json') as data_file:
        docs = json.load(data_file)

    i = 0
    start_time = time.time()
    for document in docs:
        # dump every 500 iterations
        # uncoment if needed
        # i += 1
        # if i%500 == 0:
        #     print("--- %s seconds passed ---" % (time.time() - start_time))
        #     file_name = './index_{}.json'.format(i)
        #     output_f = open(file_name, 'w')
        #     output_f.write(json.dumps(index))
        #     output_f.close


        # get data and lowercase
        docID = document.get('docID')
        docName = document.get('docName').lower()
        docCont = document.get('docCont').lower() # cont stands for content

        # tokenizing
        word_list_name = docName.split()
        word_list_cont = docCont.split()
        tokenize(word_list_name)
        tokenize(word_list_cont)

        # stopwords removal
        filtered_words_name = stopwords_rem(word_list_name)
        filtered_words_cont = stopwords_rem(word_list_cont)

        # stemming
        stem(filtered_words_name)
        stem(filtered_words_cont)

        # index building
        add_to_index(filtered_words_name, docID, index)
        add_to_index(filtered_words_cont, docID, index)

        # logging
        print ('Doc '+str(docID) + ' has been indexed.')


    file_name = './index.json'
    output_f = open(file_name, 'w')
    output_f.write(json.dumps(index))
    output_f.close


if __name__ == '__main__':
    main()
