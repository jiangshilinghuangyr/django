<template>
  <div  :class="pageBackground">
    <NavBar></NavBar>
     <!-- <NavBarTest></NavBarTest> -->
    <router-view/>
  </div>

</template>



<script>




import { computed } from 'vue';
import { useRoute } from 'vue-router';

import NavBar from '@/components/NavBar.vue'
// import NavBarTest from './components/NavBarTest.vue';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"

export default{
  components:{
  NavBar,
  // NavBarTest

  },
  setup() {
    const route = useRoute();

    const pageBackground = computed(() => {
      switch (route.name) {
        case 'notfound':
          return 'notfound-background';
        case 'frontpage':
          return 'frontpage-background';
        case 'operationpage':
          return 'operationpage-background';
        case 'firstlevel':
          return 'firstlevel-background';
        case 'secondlevel':
          return 'secondlevel-background';
        case 'userinfo':
          return 'userinfo-background';
        case 'contactus':
          return 'contactus-background';
        case 'usermanage':
          return 'usermanage-background';
        default:
          return 'default-background';
      }
    });

    return { pageBackground };
  },
}
</script>


<style>
.frontpage-background {
  background-image: url("@/assets/img/laonong.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}

.operationpage-background {
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}

.firstlevel-background {
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}

.secondlevel-background {
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}

.userinfo-background {
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}

.contactus-background {
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}
.usermanage-background {
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}
.notfound-background {
  background-color: white;
  min-height: 100vh;
}
.default-background{
  background-image: url("@/assets/img/daotian.jpg") !important;
  background-size: cover;
  min-height: 100vh;
}


</style>
