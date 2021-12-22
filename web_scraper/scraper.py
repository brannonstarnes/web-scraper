import requests

need_cites = []

def scrape_page(url):

    page = requests.get(url) #<-- returns unparsed source code

    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(page.content, "html.parser")
    span_soup = soup.find_all('span')
    inner_text = 'citation needed'
   
    for i in span_soup:
        if i.string == inner_text:
            p_text = i.find_parents("p")
            print(str(p_text)[4:130], "...")
            need_cites.append(p_text)
            
    _count_citations(need_cites)



def _count_citations(cites_list):
    num_cites = len(cites_list)
    print(f"There are {num_cites} passages on the page that need citations.")



scrape_page("https://en.wikipedia.org/wiki/Roller_coaster")
