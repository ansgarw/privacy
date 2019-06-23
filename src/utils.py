import requests
import re
import enchant
from bs4 import BeautifulSoup
from urlparse import urljoin 
from boilerpipe.extract import Extractor
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
english_dict = enchant.Dict("en_US")       

# find onward links from a url
def onward_links(url,domain_name):
    status, html = get_html(url)
    if not status:
        return False, "html request failed with error: " + str(html)
    
    status, hrefs = find_all_links(html,domain_name)
    if not status:
        return False, "link extraction failed with error: " + str(hrefs)
        
    return True, hrefs

# download html code from a website
def get_html(url):
    try:
        if not (url.startswith('http://') or url.startswith('https://')): url='http://'+url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        html = requests.get(url, headers=headers, timeout=5).text
    except Exception as e:
        return False, e
    return True, html

# find all links in a html document
def find_all_links(html, domain_name):
    try:
        soup = BeautifulSoup(html, 'html.parser')
    
        #Get all the links (remove blanks and duplicates)
        hrefs = list(set(filter(None, [a['href'] for a in soup.find_all(href=True)])))
    
        #Remove email addresses and embed
        hrefs = [a for a in hrefs if (not "mailto:" in a and not 'embed?' in a)]
    
        #converting relative URL to absolute URL
        if not (domain_name.startswith('http://') or domain_name.startswith('https://')): 
            domain_name='http://'+domain_name
        for index in range(len(hrefs)):
            hrefs[index] = urljoin(domain_name, hrefs[index])
    
        #Remove '#' (not a different link)
        hrefs = [a.split('#')[0] for a in hrefs]
        
        # remove formatting characters that sneak in
        hrefs = [a.replace('\n','').replace('\r','').replace('\t','') for a in hrefs]
    
        #Keep only those with the domain name in it
        hrefs = [a for a in hrefs if domain_name in a]
        hrefs = list(set(hrefs))
    except Exception as e:
        return False, str(e)
    
    return True, hrefs

# unique list of links without changing order
def unique(url_list):
    seen = set()
    return [x for x in url_list if not (x in seen or seen.add(x))] 

# extract text from url and organise into paragraphs
def get_paragraphs(url,min_chars = 100):
    try:
        text = Extractor(extractor='KeepEverythingExtractor', url=url).getText().split('\n')
        pars = [par for par in text if len(par)>min_chars]
    except Exception as e:
        return []
    return pars

# tokenize a string
def get_tokens(string):
    # remove punctuation and digits
    newstr = re.sub(r'[^\w\s]','',string)
    newstr = ''.join(i for i in newstr if not i.isdigit())
    # tokenize 
    tokens = word_tokenize(newstr)
    # remove stop words
    tokens = [word.lower() for word in tokens if not word.lower() in stopwords.words('english')]
    # remove non english words
    tokens = [word for word in tokens if english_dict.check(word)]
    return tokens

# lemmatize list of tokens
def get_lemmas(tokens):
    lemmas = [WordNetLemmatizer().lemmatize(word) for word in tokens]
    # remove duplicate paragraphs from lemmas
    unique_lemmas = []
    for par in lemmas:
        if par not in unique_lemmas:
            unique_lemmas.append(par)
    lemmas = unique_lemmas
    return lemmas

   
