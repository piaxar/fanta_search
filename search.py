import json
import indexer as ind
import operator
import expression_parser as exp
from nltk.stem.snowball import EnglishStemmer

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
            print ("\tType your query, for example 'term1 & term2 & ~term3'")
            print ("\tFor help, pleas refer to HELP opiton in main menu\n")
            query = input("Query:\t")
            print ("\n\tFOUND:")
            print ("\t"+ str(search(index, query)))
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

def search(index, query):
    # normalizing query
    query = query.lower()
    parser = exp.ExpresisonParser()
    ast = parser.parse(query)
    return getChild(ast)

def getChild(node):
    if type(node) is exp.Term:
        return getDocs(node.term)
    else:
        left_set = getChild(node.left)
        result = []
        if node.operator == '~':
            # extract given indices from set
            for i in all_docIDs:
                if i not in left_set:
                    result.append(i)
            return result
        else:
            right_set = getChild(node.right)
            if node.operator == '&':
                for i in right_set:
                    if i in left_set:
                        result.append(i)
                return result
            elif node.operator == '|':
                result.extend(left_set)
                for i in right_set:
                    if i not in left_set:
                        result.append(i)
                return result

def getDocs(term):
    search_term = stemmer.stem(term)
    allDocs = index.get(search_term)
    reduced_list = []
    if type(allDocs) is list:
        for i in allDocs:
            if i not in reduced_list:
                reduced_list.append(i)
    return reduced_list

if __name__ == '__main__':
    main()
