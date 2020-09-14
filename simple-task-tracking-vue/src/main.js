import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'

// Add AwesomeIcons
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {library} from '@fortawesome/fontawesome-svg-core'
// We need to import any font we need and add to library
import {faHome,} from '@fortawesome/free-solid-svg-icons'

Vue.component('font-awesome-icon', FontAwesomeIcon)
library.add(faHome)

Vue.config.productionTip = false

// global variables
// Reference: https://vuejs.org/v2/cookbook/adding-instance-properties.html

// - self-defined session variable
Vue.prototype.$session = {
    loggedIn: null
}

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
