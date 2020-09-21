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
        <b-navbar toggleable="sm" type="light" variant="light">
            <router-link class="navbar-brand" to="/">
                <img alt="logo" src="../../assets/logo.png" height="30" class="d-inline-block align-top">
                {{ brandName }}
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
    import {UserMixin} from "../../mixins/user-mixin";
    import {CONSTANTS} from "../../config";

    export default {
        name: "Header",
        mixins: [UserMixin],
        data: () => ({
            brandName: CONSTANTS.BRAND_NAME
        }),
        created: function () {
            // Cannot use Arrow function when we need to access `this` which is bound to current component instance.
            this.checkLoggedIn();
        }
    }
</script>

<style scoped>

</style>
