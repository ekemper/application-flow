
---

**Instructions**

You are an expert technical recruiter and hiring advisor tasked with evaluating candidate materials for high-level technical roles such as Technical Program Manager. Your goal is to analyze the candidate’s resume and cover letter in the context of a provided job description and produce a structured, professional evaluation.

---

### Step 1: Parse the Job Description

You’ll receive a job description in JSON format with the following fields:

    title
    name
    company
    location
    via
    posted
    salary
    extensions
    detected_extensions
    description
    share_link
    job_highlights

- Note any missing or empty fields.
- Include a section in your evaluation summarizing any parsing errors.

---

### Step 2: Extract Job Insights

From the job description, extract the following categorical or boolean indicators:

- **Is Remote**: true/false  
- **Is Hybrid**: true/false  
- **Is Onsite**: true/false  
- **Has DEI Initiative**: true/false  
  (Look for statements about DEI programs, inclusive hiring, ERGs, etc.)
- **Requires Security Clearance**: true/false  
- **Main Industry Domain**: e.g., Healthcare, AdTech, SaaS, Fintech  
- **Requires Software Engineering Experience**: true/false  
- **Has Pay Information**: true/false

---

### Step 3: Extract Role Requirements and Context

Summarize the following from the job description:

- Required and preferred technical and soft skills  
- Years and types of experience (e.g., “3+ years in TPM roles”)  
- Key responsibilities and deliverables  
- Domain or industry focus (if applicable)  
- Cultural values and team expectations  

Use these details to inform your evaluation of the candidate.

---

### Step 4: Evaluate the Candidate Fit

Based on the resume and cover letter, assign a score and write detailed feedback for each of the following categories:

| Category                        | Max Points |
|----------------------------------|------------|
| Technical Skills                 | 25         |
| Relevant Experience              | 20         |
| Domain Knowledge                 | 10         |
| Communication Skills             | 10         |
| Motivation & Alignment           | 15         |
| Cultural or Organizational Fit   | 10         |
| Career Trajectory & Role Alignment | 10         |

#### Important: Penalty Rules  
Explicitly deduct points if the following apply (and explain each deduction):

- The role requires a security clearance, but the candidate doesn’t mention one.
- The candidate has never managed a team of TPMs, and the job requires it.
- The resume leans too heavily on software engineering, while TPM-specific experience is required or preferred.
- The candidate lacks specific technologies or methodologies that are explicitly required.
- The candidate’s experience and education do not meet clearly stated minimums.

Adjust the category scores accordingly and explain any point deductions clearly in your feedback.

---

### Step 5: Provide Actionable Suggestions

Offer concrete suggestions to improve the resume and cover letter.

#### Resume Bullet Updates

Each suggestion should include:

- **Update**: A revised or new resume bullet point  
- **Rationale**: Why this update improves clarity, keyword match, relevance, or impact

Focus on:

- Aligning more closely with the job description  
- Adding truthful keywords or technologies  
- Introducing quantifiable results  
- Improving clarity and relevance for hiring managers and ATS systems  

#### Cover Letter Updates

Each suggestion should include:

- **Update**: A suggested change to tone, structure, or content  
- **Rationale**: Why the change improves storytelling, alignment, or professionalism

Focus on:

- Strengthening the narrative  
- Better aligning with the job description  
- Enhancing clarity and flow  

---

### Final Output Format (in Markdown)

Structure your final evaluation as follows:

#### 📄 Candidate Evaluation Summary

**Total Score**:  
- Integer between 0 and 100  
- Sum of all category scores  

---

#### 🎯 Category Scores and Feedback

Provide each of the following:

- **Score**: Numerical score for the category  
- **Feedback**: A few professional sentences justifying the score using specific evidence

---

#### 🧾 Summary

Write a short paragraph (3–5 sentences) summarizing your overall impression, including:

- Key strengths  
- Gaps or concerns  
- Notable highlights or red flags  

---

#### 💡 Suggestions

**Resume Bullet Updates**  
A list of proposed resume changes, each with:
- **Update**: The proposed new bullet
- **Rationale**: Why this bullet is an improvement

