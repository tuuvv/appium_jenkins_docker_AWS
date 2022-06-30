pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                 git branch: 'main', credentialsId: '111222333', url: 'https://github.com/tuuvv/appium_jenkins_docker_AWS'
            }
        }
        stage('Test') {
            steps {
                dir('/var/lib/jenkins/workspace/run_by_hand/tests'){
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest --junitxml=allure_result_folder/unittests.xml test_crollview.py'
                }
            }
        }
        stage('Product') {
            steps {
                echo 'waiting for QA'
            }
        }
    }
}
