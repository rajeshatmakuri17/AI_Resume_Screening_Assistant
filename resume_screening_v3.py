# AI Resume Screening Assistant V3
# Rajesh Atmakuri

import re

job_requirements = [
    "Python",
    "SQL",
    "Machine Learning",
    "Power BI"
]

skill_dictionary = {
    "Python": ["python"],
    "SQL": ["sql", "sql server"],
    "Machine Learning": ["machine learning", "ml"],
    "Power BI": ["power bi", "powerbi"]
}

print("=" * 50)
print("AI Resume Screening Assistant V3")
print("=" * 50)

resume_text = input("\nPaste resume text:\n\n")

resume_text = resume_text.lower()

extracted_skills = []

for skill, keywords in skill_dictionary.items():
    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, resume_text):
            extracted_skills.append(skill)
            break

matched_skills = []
missing_skills = []

for skill in job_requirements:
    if skill in extracted_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

match_score = (
    len(matched_skills) /
    len(job_requirements)
) * 100

if match_score >= 75:
    recommendation = "Proceed to Interview"
elif match_score >= 50:
    recommendation = "Further Review Required"
else:
    recommendation = "Not Recommended"

print("\n" + "=" * 50)
print("SCREENING RESULTS")
print("=" * 50)

print("\nExtracted Skills:")
for skill in extracted_skills:
    print(f"- {skill}")

print("\nMatched Skills:")
for skill in matched_skills:
    print(f"- {skill}")

print("\nMissing Skills:")
for skill in missing_skills:
    print(f"- {skill}")

print(f"\nMatch Score: {match_score:.0f}%")
print(f"Recommendation: {recommendation}")