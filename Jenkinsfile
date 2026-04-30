pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t c3-fastapi-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f c3-fastapi-container || true
                docker run -d -p 8000:8000 --name c3-fastapi-container c3-fastapi-app
                '''
            }
        }

        stage('Test App') {
            steps {
                sh '''
                sleep 3
                curl http://localhost:8000/
                '''
            }
        }
    }
}