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
    

def filter_by_location(location_name: str) -> str:
    if location_name == "Kyiv":
        return constants.LocationConstants.KYIV
    if location_name == "Zhytomyr":
        return constants.LocationConstants.ZHYTOMYR
    if location_name == "Lviv":
        return constants.LocationConstants.LVIV
    if location_name == "Kharkiv":
        return constants.LocationConstants.KHARKIV
    if location_name == "Odesa":
        return constants.LocationConstants.ODESA
    if location_name == "Dnipro":
        return constants.LocationConstants.DNIPRO
    if location_name == "Vinnytsia":
        return constants.LocationConstants.VINNYTSIA
    if location_name == "Poltava":
        return constants.LocationConstants.POLTAVA
    if location_name == "Chernihiv":
        return constants.LocationConstants.CHERNIHIV
    if location_name == "Cherkasy":
        return constants.LocationConstants.CHERKASY
    if location_name == "Sumy":
        return constants.LocationConstants.SUMY
    if location_name == "Mykolaiv":
        return constants.LocationConstants.MYKOLAIV
    if location_name == "Kherson":
        return constants.LocationConstants.KHERSON
    if location_name == "Rivne":
        return constants.LocationConstants.RIVNE
    if location_name == "Khmelnytskyi":
        return constants.LocationConstants.KHMELNYTSKYI
    if location_name == "Ternopil":
        return constants.LocationConstants.TERNOPIL
    if location_name == "Ivano-Frankivsk":
        return constants.LocationConstants.IVANO_FRANKIVSK
    if location_name == "Lutsk":
        return constants.LocationConstants.LUTSK
    if location_name == "Uzhhorod":
        return constants.LocationConstants.UZHHOROD


def filter_by_salary(salary_range: str) -> str:
    if salary_range == "to 10k":
        return constants.SalaryConstants.SALARY_TO_10K
    if salary_range == "to 15k":
        return constants.SalaryConstants.SALARY_TO_15K
    if salary_range == "to 20k":
        return constants.SalaryConstants.SALARY_TO_20K
    if salary_range == "to 30k":
        return constants.SalaryConstants.SALARY_TO_30K
    if salary_range == "to 40k":
        return constants.SalaryConstants.SALARY_TO_40K
    if salary_range == "to 50k":
        return constants.SalaryConstants.SALARY_TO_50K
    if salary_range == "to 100k":
        return constants.SalaryConstants.SALARY_TO_100K