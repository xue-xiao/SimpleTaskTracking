<template>
    <div class="hello">
        <img alt="logo" src="../assets/logo.png"/>
        <ShadowBox>
            <div class="col-lg-5 text-center text-lg-left my-3">
                <h3 class="mb-3">
                    Welcome to <br/>
                    Simple Task Tracking</h3>
                <p class="mr-lg-6">
                    Create tasks and assign them to team members.
                    Track tasks efficiently.
                    Comment on tasks to share ideas and feedback.
                </p>
            </div>
            <div class="col-lg-7 d-flex flex-wrap flex-md-nowrap justify-content-center justify-content-lg-end">
                <div class="col-12 col-sm-6 col-md-5 d-flex flex-column justify-content-between align-items-center text-center p-3">
                    <router-link to="/login" class="text-decoration-none">
                        <font-awesome-icon icon="sign-in-alt" class="mb-2 text-primary" size="3x"></font-awesome-icon>
                        <h3 class="text-primary">Sign In</h3>
                        <p class="text-secondary mt-3">Login with your email and password.</p>
                    </router-link>
                </div>
                <div class="col-12 col-sm-6 col-md-5 d-flex flex-column justify-content-between align-items-center text-center p-3">
                    <router-link to="/signup" class="text-decoration-none">
                        <font-awesome-icon icon="user-plus" class="mb-2 text-success" size="3x"></font-awesome-icon>
                        <h3 class="text-success">Sign Up</h3>
                        <p class="text-secondary mt-3">Create a new account. </p>
                    </router-link>
                </div>
            </div>
        </ShadowBox>
    </div>
</template>

<script>
    import ShadowBox from './layout/ShadowBox.vue'

    export default {
        name: 'Welcome',
        components: {
            ShadowBox,
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .text-decoration-none:hover {
        text-shadow: 0 0 1px;
    }
</style>
