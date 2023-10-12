node {
    stage('Get source'){
        git('https://github.com/jahp87/flaskhello.git')
        if(!fileExists("Dockerfile")){
            error('Dockerfile not found')
        }
    }
    stage('Build Docker'){
        sh("docker build flaskhello") 
    }
    stage('Running image'){
        sh("docker run -d --name=flaskhello -p 8080:8080 flaskhello")
    }

}