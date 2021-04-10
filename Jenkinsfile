pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run monitoring') {
            steps {
                sh 'pytest'
            }
        }
    }
}
