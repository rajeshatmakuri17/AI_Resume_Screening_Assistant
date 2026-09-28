# AI Resume Screening Assistant V4
# Rajesh Atmakuri

import re

skill_dictionary = {
    "Python": ["python"],
    "SQL": ["sql", "sql server"],
    "Machine Learning": ["machine learning", "ml"],
    "Power BI": ["power bi", "powerbi"],
    "Excel": ["excel", "ms excel", "microsoft excel"]
}

print("=" * 60)
print("AI Resume Screening Assistant V4")
print("=" * 60)

job_description = input(
    "\nPaste Job Description:\n\n"
)

resume_text = input(
    "\nPaste Resume Text:\n\n"
)

job_description = job_description.lower()
resume_text = resume_text.lower()


def extract_skills(text):
    skills = []

    for skill, keywords in skill_dictionary.items():
        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, text):
                skills.append(skill)
                break

    return skills


job_skills = extract_skills(job_description)
resume_skills = extract_skills(resume_text)

matched_skills = []

for skill in job_skills:
    if skill in resume_skills:
        matched_skills.append(skill)

missing_skills = []

for skill in job_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)

if len(job_skills) > 0:
    match_score = (
        len(matched_skills) /
        len(job_skills)
    ) * 100
else:
    match_score = 0

if match_score >= 75:
    recommendation = "Proceed to Interview"
elif match_score >= 50:
    recommendation = "Further Review Required"
else:
    recommendation = "Not Recommended"

print("\n" + "=" * 60)
print("SCREENING RESULTS")
print("=" * 60)

print("\nJob Skills:")
for skill in job_skills:
    print("-", skill)

print("\nResume Skills:")
for skill in resume_skills:
    print("-", skill)

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)

print(f"\nMatch Score: {match_score:.0f}%")
print("Recommendation:", recommendation)