pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py -v'
            }
            post {
                failure { echo 'Tests failed!' }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        always { echo 'Pipeline completed' }
        success { echo 'Pipeline succeeded!' }
        failure { echo 'Pipeline failed!' }
    }
}
