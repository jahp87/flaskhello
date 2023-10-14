pipeline {
    agent any    
    stages {
        
        stage('Build Main') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo Building Docker Image...'
                sh 'comando sh o llamada a un script sh'
            }             
        }
        stage('Build Dev')
        {
            when {
                branch 'dev'
            }
            steps {
                sh 'echo Building Docker Image...'
                sh 'comando sh o llamada a un script sh'
            }
        }
        stage('Deploy Main') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying.... '
                echo 'Running Container...'
                sh 'comando sh o llamada a un script sh'
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
                sh 'comando sh o llamada a un script sh'
            }
        }
              
    }
}