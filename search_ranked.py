#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import indexer as ind
import operator
import expression_parser as exp
from nltk.stem.snowball import EnglishStemmer
import math

stemmer = None
parser = None
index = None
all_docIDs = []

def main():
    global stemmer, parser, index, all_docIDs

    index = {}

    parser = exp.ExpresisonParser()
    stemmer = EnglishStemmer()

    with open('./processed_data/index.json') as data_file:
        index = json.load(data_file)

    with open('./processed_data/dataset.json') as df:
        docs = json.load(df)

    for doc in docs:
        all_docIDs.append(doc.get("docID"))

    # main loop
    while True:
        command = input("Enter\t's' to search\
                            \n\t'd' to find document by id\
                            \n\t'h' for help\
                            \n\t'e' to exit\
                            \nCommand: ")
        if command == 'e':
            break
        elif command == 'h':
            print ("HELP")
            print ("\tFind all information on project's github page:")
            print ("\thttps://github.com/piaxar/fanta_search")
            input("\nPress 'enter' to continue")
        elif command == 's':
            print ("SEARCH")
            print ("\tType your query")
            print ("\tFor help, please refer to HELP opiton in main menu\n")
            query = input("Query:\t")
            print ("\n\tFOUND:")
            print ("\t{}\t-\t{}".format("doc id", "score"))
            for tup in search(query):
                print ("\t{}\t-\t{}".format(tup[0], tup[1]))
            input("\nPress 'enter' to continue")
        elif command == 'd':
            print ("DOCUMENT")
            print ("\tType document id (from search results)\n")
            query = int(input("DocID: "))
            if query in range(1, len(docs)+1):
                doc = docs[query - 1]
                if doc.get("docID") == query:
                    print ("\n\tFOUND:")
                    print ("\tDocID: " + str(doc.get("docID")) + \
                            "\n\n\tName: " + str(doc.get("docName")) + \
                            "\n\n\tContent: "+ str(doc.get("docCont")))
            else:
                print ("\n\tDocument with such id doesn't exist")
            input("\nPress 'enter' to continue")



    #print (list(index.items())[0])

def search(query, top_n = 20):
    # normalizing query
    query = query.lower()
    terms = query.split()
    
    N = 6004 #len(doc_ids)
    
    #removing stopwords
    terms = ind.stopwords_rem(terms)
    
    all_terms = [0] * len(terms)
    
    for i in range(len(terms)):
        all_terms[i] = stemmer.stem(terms[i])
    
    terms = list(set(all_terms))
    
    # sorting and counting tf for query
    query_vec = [all_terms.count(i) for i in terms]
    query_vec = [1.0 + math.log10(x) for x in query_vec]
    
    # creating vectors of documents with logarithmic tf
    doc_vecs = {}
    doc_freq = [0] * (len(terms))
    doc_ids = getDocKeys(terms)
    for doc_id in doc_ids:
        doc_vecs[doc_id] = [0] * (len(terms))
        
        for i in range(len(terms)):
            term_docs = index.get(terms[i])
            if term_docs.count(doc_id) != 0:
                doc_freq[i] += 1
            tf_score = 1+ math.log10(term_docs.count(doc_id)) if term_docs.count(doc_id) != 0 else 0
            doc_vecs[doc_id][i] = tf_score
    
    # appplying idf for query vector:
    for i in range(len(query_vec)):
        query_vec[i] = query_vec[i] * math.log10(N/doc_freq[i])
    
    #normalization for query vector:
    v = [x**2 for x in query_vec]
    norm_factor = math.sqrt(sum(v))
    v = [x/norm_factor for x in query_vec]
    query_vec = v 
        
    # normalizing document vectors
    for key, tfs in doc_vecs.items():
        v = [x**2 for x in tfs]
        norm_factor = math.sqrt(sum(v))
        v = [x/norm_factor for x in tfs]
        doc_vecs[key] = v
        
    # counting scores
    scores = {}
    for doc_id, vec in doc_vecs.items():
        score = 0
        for i in range(len(vec)):
            score += vec[i] * query_vec[i]
        scores[doc_id] = score

    return sorted(scores.items(), key=lambda x:x[1], reverse=True)[:top_n]


def getDocs(term):
    allDocs = index.get(search_term)
    reduced_list = []
    if type(allDocs) is list:
        for i in allDocs:
            if i not in reduced_list:
                reduced_list.append(i)
    return reduced_list

def getDocKeys(terms):
    result = []
    for q in terms:
        res = index.get(q)
        if type(res) is list:
            result+= res
    reduced_list = []
    for i in result:
        if i not in reduced_list:
            reduced_list.append(i)
    return reduced_list


if __name__ == '__main__':
    main()
