pipeline {
    agent any

    stages {
    
        stage("Debug Env") {
            steps {
                sh 'which python'
                sh 'which pip'
                sh 'python --version || python3 --version'
                sh 'pip --version || pip3 --version'
            }
        }

        stage("Install") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage ("Test") {
            steps {
                sh 'pytest'
            }
        }

    }
}
