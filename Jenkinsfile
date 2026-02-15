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
				sh 'docker run --rm -v $PWD:/output comisiones-app'
			}
		}
		
        stage('Verify Artifact') {
            steps {
                sh 'ls -lh'
            }
        }
		
        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'comisiones.xlsx', fingerprint: true
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
