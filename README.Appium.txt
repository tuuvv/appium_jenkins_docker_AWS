Soft====================================================================================
1. Cài đặt appium-server: Appium-windows-1.18.2.exe (C:\Program Files (x86)\Appium)
2. Cài đặt appium-server trên katalon
2.1 Cài đặt nodejs: C:\Program Files\nodejs
2.2 Kiểm tra version: node --version
2.2 Cài đặt appium: npm install -g appium
2.3 Mở Katalon, add appium: Windows->Preferences->Katalon->Mobile->Appium Directory
C:\Users\vuvan\AppData\Roaming\npm\node_modules\appium
AppiumSession=============================================================================
1. Mở cmd trong folder chứa apk
2. Lấy tên device: adb devices 
name: R9YRA0QGAXN
3. Cài ứng dụng lên máy: adb install com.theyield.sensingplusv2.apk
Env=====================================================================================
cài adroid studio
cài JDK
ATLAN_ANDROID C:\Users\vuvan\AppData\Local\Android\Sdk

%ATLAN_ANDROID%\emulator
%ATLAN_ANDROID%\tools
%ATLAN_ANDROID%\tools\bin
%ATLAN_ANDROID%\platform-tools

4. Lấy thông tin ứng dụng: Mở app -> login app -> adb shell "dumpsys window | grep mCurrentFocus"
appPackage:
appWaitActivity:
5. Mở appium-server: start server -> start inspector session (kính lúp)
6. Appium needs to know package and activity names in order to properly initialize the application under test. This information is expected to be provided in driver capabilities and consists of the following keys:
	appActivity: The name of the main application activity
	appPackage: The identifier of the application package
	appWaitActivity: The name of the application activity to wait for/which starts the first
	appWaitPackage: The id of the application package to wait for/which starts the first
	appWaitDuration: The maximum duration to wait until the appWaitActivity is focused in milliseconds (20000 by default)
	appWaitForLaunch: Whether to wait until Activity Manager returns the control to the calling process. By default the driver always waits until appWaitDuration is expired. Setting this capability to false effectively cancels this wait and unblocks the server loop as soon as am successfully triggers the command to start the activity.
7. Input JSON Representation -> save -> start session
{
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "BRG00056992",
  "fullReset": "true",
  "appPackage": "com.theyield.sensingplusv2",
  "appWaitActivity": "crc64f031137d8312bd18.MainActivity",
  "app": "C:\\Users\\vuvan\\PycharmProjects\\PytestBDD_framework\\Yield\\Appium\\com.theyield.sensingplusv2.apk"
}
{
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "R9YRA0QGAXN",
  "fullReset": "true",
  "appPackage": "com.swaglabsmobileapp",
  "appWaitActivity": "com.swaglabsmobileapp.MainActivity",
  "app": "C:\\Users\\vuvan\\PycharmProjects\\PytestBDD_framework\\Yield\\Appium\\Android.SauceLabs.Mobile.Sample.app.2.1.0.apk"
}
{
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "R58R332YAYL",
  "fullReset": "false",
  "appPackage": "com.code2lead.kwad",
  "appWaitActivity": "com.code2lead.kwad.MainActivity",
  "app": "C:\\Users\\vuvan\\OneDrive\\Documents\\apium\\demotest\\source\\Android_Demo_App.apk"
}

//////--------Allure-------------///////

pip install pytest
pip install allure-pytest
ấn link tải allure về để thiết lập môi trường tạo server allure

https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.8.1/allure-commandline-2.8.1.zip
giải nén copy vào ổ C

tạo biến môi trường vào path C:\allure\bin
chạy lệnh
npm install -g allure-commandline --save-dev

chạy lệnh để chạy hết tất cả test case và lấy báo cáo
py.test --alluredir=%allure_result_folder% ./tests 
cd vào thư mục tests chạy từng test case
py.test --alluredir=allure_result_folder -v -s test_file_name.py
chạy lệnh để tạo server
allure serve C:\Users\vuvan\OneDrive\Documents\apium\demotest\tests\allure_result_folder

///------jenkins-------///

https://www.youtube.com/watch?v=E6yxYQUs670
cài lại JDK 11 trong soure vì jenkins chỉ hỗ trợ jdk11 thay lại JAVA_HOME trong môi trường C:\Program Files\Java\jdk-11.0.15



start cmd fix: java -jar C:\Users\vuvan\OneDrive\Documents\apium\demotest\source\jenkins.war --httpPort=8080
truy cập localhost:8080
thông tin : copy token dán vô
chọn select pluins to install, mục buildtools (2/4) bỏ chọn ant và Gradle click install. đặt tài khoản admin. click tới khi start using Jenskin
user: vuvantuu, pass: bean1991, mail : vuvantuu@gmail.com

b1: ấn newItem đặt tên project. click freestyle project ấn ok
b2: ấn advance, check ô use custom workspace điền vào đường dẫn thư mục tests của dự án ví dụ:
C:\Users\vuvan\OneDrive\Documents\apium\demotest\tests
b3: mục build chọn Execute Windows batch command
b4: nhập lệnh build như dưới local :  py.test --alluredir=C:\Users\vuvan\OneDrive\Documents\apium\demotest\tests\allure_result_folder test_crollview.py ấn save
b5: Jenkins -> Manage Jenkins -> Configure System -> Global properties -> Environment variables
name: path. value C:\Users\vuvan\AppData\Local\Programs\Python\Python310 ấn save , ấn nhấn jenkins.exe restart
b6: tải lại browser ấn Build Now ở menu trái
b7: đẳ chiến dịch chọn build Trigger -> build periodically ấn dấu hỏi để biết cách đặt cronjob tự động chạy
dấu * nghĩa là bỏ qua. có năm vị trí phút (vd: H/15 mỗi mười lăm phút), (vd: 9-16/2 mỗi 2 giờ từ 9AM tới 4 PM)giờ,(vd: 1,15 ngày 1 và ngày 15 hàng tháng) ngày trong tháng,(VD:1-11 từ tháng 1 tới tháng 11) tháng, (vd: 1-5 các ngày trừ T7 và CN))và ngày trong tuần
Vd: 15 8-15/2 1 * 1-3 mỗi hai giờ từ 8h15 tới 15h15 ngày một hàng tháng các ngày từ thứ hai tới thứ 4.


