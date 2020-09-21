<template>
    <div class="container px-lg-4">
        <div class="d-lg-flex my-5 mx-auto p-4 p-md-7 rounded box-shadow-large">
            <slot/>
        </div>
    </div>
</template>

<style scoped>
    .box-shadow-large {
        box-shadow: 0 8px 24px rgba(149, 157, 165, .2) !important;
    }
</style>