**Cover Letter Updates**  
A list of proposed improvements, each with:
- **Update**: The proposed change
- **Rationale**: Why this change enhances clarity, tone, or alignment

---

#### 🔍 Job Insights

Include all of the following metadata extracted from the job description:

- Is Remote  
- Is Hybrid  
- Is Onsite  
- Has DEI Initiative  
- Requires Security Clearance  
- Main Industry Domain  
- Requires Software Engineering Experience  
- Has Pay Information  

---

#### ⚠️ Parsing Errors (if any)

List any missing or malformed fields from the job description JSON.


# Edward Kemper

**Email:** edwardkemper@gmail.com  
**Phone:** (928) 514-7342  
**Location:** Golden, CO  
**LinkedIn:** [linkedin.com/in/edward-kemper-65929934](https://linkedin.com/in/edward-kemper-65929934)

---

## Summary

Technical Program Manager / Engineer with 11 years of experience leading cross-functional teams to deliver scalable software solutions. Skilled at driving complex programs from inception to completion while ensuring alignment across engineering, product, and business objectives. Experienced in conducting security audits, implementing DevOps best practices, and enhancing system observability. Adept at risk management, workflow optimization, and fostering cross-team collaboration. A proactive leader who champions growth through empathy and trust. PMP certification in progress.

---

## Professional Experience

### Technical Project Manager (Construction)  
**Denver, CO | Jan 2025 – Present**

- Develops and maintains project roadmaps, Gantt charts, and milestone tracking for initiatives exceeding $100k ensuring high quality and timely delivery.  
- Manages and coordinates meetings with subcontractors to ensure adherence to project timelines, alignment on priorities, and clarity of deliverables.  
- Provides regular project status reports to the client, clearly communicating progress, risk mitigation, and change management. Ensures transparency, manages expectations, and fosters stakeholder trust.

### Medical Solutions  
**Remote | Feb 2024 – July 2024**  
**Senior Software Engineer**

- Built REST API MVP solution with developer-friendly documentation to support a digital platform for short-term clinician contract management and compliance tracking.  
- Collaborated with product and QA teams to implement robust testing strategies and reduce post-release defects.

### Sparkplug  
**Remote | Jan 2023 – June 2023**  
**Senior Software Engineer**

- Built third-party API integrations to optimize vendor integration workflows, supporting enterprise business development.  
- Designed application-layer data models to migrate relational data from MongoDB to PostgreSQL, enhancing analytical and transactional query support.

### Storyblocks  
**Remote | 2020 – 2022**  
**Senior Software Engineer / Team Lead**

- Led agile sprint ceremonies, managed project risks, and ensured team alignment—resulting in a 15% increase in team velocity and stronger team cohesion.  
- Managed a team delivering an enterprise free trial subscription workflow, reducing B2B contract close times by 20%.  
- Developed internal tools used by 200+ employees by improving internal API accessibility and developer productivity.  
- Identified and mitigated key project risks, established milestones and timelines.  
- Implemented structured mentorship programs with one-on-ones, growth plans, and performance reviews.

### Other Relevant Software Engineering Experience  
**2016 – 2020**

- Held software development roles at IHS Markit and Proximity Inc.  
- Delivered financial data visualization solutions for a client serving over 1M users/day.  
- Established agile standards, improving delivery velocity and team efficiency by 10%.  
- Implemented automated testing using Vue.js, PHP, and Docker, increasing deployment stability and developer confidence.

### Kemper Systems LLC  
**Flagstaff, AZ | 2013 – 2017**  
**Technical Program Manager**

- Developed a system to measure dielectric properties of materials, becoming the company-wide standard for product development (~$200k/project).  
- Led end-to-end project execution, aligning technical solutions with business needs and compliance standards.  
- Defined engineering roadmaps, managed change, timelines, budgets, and risk.

### HelpTile.com  
**Flagstaff, AZ | 2014 – 2016**  
**Co-founder / Developer**

- Implemented E2E testing to ensure release quality.  
- Established telemetry to evaluate user engagement and guide product development.  
- Conducted a cybersecurity audit with an external consultant.

### Northern Arizona University  
**Flagstaff, AZ | 2013**  
**Engineer / Project Manager**

- Engineered a scientific instrument to quantify insecticide concentrations in water.  
- Led design and implementation across biochemistry, EE, and ME stakeholders.

---

## Core Competencies

SDLC • Technical Program Management • Team Leadership • Stakeholder Communication • Cross-team Collaboration • Servant Leadership • Agile Methodologies • Developer Experience • Change Management • Technical Requirements Analysis • Risk Assessment & Mitigation • SQL / Analysis • Quality Assurance • Full-Stack Engineering • Automated Testing • Budgeting & Resource Allocation • Process Improvement • Machine Learning • AI Integrations • Scientific Computing • Electro-Mechanical Design • Control & Automation Systems • Image Processing Algorithms

---

## Technical Skills

**Frontend:** React • Vue.js  
**Backend:** Node.js • TypeScript • Python • PHP  
**Databases:** MySQL • PostgreSQL • MongoDB  
**API Development:** Public REST APIs  
**Testing & Automation:** Selenium • Cypress • Jest  
**Infrastructure & CI/CD:** AWS • Google Cloud Platform • Pulumi • GitHub • Docker • Linux  
**Security & Tools:** Cyber Security Best Practices • Jira • Linear • Asana • Figma • Notion

---

## Education

**MS, Electrical Engineering**  
Northern Arizona University, 2014

**BS, Physics** (Minor: Applied Mathematics)  
Humboldt State University, 2007

# Cover Letter Examples

## Example 1

I am excited to express my interest in the Technical Project Manager role with Heartflow. I believe I have the right combination of deep technical experience and leadership experience to make a positive impact.

As a leader, I believe in practicing radical candor by providing and receiving honest feedback with empathy and respect. As a team lead at StoryBlocks, I maintained focus on fostering psychological safety such that radical candor was the norm. In this environment, everyone on the team was excited to ideate and contribute thoughtfully to discussions. The result was a highly aligned and motivated group of people that were eager to solve difficult problems and hold each other accountable to high standards. I aim to facilitate this type of culture in my next role.

At StoryBlocks, I led a multiphase effort to create an enterprise free trial subscription workflow for our sales team to use with prospects. Each phase was validated by measured customer interactions and qualitative reports from SDR sales calls to assess its effectiveness. Throughout the project I interfaced with folks from design and product roles as well as the commercial sales team to develop specifications for technical deliverables, user experience flows, and OKRs / KPIs for the project. The technical deliverables required new API endpoints, new and updated database models, new customer-facing workflows, and instrumentation for analytics and observability. The ROI for the project was a more effective sales cycle and faster times to close for B2B contracts worth upwards of $50K.

Early in my career, I formed an LLC to service engineering contracts for a company that designs materials for aerospace applications. My role was to design and implement engineering processes for measuring the electrodynamic properties of the materials under strict compliance requirements. I developed a true sense of ownership with this role. I was responsible for the engineering work, managing customer-facing business processes, and everything in between. The work I did was critical to their product development lifecycle and enabled the delivery of several projects that totaled in value over $500K.

In sum, I will bring over a decade of experience in engineering, technical leadership, and scientific computing to the table. I have a proven track record of leading engineering efforts that generate customer value, while maintaining continuous focus on improvement of technical and social processes.

Thank you for considering my application. I look forward to speaking with you.

**Cheers,**  
Eddie Kemper

---

## Example 2

Dear Hiring Manager,

I’m excited to apply for the \_**_ role at _**. With over a decade of experience leading cross-functional software initiatives—spanning cloud-native development, agile delivery, REST API design, and stakeholder alignment—I bring a proven track record of successfully managing full project lifecycles in dynamic, high-growth environments.

At Storyblocks, I led multiple initiatives to deliver SaaS features and internal tools used by over 200 employees. I owned the entire agile cycle using Jira—from backlog grooming and sprint planning to risk mitigation and release readiness—driving a 15% increase in team velocity. I partnered closely with engineering leads, QA, and product managers to manage milestones, track deliverables, and ensure functional specs were aligned across teams.

More recently, I contributed to a cloud-based compliance platform at Medical Solutions, building and deploying REST APIs. Throughout my career, I’ve consistently managed technical risks, optimized team collaboration, and delivered projects on time and within budget across distributed teams.

I’m confident that my experience working with SaaS architecture, cloud infrastructure (AWS and GCP), and agile program management makes me well-suited for this role. I’m especially excited by Oracle’s mission to drive innovation at scale through cloud services and would love the opportunity to contribute to your team’s success.

Thank you for considering my application. I’d welcome the chance to discuss how I can support your product and engineering teams in delivering high-quality cloud solutions.

**Cheers,**  
Eddie Kemper

---

## Example 3

Dear Hiring Manager,

I’m excited to apply for the **_ role with _**. I bring over 10 years of experience delivering scalable web applications, managing cross-functional teams, and driving experimentation-focused development.

At Storyblocks, I led web platform initiatives that included A/B testing, internal tooling, and front-end enhancements. By aligning engineering, product, and design teams, I helped improve conversion metrics and accelerate time-to-value. My background spans Agile project management, risk mitigation, and platform-level delivery—skills I’ve used to keep web initiatives on track and outcome-driven.

With a strong engineering foundation, I translate technical complexity into clear plans and stakeholder updates. I’m passionate about experimentation, continuous improvement, and building web experiences that scale effectively.

Thank you for considering my application. I’d welcome the opportunity to discuss how I can support your team’s goals.

**Best regards,**  
Eddie Kemper

---

## Additional Project Highlights

-   **API Integration for Lead Generation**  
    I led an effort to integrate a third-party API data service into our top-of-funnel user acquisition process. This integration optimized our enterprise sales lead generation ability. I managed relationships with our enterprise sales team, helped negotiate the vendor contract, and led the implementation of the technical aspects of the project.

-   **Observability and CI/CD**  
    I’ve led initiatives on system observability using event pipelines, allowing for better debugging and marketing analytics. I’ve automated testing and CI/CD processes, improving deployment confidence. I also integrated a new authentication mechanism to enhance security and efficiency for internal tools.

-   **Key Responsibilities**
    -   Driving alignment among stakeholders
    -   Delegating engineering tasks
    -   Managing timelines and milestones
    -   Prioritizing backlogs
    -   Defining a “definition of done”
    -   Mitigating project risk

---

## Graduate School Project

In grad school, I designed and implemented a system to measure pesticide/insecticide concentrations in water.

**Components Designed and Built:**

-   Power electronics for the unit
-   Embedded Linux system
-   Image sensor hardware and image processing software
-   Automated calibration procedure
-   Software to extract scientific results
-   Touchscreen graphical user interface
-   Email functionality for sending measured data

**Project Management Tasks:**

-   Defined technical specs based on scientific goals
-   Managed cross-disciplinary stakeholder relationships (chemistry, biology, mechanical and electrical engineering, lab technicians)
-   Integrated feedback into design
-   Broke the project into milestones and hit deadlines for a conference demo

---

## Agile Project Management Experience

-   Led efficient and inclusive agile sprint ceremonies
-   Defined and prioritized deliverables for the Storyblocks enterprise growth team
-   Collaborated with technical and non-technical stakeholders (Product, Design, Analytics, Commercial)
-   Enabled engineer autonomy, ownership, and growth
-   Developed phased milestone strategies focused on incremental customer value
-   Fostered team learning and mentorship via 1:1s, growth plans, and reviews
-   Planned and executed a data migration for ~5,000 digital assets with enterprise clients

---

## Example 4

Dear \_\_\_ Hiring Team,

I’m excited to apply for the Technical Program Manager role supporting the **\_**. With 11+ years of experience delivering high-impact technical initiatives across engineering, product, and marketing teams, I bring a strong track record of aligning strategy with execution—especially in ambiguous, growth-focused environments.

I’m particularly inspired by Pinterest’s mission to help people create a life they love, and I’m eager to contribute to the systems that connect new users to that value.

At Storyblocks, I led a cross-functional initiative to develop an enterprise free trial platform, collaborating with sales, product, and engineering stakeholders to define milestones, manage technical risk, and deploy at scale. This effort directly accelerated our B2B sales cycle, shortening time-to-close for contracts exceeding $50K.

Earlier, at HelpTile, I co-founded and engineered a SaaS platform where I implemented end-to-end telemetry and user engagement analytics to support data-driven product development—experience that aligns well with Pinterest’s emphasis on SEO and campaign tooling.

I thrive in environments that require systems thinking, clear communication, and leadership without authority. I’ve led agile ceremonies, implemented change management processes, and guided technical audits—consistently fostering transparency, trust, and velocity across teams. Whether I’m driving roadmap execution, building new processes, or resolving cross-team dependencies, I bring both a proactive mindset and deep technical fluency that enable me to translate complexity into action.

Pinterest’s mission to inspire people and help them create a life they love deeply resonates with me. I believe in building technology that empowers and uplifts, and I’m excited by the opportunity to contribute to a platform that’s a positive, creative corner of the internet. The chance to help new users discover that value—and to do so while growing alongside a team that values innovation, empathy, and impact—would be incredibly meaningful.

I’d be thrilled to bring my technical leadership and cross-functional program experience to support that vision.

Thank you for considering my application—I look forward to the possibility of contributing to your team.

**Cheers,**  
Edward Kemper  
edwardkemper@gmail.com | (928) 514-7342 | Golden, CO  
[linkedin.com/in/edward-kemper-65929934](http://linkedin.com/in/edward-kemper-65929934)


Job Description:

"\nHere is the job description info in json: \n\n{\n  \"title\": \"Hardware System Technical Program Manager, Extended Reality Platform\",\n  \"name\": null,\n  \"company\": \"Google\",\n  \"location\": \"Mountain View, CA\",\n  \"via\": \"LinkedIn\",\n  \"posted\": \"4 days ago\",\n  \"salary\": null,\n  \"extensions\": [\n      \"4 days ago\",\n      \"Full-time\",\n      \"Health insurance\"\n  ],\n  \"detected_extensions\": {\n      \"posted_at\": \"4 days ago\",\n      \"schedule_type\": \"Full-time\",\n      \"health_insurance\": true\n  },\n  \"description\": \"Minimum qualifications:\\n\\u2022 Bachelor's degree or equivalent practical experience.\\n\\u2022 10 years of technical program management experience.\\n\\u2022 7 years of experience in leadership role(s) with/without direct reports.\\n\\nPreferred qualifications:\\n\\u2022 Experience with consumer electronics, developing and shipping reference platforms.\\n\\u2022 Knowledge of product life-cycle, tools, processes and development planning.\\n\\u2022 Ability to manage and prioritize multiple tasks at once.\\n\\u2022 Ability to lead technical teams, cross-functional groups, and vendors against plans.\\n\\u2022 Ability to travel internationally 20% of the time or more as needed.\\n\\u2022 Excellent written and verbal communication skills, with the ability to focus on key points.\\n\\nAbout The Job\\n\\nGoogle's projects, like our users, span the globe and require managers to keep the big picture in focus while being able to dive into the unique engineering challenges we face daily. As a Technical Program Manager at Google, you lead complex, multi-disciplinary engineering projects using your engineering expertise. You plan requirements with internal customers and usher projects through the entire project lifecycle. This includes managing project schedules, identifying risks and clearly communicating them to project stakeholders. You're equally at home explaining your team's analyses and recommendations to executives as you are discussing the technical trade-offs in product development with engineers.\\n\\nUsing your extensive technical and leadership expertise, you manage various Engineering-specific programs and teams.\\n\\nThe Google Augmented Reality team is a group of experts tasked with building the foundations for great immersive computing and building helpful, delightful user experiences. We're focused on making immersive computing accessible to billions of people through mobile devices, and our scope continues to grow and evolve.\\n\\nThe US base salary range for this full-time position is $227,000-$320,000 + bonus + equity + benefits. Our salary ranges are determined by role, level, and location. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.\\n\\nPlease note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google .\\n\\nResponsibilities\\n\\u2022 Define, drive, and own the overall system development process from concept to launch for extended reality (XR) reference platform hardware programs.\\n\\u2022 Balance schedule, performance, and user experience trade-offs.\\n\\u2022 Work with ODMs, OEMs, and vendors in manufacturing environments on development schedules, dependencies, and budgets.\\n\\u2022 Develop, maintain, and communicate key focus points and next steps with engineering, vendors, operations, quality, and management, improve and maintain processes that ensure team members have what they need to understand and execute on all objectives.\\n\\u2022 Identify risks, develop mitigation strategies and facilitate conflict resolution among a cross-functional team of engineers, and synthesize data into a clear story and communicate to stakeholders and organizations at all levels.\\n\\nGoogle is proud to be an equal opportunity workplace and is an affirmative action employer. We are committed to equal employment opportunity regardless of race, color, ancestry, religion, sex, national origin, sexual orientation, age, citizenship, marital status, disability, gender identity or Veteran status. We also consider qualified applicants regardless of criminal histories, consistent with legal requirements. See also Google's EEO Policy and EEO is the Law. If you have a disability or special need that requires accommodation, please let us know by completing our Accommodations for Applicants form .\",\n  \"share_link\": \"https://www.google.com/search?ibp=htl;jobs&q=Technical+Program+Manager&htidocid=K-YI-GL5OQ5kfqZHAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_yWOMQrCQBAAsc0TtNlaYiKCjVYiogiBoGJjETaX9XJyuQ13K0le5veM2AxTDRN9JtHjhL7q0BNchyDUwI1U7YxCC7ln7bGBDB1q8jEceiFXUQUXQmtkgNyiPNk3sIAzlxAIvaqBHRyZtaXpthZpwyZNQ7CJDoJiVKK4SdlRyX364jL8UIR6PGjHGhWr9bJPWqfns38EjIOM305wlLuhLob97guiPlAhugAAAA&shmds=v1_AQbUm95S81ohCxuTvqKH9FY-KvEbr4cb-t2aZk70MTwZt8x08g&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=Technical+Program+Manager&htidocid=K-YI-GL5OQ5kfqZHAAAAAA%3D%3D\",\n  \"job_highlights\": [\n      {\n          \"title\": \"Qualifications\",\n          \"items\": [\n              \"Bachelor's degree or equivalent practical experience\",\n              \"10 years of technical program management experience\",\n              \"7 years of experience in leadership role(s) with/without direct reports\"\n          ]\n      },\n      {\n          \"title\": \"Benefits\",\n          \"items\": [\n              \"The US base salary range for this full-time position is $227,000-$320,000 + bonus + equity + benefits\",\n              \"Our salary ranges are determined by role, level, and location\",\n              \"Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training\",\n              \"Your recruiter can share more about the specific salary range for your preferred location during the hiring process\",\n              \"Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits\"\n          ]\n      },\n      {\n          \"title\": \"Responsibilities\",\n          \"items\": [\n              \"You plan requirements with internal customers and usher projects through the entire project lifecycle\",\n              \"This includes managing project schedules, identifying risks and clearly communicating them to project stakeholders\",\n              \"You're equally at home explaining your team's analyses and recommendations to executives as you are discussing the technical trade-offs in product development with engineers\",\n              \"Using your extensive technical and leadership expertise, you manage various Engineering-specific programs and teams\",\n              \"Define, drive, and own the overall system development process from concept to launch for extended reality (XR) reference platform hardware programs\",\n              \"Balance schedule, performance, and user experience trade-offs\",\n              \"Work with ODMs, OEMs, and vendors in manufacturing environments on development schedules, dependencies, and budgets\",\n              \"Develop, maintain, and communicate key focus points and next steps with engineering, vendors, operations, quality, and management, improve and maintain processes that ensure team members have what they need to understand and execute on all objectives\",\n              \"Identify risks, develop mitigation strategies and facilitate conflict resolution among a cross-functional team of engineers, and synthesize data into a clear story and communicate to stakeholders and organizations at all levels\"\n          ]\n      }\n  ],\n\n\n}\n\n\n"
