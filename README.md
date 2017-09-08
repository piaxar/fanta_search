Greeting!
======
Here is a project for Information retrieval course in Innopolis University Fall 2017.

Program allows to you to perform Boolean retrieval search quries operations on [LISA dataset](https://github.com/piaxar/fanta_search/tree/master/dataset).

## Setting up environment
### Virtual environment setup
I suggest to install project into virtual environment. Your virtual environment should support python version 3.6 (wasn't tested on lower version, but must work on at least python 3.4). 
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
This code will run python script that reads raw documents, parse them and write all parsed documents in folder "/processed_data" in single json file called "dataset.json"

dataset.json has format : \[{"docID" : document_id,
                              "docName": document_name,
                              "docCont": document_content}, ... \]
                              
It contains all documents from dataset.

### Indexing documents
Run this code in terminal in project folder:
```sh
python indexer.py
```
Running this may take some time. 

This script takes dataset.json file, performs tokenizing, stopwords removal, stemming on each document. Then take each lemma and build inverse document index for each word. Index is saved into "project_dir/processed_data/index.json"

index.json has format: {"word_lemma":[docID1, docID2, ...], ...}

So index.json contains a dictionary where keys are lemmas and values are lists of docIDs.Also docIDs may repeat, this redundancy was left to make tf-idf, but wasn't used.

## Searching
TODO
## Credits

