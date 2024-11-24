pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            steps {
                sh 'docker build -t client:latest -f docker/Dockerfile.client .'
                sh 'docker build -t server:latest -f docker/Dockerfile.server .'
                sh 'docker build -t mongodb:latest -f docker/Dockerfile.mongodb .'
            }
        }
        stage('Push Images') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-password', variable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u myusername --password-stdin'
                    sh 'docker tag client:latest myusername/client:latest'
                    sh 'docker push myusername/client:latest'
                    sh 'docker tag server:latest myusername/server:latest'
                    sh 'docker push myusername/server:latest'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}
