pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm  // 👈 Simplified checkout
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("flask-todo-app").inside("--network host") {
                        // Optional: Run tests inside the container
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("flask-todo-app").run("-d -p 5000:5000")
                }
            }
        }
    }
}
