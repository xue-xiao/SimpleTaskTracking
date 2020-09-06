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

I love to try new technologies in personal project. 
So I selected vue3.0, which is a preview version as of 9/6/2020.
In addition, I selected [history mode](https://router.vuejs.org/guide/essentials/history-mode.html) for prettier url looking.

## 5. Add router

```
$ cd simple-task-tracking-vue
$ vue add router 
```

Ref: https://router.vuejs.org/installation.html#npm 

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
$ git config user.password "your password"
```

Commit the change and push!

```
$ git add -A
$ git commit -am"Initialize Vue and Flask environment"
$ git push
```
