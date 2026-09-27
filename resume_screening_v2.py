# AI Resume Screening Assistant V2
# Rajesh Atmakuri

job_requirements = [
    "Python",
    "SQL",
    "Machine Learning",
    "Power BI"
]

print("AI Resume Screening Assistant")
print("-" * 35)

resume_input = input(
    "Enter resume skills separated by commas:\n"
)

resume_skills = [
    skill.strip()
    for skill in resume_input.split(",")
]

matched_skills = []
missing_skills = []

for skill in job_requirements:
    if skill in resume_skills:
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

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)

print(f"\nMatch Score: {match_score:.0f}%")
print("Recommendation:", recommendation)