import { createStore } from 'vuex'
import ModuleUser from "@/store/user"
import ModuleRecord from '@/store/record'
import ModuleVermin from '@/store/verminset'
import ModulePost from '@/store/post'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user: ModuleUser,
    record:ModuleRecord,
    vermin:ModuleVermin,
    post:ModulePost,
  }
})
