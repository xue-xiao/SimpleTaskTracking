# SimpleTaskTracking
A task tracking system used in small organizations of multiple teams. Admin users can publish new tasks. Teams take a task, comment on the task and update status of the task.

# Deployment to Ubuntu 20.04 

## 0. Prerequisite
Ubuntu 20.04 LTS has python3.8 installed. 
But it has no git. 
Do this: `sudo apt-get install git`

## 1. Install nodejs

Reference: 
https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/
https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

```
$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

## 2. Download source
```
$ git clone https://github.com/xue-xiao/SimpleTaskTracking.git
$ cd SimpleTaskTracking/simple-task-tracking-vue/
$ npm install
$ npm run build
$ cd ../simple-task-tracking-flask/
$ sudo pip3 install pipenv
$ pipenv install
```

## 3. Run dev version
```
$ . $(pipenv --venv)/bin/activate
$ ./run-dev-server.sh
```
