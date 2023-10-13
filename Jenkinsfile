pipeline {
    agent any
    stages{
        stage('Build Docker'){
        sh("docker build -t flaskhello/flaskhello .") 
        }
        stage('Running image'){
            sh('docker stop flaskhello | docker rm flaskhello | true ')
            sh("docker run -d --name=flaskhello -p 8000:5000 flaskhello")
        }
    }
    

}