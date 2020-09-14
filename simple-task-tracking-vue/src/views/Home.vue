<template>
  <div class="home">
    <Header/>
    <img alt="logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Header from "@/components/utils/Header.vue";

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Header
  }
}
</script>
