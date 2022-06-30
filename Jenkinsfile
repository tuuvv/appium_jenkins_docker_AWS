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
                sh 'python3 -m pytest --html=report/report.html --css=report/highcontrast.css --css=report/accessible.css --self-contained-html test_crollview.py'
                }
            }
        }
        stage('Update GIT') {
          steps {
            script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withCredentials([usernamePassword(credentialsId: '111222333', 
                    passwordVariable: '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', usernameVariable: 'vuvantuu@gmail.com')]) {
                        sh "git config user.email vuvantuu@gmail.com"
                        sh "git config user.name tuuvv"
                        sh "git add ."
                        sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
                        sh "git push https://tuuvv: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@github.com/tuuvv/appium_jenkins_docker_AWS.git"
                    }
                }
              }
          }
        }
    }
}
