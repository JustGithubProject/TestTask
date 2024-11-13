from work_ua_parser import constants


def filter_by_job(job_kind: str) -> str:
    """
        Returns the constant associated with a given job title.
    """
    job_map = {
        "Web developer": constants.JobPositionConstants.WEB_DEVELOPERS,
        "Python developer": constants.JobPositionConstants.PYTHON_DEVELOPERS,
        "Javascript developer": constants.JobPositionConstants.JAVASCRIPT_DEVELOPERS,
        "Data science developer": constants.JobPositionConstants.DATA_SCIENTISTS,
        "Golang developer": constants.JobPositionConstants.GOLANG_DEVELOPER,
        "Frontend developer": constants.JobPositionConstants.FRONTEND_DEVELOPER,
        "Backend developer": constants.JobPositionConstants.BACKEND_DEVELOPER,
        "Fullstack developer": constants.JobPositionConstants.FULLSTACK_DEVELOPER,
    }
    return job_map.get(job_kind)


def filter_by_experience(experience_kind: str) -> str:
    """
        Returns the constant associated with a given level of experience.
    """
    experience_map = {
        "Без досвіду": constants.ExperienceConstants.NO_EXPERIENCE,
        "1 рік": constants.ExperienceConstants.ONE_YEAR_EXPERIENCE,
        "1-2 роки": constants.ExperienceConstants.ONE_TWO_YEARS_EXPERIENCE,
        "2-5 роки": constants.ExperienceConstants.TWO_FIVE_YEARS_EXPERIENCE,
        "5+ років": constants.ExperienceConstants.FIVE_AND_MORE_YEARS_EXPERIENCE,
    }
    return experience_map.get(experience_kind)


def filter_by_location(location_name: str) -> str:
    """
        Returns the constant associated with a given location.
    """
    location_map = {
        "Вся Україна": constants.LocationConstants.ALL_UKRAINE,
        "Київ": constants.LocationConstants.KYIV,
        "Житомир": constants.LocationConstants.ZHYTOMYR,
        "Львів": constants.LocationConstants.LVIV,
        "Харків": constants.LocationConstants.KHARKIV,
        "Одеса": constants.LocationConstants.ODESA,
        "Дніпро": constants.LocationConstants.DNIPRO,
        "Вінниця": constants.LocationConstants.VINNYTSIA,
        "Полтава": constants.LocationConstants.POLTAVA,
        "Чернігів": constants.LocationConstants.CHERNIHIV,
        "Черкаси": constants.LocationConstants.CHERKASY,
        "Суми": constants.LocationConstants.SUMY,
        "Миколаїв": constants.LocationConstants.MYKOLAIV,
        "Херсон": constants.LocationConstants.KHERSON,
        "Рівне": constants.LocationConstants.RIVNE,
        "Хмельницький": constants.LocationConstants.KHMELNYTSKYI,
        "Тернопіль": constants.LocationConstants.TERNOPIL,
        "Івано-Франківськ": constants.LocationConstants.IVANO_FRANKIVSK,
        "Луцьк": constants.LocationConstants.LUTSK,
        "Ужгород": constants.LocationConstants.UZHHOROD,
    }
    return location_map.get(location_name)


def filter_by_salary(salary_range: str) -> str:
    """
        Returns the constant associated with a given salary range.
    """
    salary_map = {
        "до 10 000 грн": constants.SalaryConstants.SALARY_TO_10K,
        "до 15 000 грн": constants.SalaryConstants.SALARY_TO_15K,
        "до 20 000 грн": constants.SalaryConstants.SALARY_TO_20K,
        "до 30 000 грн": constants.SalaryConstants.SALARY_TO_30K,
        "до 40 000 грн": constants.SalaryConstants.SALARY_TO_40K,
        "до 50 000 грн": constants.SalaryConstants.SALARY_TO_50K,
        "до 100 000 грн": constants.SalaryConstants.SALARY_TO_100K,
    }
    return salary_map.get(salary_range)
