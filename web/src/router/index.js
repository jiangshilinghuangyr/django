import { createRouter, createWebHistory } from 'vue-router'
import NotFound from '@/views/NotFound.vue'
import FrontPage from '@/views/FrontPage.vue'
import OperationPage from '@/views/OperationPage.vue'
import FirstLevelReport from '@/views/FirstLevelReport.vue'
import SecondLevelReport from '@/views/SecondLevelReport.vue'
import ContactUs from '@/views/ContactUs.vue'
import UserInfo from '@/views/UserInfo.vue'
import UserManage from '@/views/UserManage.vue'
import VerminSet from '@/views/VerminSet.vue'
import DynamicSpace  from '@/views/DynamicSpace.vue'
import AiAnswer from '@/views/AiAnswer.vue'
import store from '@/store/index'
import MySqace from '@/views/MySqace.vue'


const routes = [
  {
    path:"/404/",
    name:"notfound",
    component:NotFound,
    meta:{
      resquestAuth:false,
    }
  },
  {
    path:"/verminset/",
    name:"verminset",
    component:VerminSet,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/myspace/",
    name:"myspace",
    component:MySqace,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/dynamicspace/",
    name:"dynamicspace",
    component:DynamicSpace,
    meta:{
      resquestAuth:true,
    }
  },
  {
    path:"/",
    redirect:"/frontpage/",
    component:FrontPage,
    meta:{
      resquestAuth:false,
    },
  },
  {
    path:"/aianswer/",
    name:"aianswer",
    component:AiAnswer,
    meta:{
      resquestAuth:true,
    }
  },
 
  {
    path:"/frontpage/",
    name:"frontpage",
    component:FrontPage,
    meta:{
      resquestAuth:false,
    },
  },
  {
    path:"/firstlevel/",
    name:"firstlevel",
    component:FirstLevelReport,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/secondlevel/",
    name:"secondlevel",
    component:SecondLevelReport,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/operationpage/",
    name:"operationpage",
    component:OperationPage,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/usermanage/",
    name:"usermanage",
    component:UserManage,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/userinfo/",
    name:"userinfo",
    component:UserInfo,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/contactus/",
    name:"contactus",
    component:ContactUs,
    meta:{
      resquestAuth:true,
    },
  },
  {
    path:"/:catchAll(.*)",
    redirect:"/404/"
  },
  


]

const router = createRouter({
  history: createWebHistory(),
  routes
})



router.beforeEach((to, from, next) => {
  if (to.meta.resquestAuth && !store.state.user.is_login) {
    next({name: "frontpage"});
  } else {
    next();
  }
})
export default router
