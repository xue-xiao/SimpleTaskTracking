<!--
Standard Bootstrap classes work in most cases.
But those needs javascript cannot work.
They include:
    collapse
    dropdown


You have to use the component wrappers provided by bootstrap-vue

-->

<template>
    <div>
        <b-navbar toggleable="lg" type="light" variant="light">
            <router-link class="navbar-brand" to="/">
                <img alt="logo" src="../../assets/logo.png" height="30" class="d-inline-block align-top">
                <Brand/>
            </router-link>
            <!-- Collapsable menu -->
            <b-navbar-toggle target="nav-collapse"/>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item to="/announce">Announce</b-nav-item>
                    <b-nav-item to="/about">About</b-nav-item>
                </b-navbar-nav>

                <!-- Right aligned -->
                <b-navbar-nav class="ml-auto">
                    <!-- if logginIn -->
                    <b-nav-item-dropdown right v-if="$session.loggedIn">
                        <template v-slot:button-content>
                            {{ $session.displayName }}
                        </template>
                        <b-dropdown-item href="#">Profile</b-dropdown-item>
                        <b-dropdown-item-button @click="signOut">Sign Out</b-dropdown-item-button>
                    </b-nav-item-dropdown>
                    <!-- else -->
                    <b-nav-item to="/login" v-else>Sign In</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>

</template>

<script>
    import Brand from "../../components/const/Brand";
    import {UserMixin} from "../../mixins/user-mixin";
    import Axios from "axios";
    import {API} from "../../config";

    export default {
        name: "Header",
        components: {Brand},
        mixins: [UserMixin],
        methods: {
            signOut: function () {
                if (this.$session.loggedIn) {
                    Axios.get(API.LOGOUT, {withCredentials: true});
                }
                this.resetUserSession();
                this.$forceUpdate();
                // TODO: clear cookies
            }
        },
        created: function () {
            // Cannot use Arrow function when we need to access `this` which is bound to current component instance.
            if (this.$session.loggedIn == null) {
                // Only make a call when loggedIn status is unknown.

                Axios.get(API.USER_INFO, {withCredentials: true})
                    .then(response => {
                        if (response.data.success) {
                            this.updateUserSession(response.data.payload);
                            this.$forceUpdate();
                        } else {
                            this.$session.loggedIn = false;
                        }
                    })
                    .catch(err => {
                        console.log(err);
                        this.$session.loggedIn = false;
                    });
            }
        }
    }
</script>

<style scoped>

</style>
