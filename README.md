# fullstack-docker-project

#Deploy Application on EC2 Instance
steps that i follow:
1. Create an EC2 instance with Ubuntu AMI.
2. DO SSH 
3. sudo apt update && apt upgrade -y
4. check Python3 --version & git
5. install node
6. git clone 
7. cd Backend -> pip install -r requirements.txt (install all requirements)
8. cd Frontend -> npm install (install all dependencies)
9. frountend -> npm start 
10. backend -> python app.py
11. sudo npm install -g pm2 (install pm2)
12.  cd Frontend/ -> ls ->  pm2 start server.js -> pm2 list
13. cd Backend/ -> pm2 start app.py -> pm2 list
14. Sec Group
    22	    SSH
    8080	Jenkins
    5000	Flask
    3000	Express


 python -version
    2  python --version
    3  python3 --version
    4  node --version
    5  git -v
    6  clear
    7  sudo npm install
    8  sudo node install
    9  sudo apt update
   10  sudo apt upgrade
   11  sudo apt install nodejs
   12  node -v
   13  git clone https://github.com/ChetanaMali/fullstack-docker-project.git
   14  ls
   15  cd fullstack-docker-project/
   16  ls
   17  cd bac
   18  cd Backend/
   19  ls
   20  sudo pip install -r requirement.txt
   21  pip
   22  sudo pip install
   23  python3 -m pip --version
   24  sudo apt update
   25  sudo apt install python3-pip -y
   26  df -h
   27  pip3 --version
   28  sudo pip install -r requirement.txt
   29  python3 -m pip install -r requirements.txt
   30  sudo apt update
   31  sudo apt install python3-venv -y
   32  cd flask-project
   33  python3 -m venv venv
   34  cd flask-project
   35  ls
   36  cd/`
cd/~
   37  cd/~
   38  cd ..
   39  cd fullstack-docker-project/
   40  python3 -m venv venv
   41  source venv/bin/activate
   42  pip install -r requirements.txt
   43  cd Backend/
   44  pip install -r requirements.txt
   45  ls
   46  pip install -r requirement.txt
   47  cd ..
   48  npm install
   49  sudo apt install npm
   50  cd Backend/
   51  ls
   52  python app.py
   53  cd ..
   54  cd Frontend/
   55  ls
   56  sudo npm install
   57  sudo npm start
   58  cd ..
   59  sudo npm install -g pm2
   60  cd Frontend/
   61  ls
   62  pm2 start server.js
   63  pm2 list
   64  cd ..
   65  cd Backend/
   66  pm2 start app.py
   67  pm2 list
   68  pm2 start --name backend
   69  pm2 --name backend
   70  pm2 list
   71  cd ..
   72  pm2 save
   73  pm2 startup
   74  history

   
#Jenkin CICD 