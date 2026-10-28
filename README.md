# Smart Deployment Checker for Kubernetes Cluster 🚀

## About the Project

This is a mini DevOps project I built to understand how an application can be tested, packaged, and deployed using different DevOps tools.

The project uses a simple Python Flask application. Before deploying it, I use Pytest to check whether the application is working correctly. Then, I package the application into a Docker image and deploy it to a Kubernetes cluster using Minikube.

The application displays a deployment success message and provides a health-check endpoint to verify that it is working properly.

## What I Wanted to Learn

- How to test an application automatically using Pytest.
- How to package an application using Docker.
- How to deploy an application on Kubernetes.
- How to check the status of pods and services.
- How testing can help identify problems before deployment.

## Tools and Technologies

- Python
- Flask
- Pytest
- Docker
- Kubernetes
- Minikube
- Ubuntu on WSL

## Project Features

- A simple webpage showing deployment status.
- Automated tests to check application functionality.
- A health-check endpoint that returns the application's status.
- Docker image creation for running the application in a container.
- Kubernetes deployment with two application replicas.
- A Kubernetes Service to access the application through a browser.

## Project Structure

```text
smart-deployment-checker/
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/sumyukthayarragudi/SmartDeploymentChecker.git
cd SmartDeploymentChecker
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the tests

```bash
python -m pytest -v
```

The project includes three tests to check the home page, health endpoint, and invalid page response. All tests should pass before continuing.

### 5. Start Minikube

Make sure Docker Desktop is running and Ubuntu integration is enabled.

```bash
minikube start --driver=docker
```

### 6. Build the Docker image

```bash
minikube image build -t smart-checker:latest .
```

### 7. Deploy the application

```bash
minikube kubectl -- apply -f deployment.yaml
```

Wait for the deployment to finish:

```bash
minikube kubectl -- rollout status deployment/smart-deployment
```

### 8. Check the deployment

```bash
minikube kubectl -- get pods
minikube kubectl -- get services
```

### 9. Open the application

```bash
minikube service smart-checker-service
```

The application should open in your browser.

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Displays the deployment success page |
| `/health` | Checks the application's health status |

The health endpoint returns:

```json
{
  "status": "healthy"
}
```

## How It Works

1. The Flask application is created.
2. Pytest runs automated tests to check the application.
3. If a test fails, the issue should be fixed before deployment.
4. After successful testing, Docker builds the application image.
5. Kubernetes deploys the application to the Minikube cluster.
6. The pods and services are checked to verify the deployment.

Currently, the testing and deployment steps are performed manually. In the future, Jenkins can be added to automate the complete process.

## What I Learned

While working on this project, I learned how automated testing, Docker, and Kubernetes work together. I also gained practical experience with Docker image building, Kubernetes deployments, pods, services, and application health checks.

This project helped me understand the basic DevOps workflow and gave me a foundation for exploring CI/CD pipelines and deployment automation.

## Future Improvements

- Automate the workflow using Jenkins.
- Add a CI/CD pipeline to run tests before deployment.
- Include application monitoring and logging.
- Add notifications for failed tests or deployments.

---

**Project:** Smart Deployment Checker for Kubernetes Cluster  
**Domain:** DevOps

