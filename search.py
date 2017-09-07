import json
import indexer as ind
import operator

def main():
    index = {}

    with open('index.json') as data_file:
        index = json.load(data_file)

    while True:
        query = input("Search query: ")
        if query == 'exit()':
            break
        else:
            print (search(index, query))
    #print (list(index.items())[0])

def search(index, query):
    # normalizing query
    query = query.lower()
    m_query = query.split()
    ind.tokenize(m_query)
    filtered_query = ind.stopwords_rem(m_query)
    ind.stem(filtered_query)

    filtered_query = sorted(set(filtered_query))
    print (filtered_query)

    # collect all occurances of terms
    all_docIDs = []
    for term in filtered_query:
        if index.get(term):
            all_docIDs.extend(index[term])

    # found any occurances
    if len(all_docIDs) > 0:
        # table for relevant-sorted search results
        relevance_table = {}
        # table with key as docID and value as number of occurances
        for docID in all_docIDs:
            if not relevance_table.get(docID):
                relevance_table[docID] = 1
            else:
                relevance_table[docID] += 1

        # sort relevance table by number of occurances
        sorted_ids = []
        sorted_d = sorted(relevance_table.items(), key=operator.itemgetter(1),reverse=True)
        print (sorted_d)
        for i in sorted_d:
            sorted_ids.append(i[0])

        # print results
        # need to replace with return list of indexes
        #print ("Found " + str(len(sorted_ids))+" documents.")
        #print ("Document ids, sorted by relevance:")
        return ("sorted_ids")

    # no occurances found
    else:
        return ([-1])


if __name__ == '__main__':
    main()