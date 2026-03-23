# devops_exam
In the fourth semester of my studies at University in Adger, we had a subject "DevOps". This repository is what was delivered as the exam submission. The only thing removed are the individual reports from the other team members.

## Exam requirements

### Introduction

The following was what was given to students:

You have been hired to consult Auby & Brinch Finance in their plans to improve and expand their development team. The job description from the business is fairly general, so it's up to your team to present what you think is important and relevant.

Auby & Brinch Finance is a company consisting of ~70 general employees and 3 software developers. The plan is to expand the current software development team to ~5 people within 3 months and another team of ~5 within 12 months. The software team as it stands now consists of general developers with little DevOps experience. One developer has the role of leader, the other two are general developers.

The software being developed is used in house by the rest of the employees. The software is a web site to manage employees, customers and jobs. The software is crucial to the operation of the business and will play an important role as the company grows.

They use a self-hosted instance of GitLab EE as git repository and have prepared a Kubernetes installation to host the application

Link to the software source code (use this for setup and modifications): https://github.com/XD-DENG/flask-exampleLenker til en ekstern side.

(obviously this is not the software described in the imagined setting above, but let's pretend...)

Current working practices for the development team is as follows:

- The team meets on Mondays to discuss the plan for the week
- Each team member writes down the tasks they will do this week
- Each developer works on their own machine and submits changes to the main branch
- At the end of the week, the team leader manually tests the software and transfers the new release to the internal server
- The team is not using any tools other than the development IDE and email. Bugs and issues are handled as they are reported.

Your task is to analyze the team's working practices and compare them to current best practices in the field. The company will use your analysis and recommendations as a base for improving their working practices and for staffing up the teams. The team wishes for a working DevOps setup with their application as a reference.  would like your assistance in doing so.

### Solution requirements

- Automated testing with test coverage
- Automated deployment to staging environment
- Automated deployment to production environments with manual approvement
- Both staging and production environment hosted in Kubernetes as separate namespaces
- Development should use an SQLite database for simplicity
- Staging and production should use a postgres database
- Staging and production should use Gunicorn (https://gunicorn.org/Lenker til en ekstern side.)
- Source code should not be stored in the container hosted in Kubernetes
- Container images should be stored in GitLab container registry
- Local GitLab EE must be used for git repository
- Local Kubernets must be used for hosting the application

### Presentation requirements

The presentation should cover the following topics:

- Introduction
- What is DevOps? A general introduction to the team
- Analysis
- Risks and weak points of the current working practices
- A description of the new setup
- Suggested workflow using this setup
- Demo: Short demonstration of a change going from code to production
- Your team is free to add any additional topics you deem important. Make sure to explain both the why and how.

The audience of the presentation is the management and develop team of the company described earlier.

## What you can find in this repository

As stated before, you will find our exam submission. This consists of:

- Link to presentation video
- Presentation PPT
- Process Guide (explanation on the developed solution)
- Setup Guide (how to set up the solution)
- Appendices which include:
  * the configured flask application with tests
  * My individual report detailing how I contributed to the project
  * Configuration files needed for the solution
