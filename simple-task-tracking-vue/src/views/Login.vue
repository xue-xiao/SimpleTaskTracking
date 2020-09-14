<!-- Note:

Login page used bootstrap signin example page:
https://getbootstrap.com/docs/4.0/examples/sign-in/

-->

<template>
    <div class="text-center">
        <form class="form-signin" @submit.prevent="submitCredentials">
            <img class="mb-4" src="../assets/logo.png" alt="">
            <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
            <ErrorAlert v-if="showError" v-bind:msg="errorMsg" v-on:close="showError=false"/>

            <!-- form -->
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="email" v-model="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
            <label for="inputPassword" class="sr-only">Password</label>
            <input type="password" v-model="password" id="inputPassword" class="form-control" placeholder="Password" required>
            <div class="checkbox mb-3">
                <label>
                    <input type="checkbox" value="remember-me" v-model="remember"> Remember me
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
    import {API} from "../config";
    import {UserMixin} from "../mixins/user-mixin"

    export default {
        name: "Login",
        components: {ErrorAlert},
        mixins: [UserMixin],
        data: () => ({
            showError: false,
            errorMsg: "",
            email: "",
            password: "",
            remember: true
        }),
        methods: {
            submitCredentials() {
                const user_cred = {
                    email: this.email,
                    password: this.password,
                    remember: this.remember
                }
                this.password = "";
                Axios.post(API.LOGIN, user_cred, {withCredentials: true})
                    .then(response => {
                        // Axios automatically deserialized the response json to an object
                        if (response.data.success) {
                            this.updateUserSession(response.data.payload)
                            this.$router.push('/');
                        } else {
                            this.showError = true;
                            this.errorMsg = response.data.message;
                        }
                    })
                    .catch(err => {
                        this.showError = true;
                        this.errorMsg = "Something wrong with the server. Please try again later. ";
                        console.log(err)
                    });
            }
        }
    }

</script>

<style scoped>

    div.text-center {
        height: 100%;
        display: flex;
        justify-content: center;
    }

    .form-signin {
        width: 100%;
        max-width: 330px;
        padding: 15px;
        margin: auto;
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
