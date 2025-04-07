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

cover_letter_text = '''
I am excited to express my interest in the Technical Project Manager role with Heartflow. I
believe I have the right combination of deep technical experience and leadership experience to
make a positive impact.
As a leader, I believe in practicing radical candor by providing and receiving honest feedback
with empathy and respect. As a team lead at StoryBlocks, I maintained focus on fostering
psychological safety such that radical candor was the norm. In this environment, everyone on
the team was excited to ideate and contribute thoughtfully to discussions. The result was a
highly aligned and motivated group of people that were eager to solve difficult problems and
hold each other accountable to high standards. I aim to facilitate this type of culture in my next
role.
At StoryBlocks, I led a multiphase effort to create an enterprise free trial subscription workflow
for our sales team to use with prospects. Each phase was validated by measured customer
interactions and qualitative reports from SDR sales calls to assess its effectiveness. Throughout
the project I interfaced with folks from design and product roles as well as the commercial sales
team to develop specifications for technical deliverables, user experience flows, and OKRs /
KPIs for the project. The technical deliverables required new api endpoints, new and updated
database models, new customer facing workflows, and instrumentation for analytics /
observability. The ROI for the project was a more effective sale cycle and faster times to close
for b2b contracts worth upwards of $50k.
Early in my career, I formed an LLC to service engineering contracts for a company that designs
materials for aerospace applications. My role was to design and implement engineering
processes for measuring the electrodynamic properties of the materials under strict compliance
requirements. I developed a true sense of ownership with this role. I was responsible for the
engineering work, managing customer facing business processes and everything in between.
The work I did was critical to their product development lifecycle and enabled the delivery of
several projects that total in value > $500K.
In sum, I will bring over a decade of experience in engineering, technical leadership, and
scientific computing to the table. I have a proven track record of leading engineering efforts that
generate customer value, while maintaining continuous focus on improvement of technical and
social processes. For these reasons, I believe I will be a valuable addition to your team. Thank
you for considering my application. I look forward to speaking with you.
Cheers,
Eddie Kemper

Dear Hiring Manager,

I’m excited to apply for the ____ role at ___. With over a decade of experience leading cross-functional software initiatives—spanning cloud-native development, agile delivery, REST API design, and stakeholder alignment—I bring a proven track record of successfully managing full project lifecycles in dynamic, high-growth environments.

At Storyblocks, I led multiple initiatives to deliver SaaS features and internal tools used by over 200 employees. I owned the entire agile cycle using Jira—from backlog grooming and sprint planning to risk mitigation and release readiness—driving a 15% increase in team velocity. I partnered closely with engineering leads, QA, and product managers to manage milestones, track deliverables, and ensure functional specs were aligned across teams.

More recently, I contributed to a cloud-based compliance platform at Medical Solutions, building and deploying REST APIs. Throughout my career, I’ve consistently managed technical risks, optimized team collaboration, and delivered projects on time and within budget across distributed teams.

I’m confident that my experience working with SaaS architecture, cloud infrastructure (AWS and GCP), and agile program management makes me well-suited for this role. I’m especially excited by Oracle’s mission to drive innovation at scale through cloud services and would love the opportunity to contribute to your team’s success.

Thank you for considering my application. I’d welcome the chance to discuss how I can support your product and engineering teams in delivering high-quality cloud solutions.

Cheers,,
Eddie Kemper


Dear Hiring Manager,
I’m excited to apply for the ___ role with ___. I bring over 10 years of experience delivering scalable web applications, managing cross-functional teams, and driving experimentation-focused development.
At Storyblocks, I led web platform initiatives that included A/B testing, internal tooling, and front-end enhancements. By aligning engineering, product, and design teams, I helped improve conversion metrics and accelerate time-to-value. My background spans Agile project management, risk mitigation, and platform-level delivery—skills I’ve used to keep web initiatives on track and outcome-driven.
With a strong engineering foundation, I translate technical complexity into clear plans and stakeholder updates. I’m passionate about experimentation, continuous improvement, and building web experiences that scale effectively.
Thank you for considering my application. I’d welcome the opportunity to discuss how I can support your team’s goals.
Best regards,
Eddie Kemper


I led an effort to integrate a third party api data service into our top-of-funnel user acquisition process. This integration optimized our enterprise sales lead generation ability. In coordinating the project, I managed relationships with our enterprise sales team to understand their needs, helped negotiate the contract with the vendor, and planned and implemented the technical aspects of the project. 

As a software engineer, I have led efforts toward system observability using event pipelines, thereby allowing bugs to be more easily traceable and enabling marketing insights to be drawn from user actions. I have led efforts to automate testing and CI/CD processes resulting in a higher confidence with every deployment. I led a project to integrate a new authentication mechanism to add security and efficiency to internal platform tooling. In all of these projects, my responsibilities included driving alignment among a diverse set of stakeholders, delegating work among engineers, formalizing timelines and milestones, prioritizing the backlog, codifying a definition of done, and mitigating project risk.


In grad school, I designed and implemented the hardware and software components for a system that measured concentrations of pesticides / insecticides in water.  ( described in resume also )
This involved designing and building:
The power electronics for the unit.
The embedded linux system that was used as a computational platform.
The image sensor hardware and the image processing software for acquiring data.
An automated calibration procedure.
The software that extracted the scientific results from the image processing results.
The touchscreen graphical user interface that was used to operate the device.
The systems and software that allowed the user to email the measured data. 

In managing this project:
I distilled the scientific operation that the device was intended to automate, and created a technical specification for the device.
I managed relationships with stakeholders from many backgrounds: chemistry, biology, mechanical engineering, electrical engineering, and lab technicians. 
I integrated feedback from stakeholders into the design process.
I broke the project into measurable milestones and fit the project into a tight timeline so that the device could be demoed at a conference. 

In the context of Agile project management, I have:

Led efficient and inclusive agile sprint ceremonies enabling effective product development, resource utilization, and team cohesion. 
Defined and prioritized engineering deliverables for the Storyblocks enterprise growth team which provided critical internal tooling for individuals and teams across the organization.
Engaged in close collaboration with technical and non-technical stakeholders (Product, Design, Analytics, Commercial) which enabled innovation and strategic alignment across multiple teams.
Created opportunities for ownership and autonomy among engineers, increasing empowerment, self-organization, growth, and productivity. 
Defined risk mitigating strategies for projects and created milestones and timelines for delivering product feature sets in phases that were focused on incrementally generating value for the customer.
Fostered a team culture of continuous learning and growth through structured engineering mentorship, 1:1 meetings,  growth plans, and performance reviews.
Collaborated directly with enterprise clients and external stakeholders to successfully plan and implement a data migration for ~5000 digital assets.

Hopefully this gives an overview of the breadth of my management experience in varying technical contexts. I’m eager to know more about the projects that Grow Therapy is working on and to see where my skill set could be the most impactful for you. 



Dear ___ Hiring Team,
I’m excited to apply for the Technical Program Manager role supporting the _____. With 11+ years of experience delivering high-impact technical initiatives across engineering, product, and marketing teams, I bring a strong track record of aligning strategy with execution—especially in ambiguous, growth-focused environments. I’m particularly inspired by Pinterest’s mission to help people create a life they love, and I’m eager to contribute to the systems that connect new users to that value.
At Storyblocks, I led a cross-functional initiative to develop an enterprise free trial platform, collaborating with sales, product, and engineering stakeholders to define milestones, manage technical risk, and deploy at scale. This effort directly accelerated our B2B sales cycle, shortening time-to-close for contracts exceeding $50K. Earlier, at HelpTile, I co-founded and engineered a SaaS platform where I implemented end-to-end telemetry and user engagement analytics to support data-driven product development—experience that aligns well with Pinterest’s emphasis on SEO and campaign tooling.
I thrive in environments that require systems thinking, clear communication, and leadership without authority. I’ve led agile ceremonies, implemented change management processes, and guided technical audits—consistently fostering transparency, trust, and velocity across teams. Whether I’m driving roadmap execution, building new processes, or resolving cross-team dependencies, I bring both a proactive mindset and deep technical fluency that enable me to translate complexity into action.
Pinterest’s mission to inspire people and help them create a life they love deeply resonates with me. I believe in building technology that empowers and uplifts, and I’m excited by the opportunity to contribute to a platform that’s a positive, creative corner of the internet. The chance to help new users discover that value—and to do so while growing alongside a team that values innovation, empathy, and impact—would be incredibly meaningful. I’d be thrilled to bring my technical leadership and cross-functional program experience to support that vision.
Thank you for considering my application—I look forward to the possibility of contributing to your team.
Cheers,
Edward Kemper
edwardkemper@gmail.com | (928) 514-7342 | Golden, CO
http://linkedin.com/in/edward-kemper-65929934



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
    ],
    "cover_letter_updates": [
      "Each item should suggest improvements to specific cover letter paragraphs for clarity, continuity, and relevance."
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

You are an expert technical recruiter and hiring advisor. Given the following job description (as JSON), a resume, and a cover letter, evaluate the candidate's fit for the role and return a score out of 100 along with a detailed breakdown by category.

---

**Job Description (JSON):**
{job_description_json}

**Resume:**
{resume}

**Cover Letter:**
{cover_letter_text}

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

4. Evaluate the candidate’s fit using the resume **and** cover letter, and score the following categories:

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

> Given the resume, the cover letter, and the job description, provide improvements from the perspective of a hiring manager to better align the candidate's materials with the role. Suggestions must not introduce untrue claims. Emphasize continuity and readability, and ensure each resume suggestion includes quantifiable impact where possible. Where appropriate, incorporate specific keywords and phrases from the job description into the suggestions to better align with applicant tracking systems (ATS) and highlight relevance to the role.

**Format your response as valid JSON. Please respond in pure JSON format without any markdown formatting.Format your response as pure JSON. Do not include Markdown formatting (such as triple backticks or language hints). Only return the raw JSON object.**

Here is the output template:

{formattedJsonStructure}

"""