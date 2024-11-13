import requests

from bs4 import BeautifulSoup as BS4

from parser import constants, utils
from parser import filters


def request_to_site(url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text


def get_titles(html_content) -> list:
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    h2_mt_0_content_all = [item.text for item in h2_mt_0_all]
    return h2_mt_0_content_all


def get_links(html_content) -> list:
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    hrefs_content_all = [item.find("a").get("href") for item in h2_mt_0_all]
    return hrefs_content_all


def get_owners_info(html_content) -> list:
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    p_mt_xs_mb_0 = div_col_md_8.find_all("p", {"class": "mt-xs mb-0"})
    p_mt_xs_mb_0_content_all = [item.text for item in p_mt_xs_mb_0]
    return p_mt_xs_mb_0_content_all


def get_resumes(html_content) -> list:
    titles = get_titles(html_content)
    owners_info = get_owners_info(html_content)
    links = get_links(html_content)
    
    cards = []
    
    for i in range(len(titles)):
        card = {
            "title": titles[i],
            "owner_info": owners_info[i],
            "links": constants.BASE_URL + links[i]
        }
        cards.append(card)
    
    return cards

