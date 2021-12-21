import requests

need_cites = []

def scrape_page(url):

    page = requests.get(url) #<-- returns unparsed source code

    from bs4 import BeautifulSoup
    # print(BeautifulSoup)

    soup = BeautifulSoup(page.content, "html.parser")

    child_soup = soup.find_all('span')
    inner_text = 'citation needed'
    cite_count = 0
   
    for i in child_soup:
        if i.string == inner_text:
            p_text = i.find_parents("p")
            print(str(p_text)[4:130], "...")
            need_cites.append(p_text)
            
            cite_count += 1

    print("Number Cites Needed", len(need_cites))
    count_citations(need_cites)

def count_citations(cites_list):
    num_cites = len(cites_list)
    print(f"There are {num_cites} passages on the page that need citations.")

scrape_page("https://en.wikipedia.org/wiki/Roller_coaster")
