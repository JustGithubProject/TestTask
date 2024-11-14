from dataclasses import dataclass


BASE_URL = "https://robota.ua"

@dataclass(frozen=True)
class JobPositionConstants:
    WEB_DEVELOPERS = f"{BASE_URL}/ru/candidates/web-developer/ukraine?rubrics=%5B%221%22%5D"
    PYTHON_DEVELOPERS = f"{BASE_URL}/ru/candidates/python-developer/ukraine?rubrics=%5B%221%22%5D"
    JAVASCRIPT_DEVELOPERS = f"{BASE_URL}/ru/candidates/javascript-developer/ukraine?rubrics=%5B%221%22%5D"
    DATA_SCIENTISTS = f"{BASE_URL}/ru/candidates/data-scientist/ukraine?rubrics=%5B%221%22%5D"
    GOLANG_DEVELOPER = f"{BASE_URL}/ru/candidates/golang-developer/ukraine?rubrics=%5B%221%22%5D"
    FRONTEND_DEVELOPER = f"{BASE_URL}/ru/candidates/frontend-developer/ukraine?rubrics=%5B%221%22%5D"
    BACKEND_DEVELOPER = f"{BASE_URL}/ru/candidates/backend-developer/ukraine?rubrics=%5B%221%22%5D"
    FULLSTACK_DEVELOPER = f"{BASE_URL}/ru/candidates/fullstack-developer/ukraine?rubrics=%5B%221%22%5D"
    

@dataclass(frozen=True)
class LocationConstants:
    ALL_UKRAINE = "ukraine"
    KYIV = "kyiv"
    ZHYTOMYR = "zhitomir"
    LVIV = "lviv"
    KHARKIV = "kharkiv"
    ODESA = "odessa"
    DNIPRO = "dnipro"
    VINNYTSIA = "vinnytsia"
    POLTAVA = "poltava"
    CHERNIHIV = "chernihiv"
    CHERKASY = "cherkasy"
    SUMY = "sumy"
    MYKOLAIV = "mykolaiv"
    KHERSON = "kherson"
    RIVNE = "rivne"
    KHMELNYTSKYI = "khmelnytskyi"
    TERNOPIL = "ternopil"
    IVANO_FRANKIVSK = "ivano-frankivsk"
    LUTSK = "lutsk"
    UZHHOROD = "uzhhorod"


@dataclass(frozen=True)
class ExperienceConstants:
    NO_EXPERIENCE = '&experienceIds=["0"]'
    ONE_YEAR_EXPERIENCE = '&experienceIds=["1"]'
    ONE_TWO_YEARS_EXPERIENCE = '&experienceIds=["2"]'
    TWO_FIVE_YEARS_EXPERIENCE = '&experienceIds=["3"]'
    FIVE_AND_MORE_YEARS_EXPERIENCE = '&experienceIds=["4"]'


@dataclass(frozen=True)
class SalaryConstants:
    SALARY_TO_10K = '&salary={"from"%3Anull%2C"to"%3A10000}'
    SALARY_TO_15K = '&salary={"from"%3Anull%2C"to"%3A15000}'
    SALARY_TO_20K = '&salary={"from"%3Anull%2C"to"%3A20000}'
    SALARY_TO_30K = '&salary={"from"%3Anull%2C"to"%3A30000}'
    SALARY_TO_40K = '&salary={"from"%3Anull%2C"to"%3A40000}'
    SALARY_TO_50K = '&salary={"from"%3Anull%2C"to"%3A50000}'
    SALARY_TO_100K = '&salary={"from"%3Anull%2C"to"%3A100000}'