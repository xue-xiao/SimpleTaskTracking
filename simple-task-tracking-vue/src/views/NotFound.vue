<template>
    <div class="h-100">
        <Header/>
        <div class="row h-100">
            <div class="m-auto">
                <h1>404</h1>
                <div class="error-details">
                    Sorry, requested page not found!
                </div>
                <div class="error-actions my-5">
                    <router-link to="/" class="btn btn-primary btn-lg">
                        <font-awesome-icon icon="home" />
                        Take Me Home
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from "../components/utils/Header";
    export default {
        name: "NotFound",
        components: {Header}
    }
</script>

