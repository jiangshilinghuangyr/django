<template>
   
    <div class="row">
        <div class="col-3">
            <div class="qwe" @click="tocontactus">
                联系我们
            </div>
           <div class="qwe" @click="touserinfo">
                个人信息
           </div>
           <div class="qwe" @click="tooperationpage">
                返回
           </div>
           

        </div>
        <div class="col-6">
            <ContentBase>
                <div class="card peizhi">
                    <div class="card-body">
                        团队成员:
                        <br>
                        羊宇同,邵凯唯,王亦非,艾力扎提,江诗浪
                    </div>
                    
                </div>
                <div class="card peizhi ">
                    <div class="card-body">
                        联系我们：
                        <br>
                        qq:3337180648
                    </div>
                </div>
                <div class="card peizhi">
                    <div class="card-body">
                        感谢支持:
                        <br>
                        学校就算了吧
                        
                    </div>
                </div>
            </ContentBase>
        </div>
    </div>


</template>

<script>
import ContentBase from '@/components/ContentBase.vue'

import { useRouter } from 'vue-router';


export default {
components:{
ContentBase,
},
setup(){

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
    return {
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

.yangshi{
    color: black !important;  
    text-decoration: none !important;     /* 去除下划线 */
}
</style>