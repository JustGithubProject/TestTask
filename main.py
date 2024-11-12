from dataclasses import dataclass

from bs4 import BeautifulSoup as BS4

import requests


BASE_URL = "https://www.work.ua"


@dataclass(frozen=True)
class CategoryConstants:
    RESUMES_IT = "/resumes-it/"
    # ...


@dataclass(frozen=True)
class JobPositionConstants:
    WEB_DEVELOPERS = "https://www.work.ua/resumes-it-web+developer/"
    PYTHON_DEVELOPERS = "https://www.work.ua/resumes-it-python-developer/"
    JAVASCRIPT_DEVELOPERS = "https://www.work.ua/resumes-it-javascript-developer/"
    DATA_SCIENTISTS = "https://www.work.ua/resumes-it-data+scientist/"
    GOLANG_DEVELOPER = "https://www.work.ua/resumes-it-golang+developer/"
    

@dataclass(frozen=True)
class ExperienceConstants:
    NO_EXPERIENCE = "?experience=0"
    ONE_YEAR_EXPERIENCE = "?experience=1"
    ONE_TWO_YEARS_EXPERIENCE = "?experience=164"
    TWO_FIVE_YEARS_EXPERIENCE = "?experience=165"
    FIVE_AND_MORE_YEARS_EXPERIENCE = "?experience=166"


@dataclass(frozen=True)
class LocationConstants:
    KYIV = "+київ"
    ZHYTOMYR = "+житомир"
    LVIV = "+львів"
    KHARKIV = "+харків"
    ODESA = "+одеса"
    DNIPRO = "+дніпро"
    VINNYTSIA = "+вінниця"
    POLTAVA = "+полтава"
    CHERNIHIV = "+чернігів"
    CHERKASY = "+черкаси"
    SUMY = "+суми"
    MYKOLAIV = "+миколаїв"
    KHERSON = "+херсон"
    RIVNE = "+рівне"
    KHMELNYTSKYI = "+хмельницький"
    TERNOPIL = "+тернопіль"
    IVANO_FRANKIVSK = "+івано-франківськ"
    LUTSK = "+луцьк"
    UZHHOROD = "+ужгород"

    

@dataclass(frozen=True)
class SalaryConstants:
    SALARY_TO_10K = "?salaryto=2"
    SALARY_TO_15K = "?salaryto=3"
    SALARY_TO_20K = "?salaryto=4"
    SALARY_TO_30K = "?salaryto=5"
    SALARY_TO_40K = "?salaryto=6"
    SALARY_TO_50K = "?salaryto=7"
    SALARY_TO_100K = "?salaryto=8"


def save_html(filename: str, html) -> None:
    with open(filename, "w") as file:
        file.write(html)
        

def read_html(filename: str) -> str:
    with open(filename, "r") as file:
        html_content = file.read()
    return html_content


def request_to_site(url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        save_html("index.html", response.text)


def get_titles() -> list:
    html_content = read_html("index.html")
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    h2_mt_0_content_all = [item.text for item in h2_mt_0_all]
    return h2_mt_0_content_all


def get_links() -> list:
    html_content = read_html("index.html")
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    hrefs_content_all = [item.find("a").get("href") for item in h2_mt_0_all]
    return hrefs_content_all


def get_owners_info() -> list:
    html_content = read_html("index.html")
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
            "links": BASE_URL + links[i]
        }
        cards.append(card)
    print(cards)
    

def main():
    # request_to_site(JobPositionConstants.GOLANG_DEVELOPER)
    get_resumes()
    
    


if __name__ == "__main__":
    main()