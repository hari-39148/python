pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
