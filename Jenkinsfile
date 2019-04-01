node {
    def app

    stage('Clone repository') {

      checkout scm
    }
        
    stage('Build image') {
        
        app = docker.build("web-scrapper")
    }
    
    stage('Push image') {
        
        def stand = "dev"
        docker.withRegistry('http://registry.com:5000') {
            app.push("${stand}")
       }
    }
 
}
