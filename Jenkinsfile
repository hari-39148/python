pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'python --version || python3 --version'
                sh 'pip --version || pip3 --version'
                sh 'pip install -r requirements.txt || pip3 install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh 'python app.py || python3 app.py'
            }
        }
    }
}
