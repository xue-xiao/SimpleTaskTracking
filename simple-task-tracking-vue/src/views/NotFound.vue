<template>
    <div class="container">
        <div class="error-template">
            <h1>Oops!</h1>
            <h2>404 Not Found</h2>
            <div class="error-details">
                Sorry, an error has occurred, Requested page not found!
            </div>
            <div class="error-actions">
                <router-link to="/" class="btn btn-primary btn-lg">
                    <span class="glyphicon glyphicon-home"></span>
                    Take Me Home
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "NotFound"
    }
</script>

<style scoped>
    div.container {
        height: 100%;
        display: flex;
        justify-content: center;
    }

    .error-template {
        padding: 40px 15px;
        text-align: center;
        margin: auto;
    }

    .error-actions {
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .error-actions .btn {
        margin-right: 10px;
    }
</style>
