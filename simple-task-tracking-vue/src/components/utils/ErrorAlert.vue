<template>
    <!-- Alert Reference:  https://www.w3schools.com/bootstrap4/bootstrap_alerts.asp-->

    <div class="alert alert-danger">
        <button @click="$emit('close')" type="button" class="close" data-dismiss="alert">&times;</button>
        <div class="text-left">
            {{ msg }}
        </div>
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

        /*Center the X button vertically!*/
        position: absolute;
        right: 0;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        padding-right: inherit;
    }
    div.text-left {
        padding-right: inherit;
    }
</style>
