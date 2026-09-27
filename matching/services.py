from jobs.models import Profile, Job


def calculate_skill_match(profile, job):
    user_skills = set(profile.skills.values_list("name", flat=True))
    job_skills = set(job.skills.values_list("name", flat=True))

    matched = user_skills & job_skills
    missing = job_skills - user_skills

    match_percentage = (
        len(matched) / len(job_skills) * 100
        if job_skills else 0
    )

    return {
        "matched": matched,
        "missing": missing,
        "match_percentage": match_percentage,
    }

    