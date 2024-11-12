import constants


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
    

def filter_by_location():
    pass


def filter_by_salary():
    pass
    