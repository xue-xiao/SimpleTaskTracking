<template>
    <!-- Alert Reference:  https://www.w3schools.com/bootstrap4/bootstrap_alerts.asp-->

    <div class="alert alert-danger mx-0 px-3 row">
        <div class="text-left col-11 px-0">
            {{ msg }}
        </div>
        <button @click="$emit('close')"  class="close col-1">
            &times;
        </button>
    </div>
</template>

<script>
    export default {
        name: "ErrorAlert",
        props: {
            // props is the set of parameters passed in from caller.
            msg: String
        }
    }
</script>

<style scoped>
    button.close {
        color: inherit;
    }
</style>
