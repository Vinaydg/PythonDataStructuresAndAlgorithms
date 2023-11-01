pipeline {
    agent { docker { image 'python:3.12.0-alpine3.18' } }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
