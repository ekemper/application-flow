import json

resume = '''
Edward Kemper
edwardkemper@gmail.com | (928) 514-7342 | Golden, CO | Linkedin.com/in/edward-kemper-65929934

Technical Program Manager / Engineer with 11 years of experience leading cross-functional teams to deliver scalable software solutions. Skilled at driving complex programs from inception to completion while ensuring alignment across engineering, product, and business objectives. Experienced in conducting security audits, implementing DevOps best practices, and enhancing system observability. Adept at risk management, workflow optimization, and fostering cross-team collaboration. A proactive leader who champions growth through empathy and trust. PMP certification in progress.
PROFESSIONAL EXPERIENCE

Technical Project Manager (Construction), Denver CO | Jan 2025 – Present 
Develops and maintains project roadmaps, Gantt charts, and milestone tracking for initiatives exceeding $100k ensuring high quality and timely delivery. 
Manages and coordinates meetings with subcontractors to ensure adherence to project timelines, alignment on priorities, and clarity of deliverables.
Provides regular project status reports to the client, clearly communicating progress, risk mitigation, and change management. Ensures transparency, manages expectations, and fosters stakeholder trust.

Medical Solutions, Remote | Feb 2024 – July 2024
Senior Software Engineer
Built REST API MVP solution with developer-friendly documentation to support a digital platform for short-term clinician contract management and compliance tracking..
Collaborated with product and QA teams to implement robust testing strategies and reduce post-release defects.

Sparkplug, Remote | Jan 2023 – June 2023
Senior Software Engineer
Built third-party API integrations to optimize vendor integration workflows, supporting enterprise business development.
Designed application-layer data models to migrate relational data from MongoDB to PostgreSQL, enhancing analytical and transactional query support.

Storyblocks, Remote | 2020 – 2022
Senior Software Engineer / Team Lead
Drove successful product development by leading agile sprint ceremonies, managing project risks, and ensuring team alignment—leading to a 15% increase in team velocity and stronger team cohesion.
Managed a team delivering an enterprise free trial subscription workflow, optimizing cross-team alignment and reducing B2B contract close times by 20%
Developed critical internal tools used by 200+ employees by defining and prioritizing engineering deliverables for the enterprise growth team improving internal API accessibility and enhancing developer productivity.
Identified and mitigated key risks to project success, establishing milestones and timelines to deliver product features to customers.
Implemented a structured mentorship program including  weekly one-on-one’s, tailored growth plans, and performance reviews which contributed to improved team development and velocity.

Other Relevant Software Engineering Experience 2016 – 2020
Held roles in Software Development at IHS Markit and Proximity Inc.
Collaborated with product teams to deliver financial data visualization solutions to a client serving >1M users per day.
Established core agile processes and standards for a newly formed engineering team, driving a 10% improvement in delivery velocity and team efficiency. 
Implemented automated testing procedures with Vue.js, PHP, and Docker, leading to improved deployment stability and developer confidence across the company.

Kemper Systems LLC, Flagstaff, AZ | 2013 – 2017
Technical Program Manager
Spearheaded the development of an innovative system to measure high-frequency dielectric properties of custom materials, which became the company-wide standard for testing, directly contributing to future product development for projects valued at ~$200k each.
Oversaw technical project execution end-to-end, coordinating across multiple stakeholders, guiding the integration of technical designs with business objectives, ensuring adherence to quality and regulatory standards. 
Transformed business requirements into an actionable engineering roadmap; collaborated with engineering leaders and key stakeholders to define project milestones, own change management processes, manage budgets, and proactively mitigate risks while ensuring timely delivery.

HelpTile.com, Flagstaff, AZ | 2014 – 2016
Co-founder/Developer
Accelerated software product delivery by implementing an end-to-end (E2E) testing strategy ensuring the quality and robustness of releases.
Established telemetry to evaluate user engagement, enabling data-driven product development and strategic decision-making.
Ensured data security by reshaping the platform's security posture and performing a cybersecurity audit with an external consultant.

Northern Arizona University, Flagstaff, AZ | 2013
Engineer / Project Manager
Engineered a novel scientific instrument to quantify insecticide concentrations in water and assess environmental pollution levels.
Led system design and implementation in collaboration with key stakeholders across biochemistry, electrical engineering, and mechanical engineering departments, ensuring alignment on technical requirements and establishing a strong project framework.

CORE COMPETENCIES
SDLC • Technical Program Management • Technical Project Management • Team Leadership • Stakeholder Communication • Cross-team Collaboration • Servant Leadership • Agile Methodologies • Developer Experience • Change Management • Technical Requirements Analysis • Risk Assessment & Mitigation • SQL / Analysis • Quality Assurance • Full-Stack Engineering • Automated Testing Procedures • Budgeting & Resource Allocation • Process Improvement • Machine Learning • AI Integrations • Scientific Computing • Electro-Mechanical Design • Control & Automation Systems • Image Processing Algorithms

TECHNICAL SKILLS
Frontend: React • Vue.js | Backend: Node.js • Typescript • Python • PHP | Database Design: MYSQL • PostgreSQL • MongoDB | API Development: Public REST APIs | Testing & Automation: Selenium • Cypress • Jest 
Infrastructure & CI/CD: AWS • Google Cloud Platform • Pulumi • GitHub • Docker • Linux
Cyber Security Best Practices | Project Management tools: Jira • Linear • Asana • Figma • Notion

EDUCATION 
MS Electrical Engineering, Northern Arizona University 2014
BS Physics, Minor in Applied Mathematics, Humboldt State University 2007

'''

