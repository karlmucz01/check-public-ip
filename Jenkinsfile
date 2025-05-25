pipeline {
    agent any

    stages {
    
        stage("Install") {
            sh 'pip install -r requirements.txt'
        }

        stage ("Test") {
            steps {
                sh 'pytest'
            }
        }

    }
}
