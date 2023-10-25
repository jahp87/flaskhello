pipeline {
    agent any    
    stages {
        
        stage('Build Main') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo Building Docker Image...'
                sh 'docker build -t flaskhello .'
            }             
        }
        stage('Build Dev')
        {
            when {
                branch 'dev'
            }
            steps {
                sh 'echo Building Docker Image...'
                sh 'docker build -t flaskhello -f docker/Dockerfile .'
            }
        }
        stage('Deploy Main') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying.... '
                echo 'Running Container...'
                sh "docker stop flaskhello | docker rm flaskhello | true "
                sh "docker run -d --name=flaskhello -p 8000:5000 flaskhello" 
            }            
        }
        stage('Deploy Dev')
        {
            when {
                branch 'dev'
            }
            steps {
                echo 'Deploying.... '
                echo 'Running Container...'
                sh "docker stop flaskhello | docker rm flaskhello | true "
                sh "docker run -d --name=flaskhello -p 8000:5000 flaskhello" 
            }
        }
              
    }
}