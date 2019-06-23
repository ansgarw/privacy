from .utils import get_paragraphs, get_tokens, get_lemmas

# download first valid policy from a ranked list of urls 
def findPolicy(ranked, **kwargs):
    for url in ranked:        
        if not url.endswith('.pdf'):
            pars = get_paragraphs(url,**kwargs)
            if 'privacy' in ' '.join(pars).lower(): 
                return True, pars, url
    return False, None, None

# clean up downloaded policy
def cleanPolicy(policy):
    tokens = [get_tokens(par) for par in policy]
    lemmas = [get_lemmas(par) for par in tokens]
    return tokens,lemmas
