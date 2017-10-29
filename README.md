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
![search](https://github.com/piaxar/fanta_search/blob/master/pics/search.png "search")

As you can see, search returns you top 20 most relevant articles along with their scores. 

### Evaluating
To perform evaluating, I choose searching phrase to be "Information service".
Next, I selected first 100 articles (this approach is random, NO information about content was known beforehand), and marked as relevant and not relevant:
SCREENSHOT

Totally, I get **19 relevant** documents and **81 not relevant**.

After running searching query, I get these results:
SCREENSHOT

Not relevant results are marked as red:
SCREENSHOT

#### Confusion matrix
Screenshot

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


## Credits
Thank you for viewing my work. Feel free to contact me.

Contacts can be easily found in github user's bio.

