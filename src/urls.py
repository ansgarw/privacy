from googleapiclient.discovery import build
from .utils import onward_links, unique

# google search
def googlePrivacy(dom, api_key, cse_id, **kwargs):
    if dom.startswith('www.'): site = dom.replace('www.','',1)
    else: site = dom
    search_term = 'privacy site:%s' % site
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        result = [item['link'] for item in res['items']]
    except Exception as e:
        return False, str(e)
    return True, result

# crawler
def crawlPrivacy(dom,clicks=2):
    # shallow crawl
    status, root_urls = onward_links(dom,dom)
    if not status:
        return False, "root crawl failed with error: " + root_urls
    
    # deep crawl
    urls = [root_urls]
    for i in range(clicks-1):
        old = urls[i]
        new = []
        for url in old:
            status, links =  onward_links(url,dom)
            if status: 
                new = list(set(new + links))
        urls.append(new)
        
    return True, urls

# filter
def filterPrivacy(urls):
    narrow = ['privacy','data','inform']
    wide = ['privacy', 'data', 'cookie', 'legal', 'compliance', 'polic', 'inform',
                  'statement', 'term', 'notice', 'note', 'declaration','condition','code']
    high = list(filter(lambda s: 'priva' in s.lower() and 'polic' in s.lower(),urls))
    med  = list(filter(lambda s: any(x in s.lower() for x in narrow), urls))
    low  = list(filter(lambda s: any(x in s.lower() for x in wide), urls))
    ranked = unique(high + med + low)
    return ranked