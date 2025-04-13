pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[
                              url: 'https://github.com/sah1l-17/flask-todo-app.git',
                              credentialsId: 'github-token'
                          ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("flask-todo-app")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run("-d -p 5000:5000")
                }
            }
        }
    }
}
