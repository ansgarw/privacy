This repo contains the data used for our research paper: "[The Market for Data Privacy](https://www.ssrn.com/abstract=3352175)" by Tarun Ramadorai, Antoine Uettwiller and Ansgar Walther. 

The published data consists of privacy policies, attributes of those policies, 
and measures of third-party sharing behavior
for the sample of firms from Compustat US used in the paper.

The Python code allows users to scrape and clean similar data 
for use in research on other firms and institutions in English-speaking countries.

If you use either the code or the data in your work, please cite our paper (see bibtex citation below).


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

### 3. Expert evaluation training data

The file *expert.csv* contains...

### 4. Third-party sharing behavior

The file *tpsharing.csv* contains the measures of third-party sharing used in the paper. 
This is based on measurements we did on *privacyscore.org*, which in turn uses the OpenWPM
crawler developed by Steven Englehardt and Arvind Narayanan (see: https://github.com/mozilla/OpenWPM)

# Code

The folder *src* contains python functions that allow you to scrape privacy policies, 
clean them, calculate their attributes. 

You can also calculate the legal clarity of these policies
using automated classifiers (saved in *clfs*)
that are based on our expert evaluation.

The Jupyter notebook *demo.ipynb* has a full demo. 

We are also working on end-to-end code that will allow you to measure third-party behavior
using OpenWPM as a dependency. 
For now, we publish code that scrapes results from *privacyscore.org*, as we did for the paper.

**Important:** To run the part of the code that performs an automated Google search, you will need credentials 
for Google's Custom Search Engine. To set this up with your Google account, follow the instructions
at: TODO 

# Citation

```
@article{ramadorai2019market,
  title={The Market for Data Privacy},
  author={Ramadorai, Tarun and Walther, Ansgar and Uettwiller, Antoine},
  year={2019},
  publisher={CEPR Discussion Paper No. DP13588}
}
```
