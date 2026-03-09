pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install --upgrade pip'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'py -m pytest test_app.py -v'
            }
            post {
                failure { echo 'Tests failed!' }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t flask-app:${BUILD_NUMBER} ."
            }
        }
    }

    post {
        always { echo 'Pipeline completed' }
        success { echo 'Pipeline succeeded!' }
        failure { echo 'Pipeline failed!' }
    }
}
