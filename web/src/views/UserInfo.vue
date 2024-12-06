<template>
   
            <div class="row">
               


<div class="col-3">

</div>

                <div class="col-6">
                    <ContentBase>
                        <div class="card peizhi">
                            <div class="card-body">
                                基础信息
                                <div class="form-floating">
                                
                                <input v-model="username" type="text" class="form-control" id="floatingInput">
                                <label for="floatingInput">用户名:{{ store.state.user.username }}</label>
                                </div>
                                <div class="form-floating">
                                <input v-model="password" type="password" class="form-control" id="floatingPassword">
                                <label for="floatingPassword">密码:*******</label>
                                </div>
                                <div class="form-floating">
                                <input v-model="sex" type="text" class="form-control" id="floatingPassword">
                                <label for="floatingPassword">性别:{{ store.state.user.sex }}</label>
                                </div>
                                <div class="form-floating">
                                <input v-model="bir" type="date" class="form-control" id="floatingPassword">
                                <label for="floatingPassword">生日:{{ store.state.user.bir }}</label>
                                </div>
                            </div>
                            
                        </div>
                        <div class="card peizhi ">
                            <div class="card-body">
                                联系信息
                                <div class="form-floating">
                                <input v-model="email" type="email" class="form-control" id="floatingInput">
                                <label for="floatingInput">邮箱:{{ store.state.user.email }}</label>
                                </div>
                                <div class="form-floating">
                                <input v-model="phone" type="text" class="form-control" id="floatingPassword">
                                <label for="floatingPassword">电话号码:{{ store.state.user.phone }}</label>
                                </div>
                            </div>
                        </div>
                        <!-- <div class="card peizhi">
                            <div class="card-body">
                                无人机配置
                                <div class="form-floating">
                                <input v-model="manufacturer" type="text" class="form-control" id="floatingInput">
                                <label for="floatingInput">厂商:大疆</label>
                                </div>
                                <div class="form-floating">
                                <input v-model="pro_date" type="date" class="form-control" id="floatingPassword">
                                <label for="floatingPassword">生产日期:2024/11/15</label>
                                </div>
                            </div>
                        </div> -->
                        <button type="submit" class="btn btn-warning" @click="setInfo">确认修改</button>
                        <button style="margin-left: 620px;" type="submit" class="btn btn-warning" @click="tooperationpage">返回</button>
                    </ContentBase>
                </div>




                

<div class="col-3">
    
</div>

            </div>


            



</template>

<script>
import ContentBase from '@/components/ContentBase.vue'
import { useStore } from 'vuex';
import { ref } from 'vue'
import { useRouter } from 'vue-router';

export default {
    components:{
        ContentBase,
},
    setup(){

        const store = useStore();
        let username = ref('');
        let password = ref('');
        let sex = ref('');
        let bir = ref('');
        let email = ref('');
        let phone = ref('');
        let manufacturer = ref('');
        let pro_date = ref('');


        const router=useRouter()

        const tocontactus = ()=>{
            router.push({name:"contactus"})
        }
        const touserinfo = ()=>{
            router.push({name:"userinfo"})
        }
        const tooperationpage = ()=>{
            router.push({name:"operationpage"})
        }


        const setInfo=()=>{
            store.dispatch("setInfo",{
                    id:store.state.user.id,
                    username:username.value,
                    password:password.value,
                    sex:sex.value,
                    bir:bir.value,
                    email:email.value,
                    phone:phone.value,
                    manufacturer:manufacturer.value,
                    pro_date:pro_date.value,
                    success(resp){
                        console.log(resp+"修改成功");
                    },
                    error(resp){
                        console.log(resp+"修改失败");
                    }
                },
               
            )
        }

       return{
        store,
        username,
        password,
        sex,
        bir,
        email,
        phone,
        manufacturer,
        pro_date,
        setInfo,
        tocontactus,
    tooperationpage,
    touserinfo
       }
    }

}
</script>

<style scoped>
.peizhi{
    margin-bottom: 40px ;
}

.qwe{
    color: black;
    margin-left: 45px;
    margin-top: 100px;
    margin-bottom: 100px;
    cursor: pointer;
    font-weight: 900;
    font-size: x-large;
}


</style>