pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Akanksha\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install --upgrade pip'
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m pytest test_app.py -v'
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
