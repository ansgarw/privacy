This repo contains the data used for "The Market for Data Privacy" by Tarun Ramadorai, Antoine Uettwiller and Ansgar Walther.

The published data consists of privacy policies, attributes of those policies, 
and measures of third-party sharing behavior
for the sample of firms from Compustat US used in the paper.

The Python code allows users to scrape and clean similar data 
for use in research on other firms and institutions in English-speaking countries.


# Published Data

Our data is indexed by websites, which can be merged onto the Compustat US data using the *weburl* field in WRDS. 
There are 3 data files.

### 1. Policy text

The file *output.json* contains the scraped text of each firm's privacy policy, which is saved as a list of paragraphs.
It further contains a lemmatized version of each policy, which is saved as a nested list: 
one list of lemmas for each paragraph. 

The text has been preprocessed... TODO describe

The following examples show how to extract information from this file using Python:

```python

import json
with open('output.json','r') as f:
  output = json.load(f)

```

### 2. Policy attributes

The file *attributes.csv* contains the policy attributes used in the paper, which are... TODO describe

### 3. Third-party sharing behavior



# Citation

If you use either the code or the data, please cite our paper:

```
@article{ramadorai2019market,
  title={The Market for Data Privacy},
  author={Ramadorai, Tarun and Walther, Ansgar and Uettwiller, Antoine},
  year={2019},
  publisher={CEPR Discussion Paper No. DP13588}
}
```
