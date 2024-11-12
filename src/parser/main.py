import requests

from bs4 import BeautifulSoup as BS4

import constants
import utils


def request_to_site(url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        utils.save_html("index.html", response.text)


def get_titles() -> list:
    html_content = utils.read_html("index.html")
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    h2_mt_0_content_all = [item.text for item in h2_mt_0_all]
    return h2_mt_0_content_all


def get_links() -> list:
    html_content = utils.read_html("index.html")
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    hrefs_content_all = [item.find("a").get("href") for item in h2_mt_0_all]
    return hrefs_content_all


def get_owners_info() -> list:
    html_content = utils.read_html("index.html")
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    p_mt_xs_mb_0 = div_col_md_8.find_all("p", {"class": "mt-xs mb-0"})
    p_mt_xs_mb_0_content_all = [item.text for item in p_mt_xs_mb_0]
    return p_mt_xs_mb_0_content_all


def get_resumes():
    titles = get_titles()
    owners_info = get_owners_info()
    links = get_links()
    
    cards = []
    
    for i in range(len(titles)):
        card = {
            "title": titles[i],
            "owner_info": owners_info[i],
            "links": constants.BASE_URL + links[i]
        }
        cards.append(card)
    
    for i in range(len(titles)):
        print(cards[i]["links"])
    

def main():
    # request_to_site(constants.JobPositionConstants.GOLANG_DEVELOPER)
    get_resumes()
    
    


if __name__ == "__main__":
    main()