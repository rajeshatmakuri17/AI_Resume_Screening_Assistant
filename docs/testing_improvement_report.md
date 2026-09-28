# Testing and Improvement Report

## Project Title

AI Resume Screening Assistant

## Student Information

Student Name: Rajesh Atmakuri

Course: BCIS 5140 – Artificial Intelligence in Business

---

# 1. Introduction

The purpose of this project was to develop an AI-powered workflow automation solution that assists recruiters during the initial resume screening process. The project was developed incrementally across multiple versions, allowing testing, evaluation, and continuous improvement throughout development.

The system was designed to compare candidate qualifications against job requirements and generate recommendations regarding interview eligibility. As the project evolved, additional capabilities were introduced to improve usability and automation.

---

# 2. Testing Approach

Testing was conducted to verify that the system correctly:

- Identified candidate skills
- Calculated match scores
- Detected missing qualifications
- Generated recommendations
- Produced expected outputs under different scenarios

Five test cases were developed and executed using Version 2 of the Resume Screening Assistant.

---

# 3. Test Results

## Test Case 1

Resume Skills:

- Python
- SQL
- Excel
- Machine Learning

Expected Match Score:

75%

Expected Recommendation:

Proceed to Interview

Actual Result:

75%

Status:

Pass

---

## Test Case 2

Resume Skills:

- Python
- SQL
- Machine Learning
- Power BI

Expected Match Score:

100%

Expected Recommendation:

Proceed to Interview

Actual Result:

100%

Status:

Pass

---

## Test Case 3

Resume Skills:

- Python
- SQL

Expected Match Score:

50%

Expected Recommendation:

Further Review Required

Actual Result:

50%

Status:

Pass

---

## Test Case 4

Resume Skills:

- Python

Expected Match Score:

25%

Expected Recommendation:

Not Recommended

Actual Result:

25%

Status:

Pass

---

## Test Case 5

Resume Skills:

- Excel

Expected Match Score:

0%

Expected Recommendation:

Not Recommended

Actual Result:

0%

Status:

Pass

---

# 4. Version Evolution

## Version 1: Basic Resume Screening

Features:

- Fixed candidate skill list
- Match score calculation
- Recommendation generation

Strengths:

- Demonstrated the core screening logic
- Established the foundation for future improvements

Limitation:

- Skills were hardcoded and could not be modified without editing the source code.

---

## Version 2: Interactive Screening System

Enhancement:

- Added user input functionality

Benefits:

- Recruiters could evaluate multiple candidates
- Candidate skills could be entered dynamically
- Reduced dependency on hardcoded values

Limitation:

- Users still had to manually enter skills instead of providing resume text.

---

## Version 3: Resume Text Analysis

Enhancement:

- Added automatic skill extraction from resume text

Benefits:

- Resume text could be pasted directly into the system
- Skills were extracted automatically
- Reduced manual work

Example:

Resume Text:

"Rajesh Atmakuri has experience in Python, SQL, Machine Learning, Excel, and Power BI."

Results:

- Python detected
- SQL detected
- Machine Learning detected
- Power BI detected

Match Score:

100%

Recommendation:

Proceed to Interview

Limitation:

- Job requirements remained predefined within the program.

---

## Version 4: Resume and Job Description Comparison

Enhancement:

- Added automatic extraction from both job descriptions and resume text

Benefits:

- More realistic recruitment workflow
- Automated comparison of candidate qualifications against job requirements
- Better support for different hiring scenarios

Example:

Job Description:

Required: Python, SQL, Machine Learning, Power BI, Excel

Resume:

Python, SQL, Machine Learning, Power BI

Result:

Match Score: 80%

Missing Skill:

Excel

Recommendation:

Proceed to Interview

This version represents the most advanced implementation completed during the project.

---

# 5. Challenges Encountered

Several challenges were encountered during development.

### Challenge 1: Transition from Static Data

The initial version relied entirely on predefined skill lists. Modifying the code for every candidate was inefficient and highlighted the need for user input functionality.
 
### Challenge 2: Implementing Automated Skill Extraction
 
Extracting skills from free-form resume text required additional logic and careful testing to ensure skills were identified correctly.
 
### Challenge 3: Package Compatibility
 
During development, the spaCy package was installed successfully. However, related dependency issues involving PyTorch generated runtime errors. To maintain project stability and ensure successful completion, an alternative text-processing approach was implemented.
 
---
 
# 6. Lessons Learned
 
The project provided several valuable learning experiences.
 
- Iterative development improves software quality.
- Testing helps identify limitations before deployment.
- AI and automation solutions require continuous refinement.
- Business workflows can be improved through automation.
- User-centered design increases practicality and usability.
- Technical challenges are a normal part of software development and often require alternative solutions.
 
---
 
# 7. Conclusion
 
The AI Resume Screening Assistant successfully evolved from a simple rule-based screening system into a more advanced workflow automation solution capable of extracting information from resume text and comparing candidate qualifications against job requirements. Through testing, evaluation, and multiple enhancements, the project demonstrated practical applications of AI-inspired workflow automation within a business recruitment context. All planned test cases passed successfully, and the final version provided a more realistic and usable solution than the original prototype.