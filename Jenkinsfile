pipeline {
    agent { docker { image 'python:3.9-alpine' } }
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
    post {
        failure {
            mail to: 'chandler@chandlerswift.com.com',
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Something is wrong with ${env.BUILD_URL}"
        }
    }
}
