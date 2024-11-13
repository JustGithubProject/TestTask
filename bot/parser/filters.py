from parser import constants


def filter_by_job(job_kind: str) -> str:
    if job_kind == "Web developer":
        return constants.JobPositionConstants.WEB_DEVELOPERS
    if job_kind == "Python developer":
        return constants.JobPositionConstants.PYTHON_DEVELOPERS
    if job_kind == "Javascript developer":
        return constants.JobPositionConstants.JAVASCRIPT_DEVELOPERS
    if job_kind == "Data science developer":
        return constants.JobPositionConstants.DATA_SCIENTISTS
    if job_kind == "Golang developer":
        return constants.JobPositionConstants.GOLANG_DEVELOPER
    if job_kind == "Frontend developer":
        return constants.JobPositionConstants.FRONTEND_DEVELOPER
    if job_kind == "Backend developer":
        return constants.JobPositionConstants.BACKEND_DEVELOPER
    if job_kind == "Fullstack developer":
        return constants.JobPositionConstants.FULLSTACK_DEVELOPER


def filter_by_experience(experience_kind: str) -> str:
    if experience_kind == "Без досвіду":
        return constants.ExperienceConstants.NO_EXPERIENCE
    if experience_kind == "1 рік":
        return constants.ExperienceConstants.ONE_YEAR_EXPERIENCE
    if experience_kind == "1-2 роки":
        return constants.ExperienceConstants.ONE_TWO_YEARS_EXPERIENCE
    if experience_kind == "2-5 роки":
        return constants.ExperienceConstants.TWO_FIVE_YEARS_EXPERIENCE
    if experience_kind == "5+ років":
        return constants.ExperienceConstants.FIVE_AND_MORE_YEARS_EXPERIENCE
    

def filter_by_location(location_name: str) -> str:
    if location_name == "Вся Україна":
        return constants.LocationConstants.ALL_UKRAINE
    if location_name == "Київ":
        return constants.LocationConstants.KYIV
    if location_name == "Житомир":
        return constants.LocationConstants.ZHYTOMYR
    if location_name == "Львів":
        return constants.LocationConstants.LVIV
    if location_name == "Харків":
        return constants.LocationConstants.KHARKIV
    if location_name == "Одеса":
        return constants.LocationConstants.ODESA
    if location_name == "Дніпро":
        return constants.LocationConstants.DNIPRO
    if location_name == "Вінниця":
        return constants.LocationConstants.VINNYTSIA
    if location_name == "Полтава":
        return constants.LocationConstants.POLTAVA
    if location_name == "Чернігів":
        return constants.LocationConstants.CHERNIHIV
    if location_name == "Черкаси":
        return constants.LocationConstants.CHERKASY
    if location_name == "Суми":
        return constants.LocationConstants.SUMY
    if location_name == "Миколаїв":
        return constants.LocationConstants.MYKOLAIV
    if location_name == "Херсон":
        return constants.LocationConstants.KHERSON
    if location_name == "Рівне":
        return constants.LocationConstants.RIVNE
    if location_name == "Хмельницький":
        return constants.LocationConstants.KHMELNYTSKYI
    if location_name == "Тернопіль":
        return constants.LocationConstants.TERNOPIL
    if location_name == "Івано-Франківськ":
        return constants.LocationConstants.IVANO_FRANKIVSK
    if location_name == "Луцьк":
        return constants.LocationConstants.LUTSK
    if location_name == "Ужгород":
        return constants.LocationConstants.UZHHOROD


def filter_by_salary(salary_range: str) -> str:
    if salary_range == "до 10 000 грн":
        return constants.SalaryConstants.SALARY_TO_10K
    if salary_range == "до 15 000 грн":
        return constants.SalaryConstants.SALARY_TO_15K
    if salary_range == "до 20 000 грн":
        return constants.SalaryConstants.SALARY_TO_20K
    if salary_range == "до 30 000 грн":
        return constants.SalaryConstants.SALARY_TO_30K
    if salary_range == "до 40 000 грн":
        return constants.SalaryConstants.SALARY_TO_40K
    if salary_range == "до 50 000 грн":
        return constants.SalaryConstants.SALARY_TO_50K
    if salary_range == "до 100 000 грн":
        return constants.SalaryConstants.SALARY_TO_100K