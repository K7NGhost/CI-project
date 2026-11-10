pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    triggers {
        githubPush()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest discover -s tests -v'
                    } else {
                        bat 'python -m unittest discover -s tests -v'
                    }
                }
            }
        }
        stage('Run application') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 app.py'
                    } else {
                        bat 'python app.py'
                    }
                }
            }
        }
    }
}
