Greeting!
======
Here is a second part of project for Information retrieval course in Innopolis University Fall 2017.

Program allows to you to perform Ranked retrieval search quries operations on [LISA dataset](https://github.com/piaxar/fanta_search/tree/master/dataset).

## Setting up environment
Installation and preprocessing are described in [main branch](https://github.com/piaxar/fanta_search). 

## Searching
Finally, when setting up environment and preprocessing is over, you can start searching. 

Run this code to start:
```sh
python search_ranked.py
```
When data loading will be over, you will see main menu:
![menu](https://github.com/piaxar/fanta_search/blob/master/pics/main_menu.png "menu")

Type s - for search, d - for searching document by id, h - for help and e - to exit.
### Performing search
You can easily search term by typing it:
SCREENSHOT
![search](https://github.com/piaxar/fanta_search/blob/ranked_retrieval/pics/ranked_search.png "search")

As you can see, search returns you top 20 most relevant articles along with their scores. 

### Evaluating
To perform evaluating, I choose searching phrase to be "Information service".
Next, I selected 100 articles, then perform indexing. After labeling I marked them as relevant and not relevant. Process of indexing and labeling on screenshots:
![search](https://github.com/piaxar/fanta_search/blob/ranked_retrieval/pics/indexing100.png "indexing")
![search](https://github.com/piaxar/fanta_search/blob/ranked_retrieval/pics/labeling100.png "labeling")

Totally, I get **19 relevant** documents and **81 not relevant**.

#### Testing query
After running searching query, I get these results:
![search](https://github.com/piaxar/fanta_search/blob/ranked_retrieval/pics/ranked_search100.png "ranked_search")

Not relevant results are marked as red:
![search](https://github.com/piaxar/fanta_search/blob/ranked_retrieval/pics/search_marked.png "labels")

#### Confusion matrix
![search](https://github.com/piaxar/fanta_search/blob/ranked_retrieval/pics/confusion_matrix.png "confusion matrix")

#### Precision
Precision = true_positive/(true_positive + false_positive)

Precision = 14/(14+6) = **0.7**
#### Recall
Recall = true_positive/(true_positive + false_negatve)

Recall = 14/(14+5) = **0.736**
#### F1 score
F1 = 2*(precision * recall)/(precision + recall)

F1 = 2*(0.7 * 0.736)/(0.7 + 0.736) = **0.717**

### Code changes
Main changes happened in searching algorithm. 
Now searching method after filtering of query takes 6 steps:

Step 1
```python
    # sorting and counting tf for query
    query_vec = [all_terms.count(i) for i in terms]
    query_vec = [1.0 + math.log10(x) for x in query_vec]
```
Step 2
```python
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
```
Step 3
```python
    # appplying idf for query vector:
    for i in range(len(query_vec)):
        query_vec[i] = query_vec[i] * math.log10(N/doc_freq[i])
```
Step 4
```python
    #normalization for query vector:
    v = [x**2 for x in query_vec]
    norm_factor = math.sqrt(sum(v))
    v = [x/norm_factor for x in query_vec]
    query_vec = v 
```
Step 5
```python
    # normalizing document vectors
    for key, tfs in doc_vecs.items():
        v = [x**2 for x in tfs]
        norm_factor = math.sqrt(sum(v))
        v = [x/norm_factor for x in tfs]
        doc_vecs[key] = v
```
Step 6
```python
    # counting scores
    scores = {}
    for doc_id, vec in doc_vecs.items():
        score = 0
        for i in range(len(vec)):
            score += vec[i] * query_vec[i]
        scores[doc_id] = score
```
Then scores are sorted and top 20 returned.

## Credits
Thank you for viewing my work. Feel free to contact me.

Contacts can be easily found in github user's bio.

