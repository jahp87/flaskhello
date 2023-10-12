pipeline {
    agent any
    stages {
        stage('Master Branch Deploy Code') {
           steps {
                 git('https://github.com/jahp87/flaskhello.git')
                 if(!fileExists("Dockerfile")){
                    error('Dockerfile not found')
                 }
            }
        }
        stage('Develop Branch Deploy Code') {
            when {
                branch 'develop'
            }
            steps {
                sh """
                echo "Building Artifact from Develop branch"
                """
                sh """
                echo "Deploying Code from Develop branch"
                """
           }
        }
    }
}