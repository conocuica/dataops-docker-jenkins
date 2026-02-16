pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t comisiones-app .'
            }
        }

		stage('Run Container') {
			steps {
				sh 'docker run --rm comisiones-app'
			}
		}
		
        stage('Verify Artifact') {
            steps {
                sh 'ls -lh'
            }
        }

    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
}
