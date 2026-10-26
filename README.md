# Task 4: CI/CD Pipeline with GitHub Actions and Docker

## Project Overview
This project demonstrates a CI/CD pipeline using GitHub Actions and Docker.
Python unit tests run automatically, and the Docker image is built and
published to Docker Hub when code is pushed to the main branch.

## Technologies Used
- Python
- Docker
- Docker Hub
- GitHub Actions
- AWS EC2
- Ubuntu Linux

## Application Features
- Web application homepage
- Health check endpoint
- Automated Python unit tests
- Automated Docker image build and push
- Deployment using Docker on EC2

## Project Links
- Live Application: http://3.92.147.165/
- Health Check: http://3.92.147.165/health
- GitHub Repository: https://github.com/chinnu9729/task4-cicd-github-actions-docker
- Docker Hub: https://hub.docker.com/r/chinnu9729/task4-cicd-app
- GitHub Actions: https://github.com/chinnu9729/task4-cicd-github-actions-docker/actions

## Run the Docker Image

Pull the image:

    docker pull chinnu9729/task4-cicd-app:latest

Run the application:

    docker run -d --name task4-cicd-app -p 8080:3000 chinnu9729/task4-cicd-app:latest

Open http://localhost:8080/ in your browser.

## Run Python Tests

    python3 -m unittest discover -s tests -v

## Screenshots
| Screenshot No. | File Name | Description |
|---|---|---|
| SS 0 | Screenshot0-EC2-Third-Instance.png | EC2 third instance details |
| SS 1 | Screenshot1-Live-App.png | Live application deployed on EC2 |
| SS 2 | Screenshot2-Health-Check.png | Application health endpoint response |
| SS 3 | Screenshot3-GitHub-Actions-Run1.png | Initial successful GitHub Actions workflow |
| SS 4 | Screenshot4-GitHub-Actions-Run2.png | Successful Fix URL query parameter routing workflow |
| SS 5 | Screenshot5-Docker-Hub.png | Docker Hub repository and latest image tag |
| SS 6 | Screenshot6-EC2-Docker.png | Running Docker container and health check |
| SS 7 | Screenshot7-Source-Code.png | GitHub repository source code |

