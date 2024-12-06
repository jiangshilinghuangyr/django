<template>

    <div class="row">
        <div class="col-9">
            <ContentBase>
                <img src="@/assets/img/hezhao.png" style="width: 96%; height: 85%;margin-left: 2%;" alt="图片">
                <!-- <video controls style="width: 1200px; height: 600px;" src="@/assets/video/video1.mp4"></video> -->
            </ContentBase>
        </div>
        <div class="col-2">
            <ContentBase>
           
                <div class="row">
                    <button type="button" class="btn btn-primary">查看健康评估</button>
                </div>
                <div class="row">
                    <button type="button" class="btn btn-primary">查看建议措施</button>
                </div>
                <div class="row">
                    <button type="button" class="btn btn-primary" @click="toFirstReport">退回一级报告</button>
                </div>
             
                <div class="row">
                    <button type="button" class="btn btn-danger delete">删除报告</button>
                </div>
            </ContentBase>
        </div>

      
    </div>

        

    </template>
    
    <script>
 import ContentBase from '@/components/ContentBase.vue'
 import { useRouter } from 'vue-router';
 import { useStore } from 'vuex';

    export default{
        components:{
   ContentBase
        },
        setup(){
            const router = useRouter();
            const store = useStore();
            const toFirstReport = ()=>{
                router.push({name:"firstlevel"});
                store.dispatch("updateIsFront",false);
           }


           
           return{
                    router,
                    toFirstReport,
                }
        }
    }
    </script>
    
    <style scoped>
.btn{
    margin-top:20px ;
}


.videomethod{
    font-size: 30px;

font-weight: bold;
}

.info{
    color: black;
    margin-bottom: 50px;
}

.record{
    margin-top: 195px;
}

.col-9{
    margin-left: 45px;
}
.col-2{
    margin-right: 45px;
}

.delete{
    margin-top: 395px;
}
    
    </style>