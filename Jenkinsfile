Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                retry(3) {
                    bat 'awscli --version'
                }
                retry(2) {
                    bat 'python --version'            
                }
            }    
        }
    }
}
