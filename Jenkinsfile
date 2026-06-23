pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }
        stage('Build & Test') {
            steps {
                echo 'Running Python Script Test...'
                sh 'python3 app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Local Production Directory...'
                // 로컬의 특정 배포 디렉토리로 복사하는 예시
                sh 'mkdir -p /tmp/deployed_app'
                sh 'cp app.py /tmp/deployed_app/'
            }
        }
    }
}
