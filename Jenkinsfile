pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh 'venv/bin/python -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t mini:latest .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker stop -f mini-devops-project || true'
                sh 'docker rm -f mini-devops-project || true'                
                sh 'docker run -d -p 5000:5000 --name mini-devops-project mini:latest'
            }
        }

        stage('Health Check') {
            steps {
               sh 'sleep 5' 
               sh 'curl --fail http://localhost:5000/health'
            }
        }
    }
}
