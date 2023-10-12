pipeline {
    agent any
    stage('Get source'){
        git('https://github.com/jahp87/flaskhello.git')
        if(!fileExists("Dockerfile")){
            error('Dockerfile not found')
        }
    }
    stage('Build Docker'){
        sh("docker build -t flaskhello .") 
    }
    stage('Running image'){
        sh('docker stop flaskhello || docker rm flaskhello || true ')
        sh("docker run -d --name=flaskhello -p 80:5000 flaskhello")
    }

}