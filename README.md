# CI/CD Pipeline Setup

## Objective
Deploy **Express (Node.js)** and **Flask (Python)** applications on AWS EC2 using Jenkins, Docker, GitHub Webhooks, and PM2.

---
## Documentation

- [Documentation](https://docs.google.com/document/d/1kPHjlIKQpuOuuUFcUKLj69pDIamMTepWk50qnEhWW44/edit?usp=sharing)
- [Github URL](https://github.com/ChetanaMali/fullstack-docker-project)

---
## Tools Used

| Tool | Purpose |
|------|---------|
| **AWS EC2** | Ubuntu server to host all services |
| **Jenkins** | CI/CD automation server |
| **Docker** | Containerization of frontend & backend apps |
| **GitHub** | Source code repository with webhook integration |
| **PM2** | Process manager to keep apps running after instance restart |

---

## Part 1 — EC2 Setup & Direct Deployment

### Steps Followed

```bash
# 1. Create an EC2 instance with Ubuntu AMI and SSH into it

# 2. Update the system
sudo apt update && sudo apt upgrade -y

# 3. Verify pre-installed tools
python3 --version
git -v

# 4. Install Node.js
sudo apt install nodejs -y

# 5. Clone the repository
git clone https://github.com/ChetanaMali/fullstack-docker-project

# 6. Install Backend dependencies (Flask)
cd Backend
pip install -r requirements.txt

# 7. Install Frontend dependencies (Express)
cd Frontend
npm install

# 8. Run apps manually to test
cd Frontend && npm start        # Express on port 3000
cd Backend && python app.py     # Flask on port 5000

# 9. Install PM2 globally
sudo npm install -g pm2

# 10. Start apps with PM2
cd Frontend && pm2 start server.js
cd Backend && pm2 start app.py
pm2 list
```

### Security Group Configuration

| Port | Protocol | Purpose |
|------|----------|---------|
| `22` | SSH | Remote access |
| `8080` | TCP | Jenkins |
| `3000` | TCP | Express (Node.js) |
| `5000` | TCP | Flask (Python) |
| `9000` | TCP | Express via Docker |
| `8000` | TCP | Flask via Docker |

---

### Express Deployment on EC2 (Port 3000)
- Deployed Express (Node.js) application directly on EC2 on port `3000`
- Used **PM2** as a process manager so the app keeps running even after the instance restarts

---

### Flask Deployment on EC2 (Port 5000)
- Deployed Flask (Python) application directly on EC2 on port `5000`
- Used **PM2** to keep the Flask app running persistently after instance restart

---

## Part 2 — Jenkins + Docker CI/CD Pipeline

### Jenkins Installation
- Created a GitHub Gist with all steps and commands to install Jenkins
-  https://gist.github.com/ChetanaMali/849f4a01ee49d42fdc879593e0f475bb

---

### Docker Installation
- Created a GitHub Gist with all steps and commands to install Docker
- https://gist.github.com/ChetanaMali/16a7f4199814298fff132a3403563f93

---

### Add Jenkins User to Docker Group

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

### GitHub Webhook Integration
- Configured GitHub webhook to automatically trigger Jenkins pipeline on every `git push`
- Jenkins job → **Build Triggers** → ✅ GitHub hook trigger for GITScm polling

---

### Flask Pipeline — Freestyle
- Created a **Freestyle pipeline** in Jenkins for the Flask application
- Connected GitHub repository and enabled webhook trigger to automate deployment

---

### Express Pipeline — Jenkinsfile

- Created a **Pipeline job** in Jenkins for the Express application
- Created a `Jenkinsfile` inside the project repository
- Provided the Jenkinsfile location in the Jenkins pipeline configuration

```groovy
pipeline {
    agent any
    stages {
        stage('Stop & Remove Old Container') {
            steps {
                sh '''
                    docker stop frontend || true
                    docker rm frontend || true
                '''
            }
        }
        stage('Build Image') {
            steps {
                sh 'cd $WORKSPACE/Frontend && docker build -t frontend .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 9000:3000 --name frontend frontend'
            }
        }
    }
}
```

---

### Express Deployment using Docker (Port 9000)
- Containerized the Express app using Docker
- Deployed on port `9000` to verify Docker-based deployment works independently
- Used Jenkins pipeline to fully automate the build and deployment process

---

### Flask Deployment using Docker (Port 8000)
- Containerized the Flask app using Docker
- Deployed on port `8000` to verify Docker-based deployment works independently
- Used Jenkins pipeline to fully automate the build and deployment process

---

## Pipeline Flow

```
Git Push → GitHub Webhook → Jenkins Triggers
                ↓
          Pull Latest Code
                ↓
    Stop & Remove Old Container
                ↓
        Build Docker Image
                ↓
        Run New Container
                ↓
          App Live on EC2
```

---

## Issues Faced & Resolved

| Issue | Solution |
|-------|----------|
| Docker permission denied in pipeline | Added `jenkins` user to `docker` group |
| Dockerfile not found in pipeline | Used `cd $WORKSPACE/Frontend` in shell script |


---

## Result

Successfully deployed both Express and Flask applications on AWS EC2 using two approaches:

- ✅ **Direct deployment** with PM2 for process persistence
- ✅ **Docker-based deployment** with Jenkins CI/CD pipeline triggered automatically via GitHub webhooks
