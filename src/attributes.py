import pandas as pd
from .utils import get_html
from .text import cleanPolicy
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from readcalc import readcalc
import nltk 
nltk.download('punkt')

# check if 'privacy' is visible on a website
def isVisible(url):
    status, html = get_html(url)
    
    if not status: 
        return False, False # did not find html (scraping error)
    
    soup = BeautifulSoup(html, features="lxml")
    data = soup.findAll(text=True)
    for x in data:
        if "privacy" in x.lower(): 
            return True, True # found html and 'privacy'
        
    return True, False # found html but not 'privacy'

# get gunning fog index for string text
def fogIndex(text):
    return readcalc.ReadCalc(text).get_gunning_fog_index()
    
# get length attributes
def policyLength(policy):
    paragraphs = len(policy)
    words = len(' '.join(policy).split(' '))
    return paragraphs, words

# get legal clarity index
def legalClarity(policies):
    docs = {}
    # transform for tdm 
    for dom in policies:
        tokens,lemmas = cleanPolicy(policies[dom])
        docs[dom] = ' '.join(sum(lemmas,[]))
    
    # make tdm
    vectorizer = TfidfVectorizer(ngram_range = (2,2), max_features=10000)
    X = vectorizer.fit_transform(docs.values())
    tdm = pd.DataFrame(X.toarray(),columns = vectorizer.get_feature_names(),index = docs.keys())
    
    # import expert evaluation: top good and bad terms
    expert = pd.read_csv('src/good_bad_list.csv')
    good = [term for term in expert['good'] if term in tdm.columns][0:100]
    bad = [term for term in expert['bad'] if term in tdm.columns][0:100]
    
    # weights on these terms in TDM
    wgood = tdm[good].sum(axis=1)
    wbad = tdm[bad].sum(axis=1)
    
    return {dom: wgood[dom] - wbad[dom] for dom in tdm.index}