jsonStructure = {
  "total_score": 0,
  "categories": {
    "technical_skills": {
      "score": 0,
      "feedback": ""
    },
    "relevant_experience": {
      "score": 0,
      "feedback": ""
    },
    "domain_knowledge": {
      "score": 0,
      "feedback": ""
    },
    "communication_skills": {
      "score": 0,
      "feedback": ""
    },
    "motivation_and_alignment": {
      "score": 0,
      "feedback": ""
    },
    "cultural_fit": {
      "score": 0,
      "feedback": ""
    },
    "career_trajectory": {
      "score": 0,
      "feedback": ""
    }
  },
  "summary": "",
  "suggestions": {
    "resume_bullet_updates": [
      "Each item should suggest a revision to a specific resume bullet, maintaining truthfulness and adding quantifiable impact."
    ]
  },
  "job_insights": {
    "is_remote": False,
    "is_hybrid": False,
    "is_onsite": False,
    "has_dei_initiative": False,
    "requires_security_clearance": False,
    "main_industry_domain": "",
    "requires_software_engineering_experience": False,
    "has_pay_information": False
  }
}


formattedJsonStructure = json.dumps(jsonStructure, indent=2)

def prompt(job_description_json):
    return f"""

You are an expert technical recruiter and hiring advisor. Given the following job description (as JSON), and a resume, evaluate the candidate's fit for the role and return a score out of 100 along with a detailed breakdown by category.

---

**Job Description (JSON):**
{job_description_json}

**Resume:**
{resume}

---

**Instructions:**

1. Parse the job description JSON object with the following properties:
    - job_title
    - company_name
    - job_description
    - pay_information
    - job_description_page_link
    - job_location
    - raw_html

2. Extract and include the following boolean or categorical indicators in the output JSON:
    - is_remote
    - is_hybrid
    - is_onsite
    - has_dei_initiative
    - requires_security_clearance
    - main_industry_domain
    - requires_software_engineering_experience
    - has_pay_information

3. Extract from the job description:
    - Required and preferred skills
    - Desired years and types of experience
    - Key responsibilities
    - Domain/industry focus (if applicable)
    - Cultural values or soft skill expectations

4. Evaluate the candidate’s fit using the resume, and score the following categories:

    - Technical Skills (0–25 points)  
    - Relevant Experience (0–20 points)  
    - Domain Knowledge (0–10 points)  
    - Communication Skills (0–10 points)  
    - Motivation & Alignment (from the cover letter) (0–15 points)  
    - Cultural or Organizational Fit (0–10 points)  
    - Career Trajectory & Role Alignment (0–10 points)

    In both the scoring and qualitative feedback, take special note of any factors that indicate a potential mismatch with the role. Clearly identify and explain when any of the following significantly contribute to a lower overall score. Specifically, call out and deduct points in the relevant categories if any of the following are present:
    
    - The job description explicitly requires an **active security clearance** and it is not evident in the resume.
    - The candidate (Edward) has **never managed a team of technical program managers**, and this experience is required.
    - The job description **does not mention that software engineering experience is a plus or counts toward relevant experience**, and the resume leans heavily on engineering experience.
    - There are **very specific technology requirements** in the job description that are **not addressed or mentioned** in the resume.
    - It is clear from the description that **Edward's years of software engineering experience and master’s in Electrical Engineering do not compensate for the stated minimum number of years of professional experience as a technical program manager**.

    These factors should impact both the quantitative score and the narrative feedback in the final summary and category feedback.


5. For the `suggestions` array, follow this logic:

> Given the resume and the job description, provide improvements from the perspective of a hiring manager to better align the candidate's materials with the role. Suggestions must not introduce untrue claims. Emphasize continuity and readability, and ensure each resume suggestion includes quantifiable impact where possible. Where appropriate, incorporate specific keywords and phrases from the job description into the suggestions to better align with applicant tracking systems (ATS) and highlight relevance to the role.

**Format your response as valid JSON. Please respond in pure JSON format without any markdown formatting.Format your response as pure JSON. Do not include Markdown formatting (such as triple backticks or language hints). Only return the raw JSON object.**

Here is the output template:

{formattedJsonStructure}

"""