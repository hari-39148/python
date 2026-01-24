pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
