<template>
    <div class="home">
        <Header/>
        <Main v-if="$session.loggedIn"/>
        <Welcome v-else/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import Welcome from '../components/Welcome.vue'
    import Header from "../components/layout/Header.vue";
    import {UserMixin} from "../mixins/user-mixin";

    export default {
        name: 'Home',
        mixins: [UserMixin],
        components: {
            Welcome,
            Header
        },
        created() {
            this.checkLoggedIn();
        }
    }
</script>
