headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

# collect links to all json results on privacyscore
def get_json_links(list_ids):
    list_links = ['https://privacyscore.org/list/%d/' % i for i in list_ids]
    json_links = []
    for link in tqdm_notebook(list_links):
        # scrape list main page
        page_source = requests.get(link, headers=headers, timeout=5).content
        soup = BeautifulSoup(page_source, 'html.parser')

        # get links to results for individual sites in the list
        href = soup.find_all('a', href =True)
        links = [a['href'] for a in href if "site" in a['href'] 
                 and not 'blacklisted-sites-anchor' in a['href'] 
                 and not 'tags=websites' in a['href']]

        # add to list
        json_links.extend(["https://privacyscore.org"+link+"json/" for link in links]) 
    return json_links

# scrape json results from privacyscore
def get_json_content(json_link):
    # get the json content
    page_source = requests.get(json_link, headers=headers, timeout=5).content
    soup = BeautifulSoup(page_source, 'lxml')
    code = soup.find("pre")
    string ="".join([a.string for a in code.findChildren() if a.string!=None])
    dictionary = json.loads(string)
    
    # save output if we have got cookie data
    if 'cookie_stats' not in dictionary.keys():
        return False, None, None
    else: 
        # get the domain name and format for merge
        domain = soup.find("h2").get_text().split("\"")[1]
        domain = domain.replace('http://','').replace('https://','')
        if domain.endswith('/'): domain = domain.replace('/','')
        return True, domain, dictionary


