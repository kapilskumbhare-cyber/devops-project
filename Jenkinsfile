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
                sh 'docker build -t mini:${BUILD_NUMBER} .'
            }
        }
       stage('Docker Push') {
           steps {
               withCredentials([usernamePassword(
               credentialsId: 'dockerhub-credentials',
               usernameVariable: 'DOCKER_USER',
               passwordVariable: 'DOCKER_PASS'
           )]) {
                sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                sh 'docker tag mini:${BUILD_NUMBER} $DOCKER_USER/mini-devops-app:${BUILD_NUMBER}'
                sh 'docker tag mini:${BUILD_NUMBER} $DOCKER_USER/mini-devops-app:latest'
                sh 'docker push $DOCKER_USER/mini-devops-app:${BUILD_NUMBER}'
                sh 'docker push $DOCKER_USER/mini-devops-app:latest'
        }
    }
}


       stage('Docker Compose Deploy') {
            steps {
                  sh '''
                    export IMAGE_TAG=${BUILD_NUMBER}
                    docker compose pull web
                    docker compose up -d --force-recreate web
                     '''
    }
}

        stage('Health Check') {
            steps {
               sh 'sleep 5' 
               sh 'curl --fail http://localhost:5000/health'
     }     
}
        stage('Deploy to EC2') {
             steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ec2-ssh-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ])  {
            sh '''
                ssh -o BatchMode=yes \
                -o StrictHostKeyChecking=accept-new \
                -i "$SSH_KEY" \
                "$SSH_USER@3.27.135.19" \
                'whoami'
               '''
        }                
     }
 }
        stage('EC2 Health Check') {
             steps {

     }
  }

    }
}
