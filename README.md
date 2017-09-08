Greeting!
======
Here is a project for Information retrieval course in Innopolis University Fall 2017.

Program allows to you to perform Boolean retrieval search quries operations on [LISA dataset](https://github.com/piaxar/fanta_search/tree/master/dataset).

## Setting up environment
### Virtual environment setup
We suggest to install project into virtual environment. Your virtual environment should support python version 3.6 (wasn't tested on lower version, but must work on at least python 3.4). 
If you have conda installed, please refer to [this page](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) to set up your environment.
If you don't have conda, then use virtualenv. For example [this tutorial](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3) on how to install and use virtualenv. 
### Cloning code
Activate virtual environment, cd into project directory and clone code. For example:
```sh
source activate project_virtual_environment_name
cd project_directory
git clone https://github.com/piaxar/fanta_search.git
```
This code works for me with conda installed on Mac.
### Installing libraries
This project uses nltk library. To install it do this:
```sh
pip install -U nltk
```
After library will be installed, you need to download resources. Run python shell:
```sh
python
```
then run this code and follow the instructions.
```python
import nltk
nltk.download()
```
To check installation, run this code and compare output:
```python
>>> from nltk.corpus import brown
>>> brown.words()
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
```
## Data preprocessing
We need to build an index from raw data.
### Parsing documents
Run this code in terminal in project folder:
```sh
python raw_to_json.py
```
Your will see something similar:

![pic](https://github.com/piaxar/fanta_search/blob/master/pics/preprocessing.png "preprocessing")

This code will run python script that reads raw documents (numbers in picture are processed document ids), parse them and write all parsed documents in folder "/processed_data" in single json file called "dataset.json"

dataset.json has format : \[{"docID" : document_id,
                              "docName": document_name,
                              "docCont": document_content}, ... \]
                              
It contains all documents from dataset.

### Indexing documents
Run this code in terminal in project folder:
```sh
python indexer.py
```
You will see something like this:

![pic](https://github.com/piaxar/fanta_search/blob/master/pics/indexing.png "indexing")

Running this may take some time. 

This script takes dataset.json file, performs tokenizing, stopwords removal, stemming on each document. Then take each lemma and build inverse document index for each word. Index is saved into "project_dir/processed_data/index.json"

index.json has format: {"word_lemma":[docID1, docID2, ...], ...}

So index.json contains a dictionary where keys are lemmas and values are lists of docIDs. Also docIDs may repeat, this redundancy was left to make tf-idf, but wasn't used.

## Searching
Finally , when setting up environment and preprocessing is over, you can start searching. 

Run this code to start:
```sh
python search.py
```
When data loading will be over, you will see main menu:
![menu](https://github.com/piaxar/fanta_search/blob/master/pics/main_menu.png "menu")

Type s - for search, d - for searching document by id, h - for help and e - to exit.
### Performing search
You can easily search term by typing it:
![search](https://github.com/piaxar/fanta_search/blob/master/pics/search.png "search")

But usually we are not interested in searching one term. As we said, you can run boolean queries search, like this:
```python
term1 & term2 | term3
```
For example:
![search_and](https://github.com/piaxar/fanta_search/blob/master/pics/search_atomenergy.png "search_and")

Another example:
![search_and_not](https://github.com/piaxar/fanta_search/blob/master/pics/search_atomnotenergy.png "search_and_not")

#### Syntax
You can use round brackets to make your queries more complicated.

Operator "__&__" is binary logical operator __AND__.

Operator "__|__" is binary logical operator __OR__.

Operator "__~__" is unary logical operator __NOT__.

__Valid queries examples:__

"term1 & term2", "term1 & (term3 | term2)", "~term1 & ~(term2 | ~term3)", etc.
#### Attention!
Searching is performing only on boolean queries, so queries with wrong structure, typos and other mistakes will be treated incorrectly. (Mistakes handling is in process)
### Documents search
List with ids of documents is useless, so you can view content of the document by simply typing document id in document finding section:
![doc_search](https://github.com/piaxar/fanta_search/blob/master/pics/document_search.png "doc_search")

## Credits
Thank you for viewing my work. Feel free to contact me.

Contacts can be easily found in github user's bio.

