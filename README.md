# sentiment_analysis
Source code to assess sentiments and plot them according to a dataset through messages.

**Note:** You need to require a dataset containing messages or phrases.You need to require a dataset containing messages or phrases.

## Create and install the environment

``` bash

$ conda create -n sentiment python=3.8
$ conda activate sentiment
$ pip install spanish_sentiment_analysis
$ pip install numpy scipy scikit-learn==0.19.2 ipython
$ conda install pandas matpllotlib
```
## Result
If the program ran correctly, a graph will be displayed showing how many messages were positive, how many negative and how many neutral. In addition to saving in a csv file (result.csv) with the respective value of the sentiment.

![image](https://github.com/jeanaray13/sentiment_analysis/blob/main/Bar%20chart%20result.png)
