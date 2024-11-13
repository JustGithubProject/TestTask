from dataclasses import dataclass


BASE_URL = "https://www.work.ua"

@dataclass(frozen=True)
class CategoryConstants:
    RESUMES_IT = "/resumes-it/"
    # ...


@dataclass(frozen=True)
class JobPositionConstants:
    WEB_DEVELOPERS = "https://www.work.ua/resumes-it-web+developer"
    PYTHON_DEVELOPERS = "https://www.work.ua/resumes-it-python-developer"
    JAVASCRIPT_DEVELOPERS = "https://www.work.ua/resumes-it-javascript-developer"
    DATA_SCIENTISTS = "https://www.work.ua/resumes-it-data+scientist"
    GOLANG_DEVELOPER = "https://www.work.ua/resumes-it-golang+developer"
    FRONTEND_DEVELOPER = "https://www.work.ua/resumes-frontend+developer"
    BACKEND_DEVELOPER = "https://www.work.ua/resumes-backend-developer"
    FULLSTACK_DEVELOPER = "https://www.work.ua/resumes-fullstack+developer"
    

@dataclass(frozen=True)
class ExperienceConstants:
    NO_EXPERIENCE = "?experience=0"
    ONE_YEAR_EXPERIENCE = "?experience=1"
    ONE_TWO_YEARS_EXPERIENCE = "?experience=164"
    TWO_FIVE_YEARS_EXPERIENCE = "?experience=165"
    FIVE_AND_MORE_YEARS_EXPERIENCE = "?experience=166"


@dataclass(frozen=True)
class LocationConstants:
    ALL_UKRAINE = ""
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
    SALARY_TO_10K = "&salaryto=2"
    SALARY_TO_15K = "&salaryto=3"
    SALARY_TO_20K = "&salaryto=4"
    SALARY_TO_30K = "&salaryto=5"
    SALARY_TO_40K = "&salaryto=6"
    SALARY_TO_50K = "&salaryto=7"
    SALARY_TO_100K = "&salaryto=8"