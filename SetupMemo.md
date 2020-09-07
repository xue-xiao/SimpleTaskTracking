# Setup initial Vue and Flask development environment on Mac

## 1. Install node & npm 
https://nodejs.org/en/ 
Download LTS version 

## 2. Install Vue CLI 

```
$ sudo npm install -g @vue/cli
```
 
Ref: https://cli.vuejs.org/guide/installation.html 

## 3. Create github repo and clone to local workspace

```
$ git clone https://github.com/xue-xiao/SimpleTaskTracking.git
```

## 4. Create new vue project

```
$ cd SimpleTaskTracking
$ vue create simple-task-tracking-vue 
```

It will ask for Vue version. 
Vue3.0 is a preview version as of 9/6/2020.
I tried it first but found vue-bootstrap doesn't support Vue3.0 yet. 
So I decided to stay with the mature Vue2.x for now and may upgrade it later.  

## 5. Add router

```
$ cd simple-task-tracking-vue
$ vue add router 
```

Ref: https://router.vuejs.org/installation.html#npm 

I selected [history mode](https://router.vuejs.org/guide/essentials/history-mode.html) for prettier url looking.

## 6. Run it to verify Vue works 

```
$ vue run serve 
```
## 7. Create pipenv environment for python

```
$ cd ..
$ mkdir simple-task-tracking-flask 
$ cd simple-task-tracking-flask 
$ pipenv install 
```

If you never install `pipenv`, run once: `pip3 install pipenv` 

## 8. Install some flask dependencies 
 
```
$ pipenv install flask flask_sqlalchemy flask-login 
```

## 9. Update .gitignore

I used python template when creating the repo on Github.
Now I want to add more things to it.

```
.idea
*.iml
.DS_Store 
```

## 9. Time to commit! 

Optionally, configure the repo's local git account

```
$ cd ..
$ git config user.name "Xue Xiao"
$ git config user.email xue-xiao@users.noreply.github.com
$ git config credential.helper cache
$ git config --global credential.usehttppath true
```

## 10. Commit the change and push!

```
$ git add -A
$ git commit -am"Initialize Vue and Flask environment"
$ git push
```

## 11. Add bootstrap to vue

```
$ cd simple-task-tracking-vue
$ vue add bootstrap-vue
```
Ref: https://bootstrap-vue.org/docs#vue-cli-3-plugin


