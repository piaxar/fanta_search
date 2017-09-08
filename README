0) setup virtualenv and move unzip project into virtualenv directory


pip install -U nltk

1) run raw_to_json.py
  this file reads raw documents, parse them and write all documents in folder
  processed_data in single json file called dataset.json
  dataset.json has format : [{"docID" : document_id,
                              "docName": document_name,
                              "docCont": document_content}, ... ]

2) run indexer.py
  this file takes dataset.json file, performs tokenizing, stopwords removal,
  stemming on each document. Then take each lemma and build inverse document index
  for each word. Index is saved into ./processed_data/index.json
  format of file index.json: {"word_lemma":[docID1, docID2, ...], ...}
  docIDs can repeat, this redundancy was left to make tf-idf, but wasn't used.
  running this may take some time

3) run search.py
  final working search engine
