This repo contains the data and code used for our research paper: "[The Market for Data Privacy](https://www.ssrn.com/abstract=3352175)" by Tarun Ramadorai, Antoine Uettwiller and Ansgar Walther. 

The easiest way to see the structure of our data and Python code is to look at 
the Jupyter notebooks `demoData.ipynb` and `demoCode.ipynb`. 

The data consists of 3 files
1. The privacy attributes of all US firms in our sample in `data/attributes.csv`. This data contains identifiers `gvkey` that can be used to merge it with Compustat data, and `weburl` for the website of each firm.
2. The full text of all privacy policies we found in this sample is in `data/policies.json`. Each policy is saved as a list of paragraphs. This data has `weburl` identifiers.
3. The evaluations of a legal expert for a smaller sample of policies are in `data/expert.csv`. This data has 
Details of expert's criteria are in the paper.
These evaluations form the basis of our legal clarity index. This data has `weburl` identifiers.

The code consists of 3 Python modules 
1. `src/urls.py` contains functions that find candidate URLs for privacy policies, using a root website (such as 'www.aa.com') as an input.
2. `src/text.py` 

The published data consists of privacy policies, attributes of those policies, 
and measures of third-party sharing behavior
for the sample of firms from Compustat US used in the paper.

The Python code allows you to scrape and clean similar data 
for use in research on other firms and institutions in English-speaking countries.

If you use this, please cite our paper (see bibtex below).

# Published Data

Our data is indexed by websites, which can be merged onto the Compustat US data using the *weburl* field in WRDS. 
There are 3 data files.

### 1. Policy text

The file *output.json* contains the scraped text of each firm's privacy policy, which is saved as a list of paragraphs.
It further contains a lemmatized version of each policy, which is saved as a nested list: 
one list of lemmas for each paragraph. 

The text and lemmas have been preprocessed... TODO describe

The following examples show how to extract information from this file using Python:

```python

import json
with open('output.json','r') as f:
    output = json.load(f)

# example: american airlines
example_url = 'www.aa.com'

# get first 2 paragraphs of text
print(output[example_url][policy][0:2]

# get the equivalent lemmas
print(output[example_url][lemmas][0:2]
```

### 2. Policy attributes

The file *attributes.csv* contains the policy attributes used in the paper, which are... TODO describe

### 3. Expert evaluation

The file *expert.csv* contains 
the evaluations of a legal expert of a sample of policies. 
Details of expert's criteria are in the paper.
These evaluations form the basis of our legal clarity index.

### 4. Third-party sharing behavior

The file *tpsharing.csv* contains the measures of third-party sharing used in the paper. 
This is based on measurements we did on *privacyscore.org*, which in turn uses the OpenWPM
crawler developed by Steven Englehardt and Arvind Narayanan (see: https://github.com/mozilla/OpenWPM)

# Code

The easiest way to use our code is to run the Jupyter notebook *demo.ipynb*, and adapt the demo for your needs.

We provide Python scripts (saved in *python*) that scrape privacy policies from arbitrary lists of websites, 
clean them, and calculate their attributes. 
We also provide automated classifiers (saved in *clfs*)
that are based on our expert evaluation and 
produce a legal clarity index.

We are still working on end-to-end code that will allow you to measure third-party behavior
using OpenWPM as a dependency. Bear with us! 
For now, we publish code that scrapes results from lists
of urls submitted to *privacyscore.org*, as we did for the paper.
You can [submit your own list here](https://privacyscore.org/list/create/) 
and use our code once your list has been scanned.

### Setup 

To run the part of the code that performs an automated Google search, you will need credentials 
for Google's Custom Search Engine. In particular, you need a Search Engine ID and an API Key. 
To set this up with your Google account, 
[follow the instructions here](https://developers.google.com/custom-search/v1/overview). 
For more than 100 queries in a day, Google will charge you $5 per 1000 queries, 
but first-time users get 
free credit (enough to write our paper, for example).

We use various Python dependencies... TODO make a list or binder

# Citation

```
@article{ramadorai2019market,
  title={The Market for Data Privacy},
  author={Ramadorai, Tarun and Walther, Ansgar and Uettwiller, Antoine},
  year={2019},
  publisher={CEPR Discussion Paper No. DP13588}
}
```
