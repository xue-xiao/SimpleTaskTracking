<!-- Note:

Login page used bootstrap signin example page directly
https://getbootstrap.com/docs/4.0/examples/sign-in/

-->

<template>
    <div class="text-center">
        <form class="form-signin" @submit.prevent="submitCredentials">
            <img class="mb-4" src="../assets/logo.png" alt="">
            <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
            <ErrorAlert v-if="showError" v-bind:msg="errorMsg" v-on:close="showError=false"/>
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="email" v-model="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
            <label for="inputPassword" class="sr-only">Password</label>
            <input type="password" v-model="password" id="inputPassword" class="form-control" placeholder="Password" required>
            <div class="checkbox mb-3">
                <label>
                    <input type="checkbox" value="remember-me"> Remember me
                </label>
            </div>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-muted">&copy; 2020</p>
        </form>
    </div>
</template>

<script>

    import Axios from 'axios';
    import ErrorAlert from "../components/utils/ErrorAlert";

    export default {
        name: "Login",
        components: {ErrorAlert},
        beforeCreate() {
            // Note:
            // Vue scoped style cannot apply to `body` but we don't want to change the `body` style of other pages.
            // therefore we give this `body` a class so that we can specifically modify this page's body style.
            // Referenced: https://stackoverflow.com/a/44544595
            document.body.className = 'login';
        },
        data: () => ({
            showError: false,
            errorMsg: "",
            email: "",
            password: ""
        }),
        methods: {
            submitCredentials() {
                const user_cred = {
                    email: this.email,
                    password: this.password
                }
                this.password = "";
                Axios.post('/api/login', user_cred)
                    .then(function (response) {
                        if (response.success) {
                            this.$router.push('/');
                        } else {
                            this.showError = true;
                            this.errorMsg = "Incorrect username or password."
                        }
                    })
                    .catch(err => {
                        this.showError = true;
                        this.errorMsg = "Something wrong with the system. Please try again later. ";
                        console.log(err)
                    });
            }
        }
    }
</script>

<style>
    body.login {
        height: 100%;
        display: -ms-flexbox;
        display: -webkit-box;
        display: flex;
        -ms-flex-align: center;
        -ms-flex-pack: center;
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
    }

    .form-signin {
        width: 100%;
        max-width: 330px;
        padding: 15px;
        margin: 0 auto;
    }

    .form-signin .checkbox {
        font-weight: 400;
    }

    .form-signin .form-control {
        position: relative;
        box-sizing: border-box;
        height: auto;
        padding: 10px;
        font-size: 16px;
    }

    .form-signin .form-control:focus {
        z-index: 2;
    }

    .form-signin input[type="email"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }

    .form-signin input[type="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
</style>