//////////////////////-----MACOS--------//////////////////////////
b1:install python3
check: python3 --version
check: pip3 --version
b2: install appium
b3: install appium inspector
b4: install android studio
b5: cài SDK adroid 11, 10, 5.1 và 5
b6: echo $SHELL
b6: terminal gõ vim ~/.zshrc
b7: ấn I, gõ export ANDROID_HOME=/Users/thanhvu/Library/Android/sdk
VÀ export PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools"
ấn esc :wq!
b8: source ~/.zshrc
b9: install java
b10: terminal gõ vim ~/.zshrc
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-11.0.15.jdk/Contents/Home
b11: start appium -> Edit configurations-> điền javahome và androidhome
b12:pycharm project chọn lại thư mục python3 tại  system intepreter


-----------Docker tại localhost---------------
b1: touch Dockerfile
FROM python:3.8.8

RUN mkdir /appium

COPY ./ /appium

COPY ./requirements.txt /appium

WORKDIR /appium
RUN pip install pip --upgrade &&  pip install -r requirements.txt

------------------------------
[Appium-Python-Client
pytest
pytest_bdd==5.0.0
requests
allure-pytest
pytest-html
]
--------------------------------
b2: pip freeze lấy list cho vào setup.py
b3: docker build -t ten_images .
b4: docker images
b5:  docker run -d -p 8000:8000 -p 50000:50000 ten_iamges
b6: docker ps -a
docker run -it ten_iamges /bin/bash
b7: cd tests
b8:pytest --junitxml=allure_result_folder/unittests.xml  test_crollview.py

b7:remove images: docker builder prune
-----------------------------AWS------------------------------------
EC2
b1: tải first_linux tạo bước tạo key
b2:ssh -i "first_linux.pem" ec2-user@ec2-3-15-43-145.us-east-2.compute.amazonaws.com
b3: update packages   sudo yum update
b4: sudo amazon-linux-extras install java-openjdk11
------------cài jenkin--------------
b1: sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
b2: sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
b3: sudo yum install jenkins -y  (chọn cái này)
sudo systemctl enable jenkins
b4: sudo systemctl start jenkins
sudo service jenkins start(chọn cái này)
đợi nó hiện ok
b5: lên EC2 chọn Actions-> networking -> change security groups add default. Tại instance click vào default chọn edit inbound ruler
chọn custom TCP chọn range 8080 save
b6:whoami
sudo su -
whoami khi là root user thì ok
b7: cd /var/lib/jenkins/secrets
cat initialAdminPassword
b8:stop:  sudo service jenkins stop
sudo service jenkins restart

b9: uninstall : sudo service jenkins stop
sudo yum remove jenkins
sudo rm -r /var/lib/jenkins
b10: chọn pipeline khi tạo item create

-----------cài git---------------
b1: git --version
b2: sudo yum update
b3: sudo yum install git
b4: git --version
b5: which git
---------------GIT-----------------------
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 github khóa 90 ngày vuvantuu@gmail.com
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 tuuvv

--------------Pipepile-----------------
tại dự án jenkinsfileCloneRepo -> chọn Pipeline Syntax
A> clone code vào AWS
b1: sample Step chọn git:GIT
b2: dán Repository URL chọn main, chọn xác thực
b3: generate được git branch: 'main', credentialsId: '20021991', url: 'https://github.com/tuuvv/appium_jenkins_docker_AWS'
b4: tại pipeline dán code :
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
         stage('CloneRepo') {
            steps {
                echo 'Hello World'
                git branch: 'main', credentialsId: '20021991', url: 'https://github.com/tuuvv/appium_jenkins_docker_AWS'
            }
        }
    }
}
B>Cài docker lên EC2
b1: kết nối EC2 bằng ssh
b2: sudo yum update -y ->  sudo amazon-linux-extras install docker
b3: sudo groupadd docker
b4: sudo usermod -aG docker $USER
b5: Ctrl +C, -> exit
b6: kết nối Lại bằng ssh
b7: sudo service docker start
b8: cd /var/lib/jenkins/workspace/
b9: cd jenkinsfileCloneRepo
b10: -> b7 ->chạy lại như dưới local
C>chạy trên jenkins
b1: tạo project chọn pipeline
b2:
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
                dir('/var/lib/jenkins/workspace/jenkinsfileCloneRepo'){
                sh 'docker build -t aws_docker .'
                sh 'docker run -it aws_docker /bin/bash'
                sh 'cd tests'
                sh 'ls -l'
                sh 'pytest --junitxml=allure_result_folder/unittests.xml test_crollview.py'
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
b3: sudo usermod -aG docker jenkins
sudo service jenkins restart
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
------------------Allure ------------------------
----install Nonejs
b1: curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
b2: sudo yum install -y nodejs
b3: mkdir allure
cd allure
wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip

sudo apt install unzip -y
unzip allure-2.13.8.zip
b4:sudo su -
b5: npm install -g allure-commandline --save-dev
------------------HTML report and push back to github-------------------
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
