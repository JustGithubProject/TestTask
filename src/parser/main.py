

from bs4 import BeautifulSoup as BS4


import requests


import constants


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


def filter_by_job(job_kind: str) -> str:
    if job_kind == "Web developer":
        return constants.JobPositionConstants.WEB_DEVELOPERS
    if job_kind == "Python developer":
        return constants.JobPositionConstants.PYTHON_DEVELOPERS
    if job_kind == "Javascript developer":
        return constants.JobPositionConstants.JAVASCRIPT_DEVELOPERS
    if job_kind == "Data science":
        return constants.JobPositionConstants.DATA_SCIENTISTS
    if job_kind == "Golang developer":
        return constants.JobPositionConstants.GOLANG_DEVELOPER


def filter_by_experience(experience_kind: str) -> str:
    if experience_kind == "No experience":
        return constants.ExperienceConstants.NO_EXPERIENCE
    if experience_kind == "1 year":
        return constants.ExperienceConstants.ONE_YEAR_EXPERIENCE
    if experience_kind == "1-2 years":
        return constants.ExperienceConstants.ONE_TWO_YEARS_EXPERIENCE
    if experience_kind == "2-5 years":
        return constants.ExperienceConstants.TWO_FIVE_YEARS_EXPERIENCE
    if experience_kind == "5+":
        return constants.ExperienceConstants.FIVE_AND_MORE_YEARS_EXPERIENCE
    
        
    
    


def filter_by_location():
    pass


def filter_by_salary():
    pass
    


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