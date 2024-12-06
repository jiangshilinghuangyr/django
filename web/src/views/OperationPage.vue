<template>
    




    <div class="row">
  
        <div class="col-9" >
            <ContentBase>
                <img :src="image_url" style="width: 1180px; height: 620px; margin-left: 15px;" alt="图片">
                <!-- <video controls style="width: 96%; height: 85%;margin-left: 2%;" src="@/assets/video/video1.mp4"></video> -->
            </ContentBase>
        </div>
        <div class="col-2">
            <ContentBase>
                <div class="videomethod">
                    人工拍照
                </div>
                <div class="row">
                    <button type="button" class="btn btn-primary">拍照并生成报告</button>
                </div>
                <!-- <div class="row">
                    <button type="button" class="btn btn-primary">结束录制</button>
                </div> -->
                <!-- <div class="info">
                            请用WASD控制方向
                </div> -->
                <div class="videomethod" style="margin-top: 50px;">
                    自动拍照
                </div>
                <!-- <div class="row">
                    <select class="form-select" aria-label="Default select example" placeholder="请选择任务">
                        <option value="vermin">虫害情况任务</option>
                        <option value="crop">作物情况任务</option>
                        <option value="damage">草害情况任务</option>
                        <option value="solid">土壤情况任务</option>
                    </select>
                </div> -->
                <div class="row">
                    <button type="button" class="btn btn-primary">拍照并生成报告</button>
                </div>




                <span class="videomethod" style="margin-top: 50px; display: inline-block;">
               
                        本地上传
                    
                 
                    <button class="btn btn-primary" style="margin-left: 6px;" type="button" disabled v-if="store.state.user.is_pull">
                        <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                        <span >请等待</span>
                        </button>
                </span>
        
                
            
                  
                <div class="row" style="margin-top: 20px;">
           
                  
            
                    <input type="file" class="form-control" ref="fileInput" >
                    
                    <button class="btn btn-outline-secondary" type="button" @click="yolov10" >上传图片</button>
               
                    
                 
                </div>
                
                <div class="row " style="margin-top: 100px;">
                    <button type="button" class="btn btn-success record" @click="toFirstReport">查看报告</button>
                </div>
            
                <!-- <div class="row " style="margin-top: 10px;">
                    <button type="button" class="btn btn-success record" @click="logout">退出登录</button>
                </div> -->
            </ContentBase>
        </div>

      
    </div>

        

    </template>
    
    <script>
 import ContentBase from '@/components/ContentBase.vue'
import $ from 'jquery'
import { ref } from 'vue';
 import { useRouter } from 'vue-router';
 import { useStore } from 'vuex';


    export default{
        components:{
   ContentBase
        },
        setup(){
            const router = useRouter();
            const store = useStore();
            const fileInput = ref(null);
            const  image_url =    ref(require("@/assets/img/hezhao.png"));

         
 
            // require(("@/assets/img/"+"image.webp"));
            
     

            


            const toFirstReport = ()=>{
               
                // store.dispatch("updateIsFront",false);
                $.ajax({
                    url:"http://localhost:3000/user/getrecord/",
                    type: "get",
                    data: {
                        id:store.state.user.id,
                    },
                    success(resp){
                    if (resp.message === "success") {

                        store.dispatch("updateTotalRecord",{
                            reports:resp.records,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            totalReports:resp.total_reports
                        })
          
                        console.log(store.state.record.reports);
                        console.log(store.state.record.current_page);
                        console.log(store.state.record.total_reports);
                        console.log(store.state.record.total_pages);

                    } 
                    else
                    {
                        console.log("未成功");
                    }
                },
                error(){

                    console.log("未成功");
                }
                })
        


                
                setTimeout(()=>{ router.push({name:"firstlevel"})}, 500)

               
           }

           const toUserManage = ()=>{
                router.push({name:"usermanage"});
                store.dispatch("updateIsFront",false);
           }

           
           const yolov10 = ()=>{


            store.state.user.is_pull = true;
            const file = fileInput.value.files[0];
            const formData = new FormData(); // 创建FormData对象
            formData.append('file', file); // 将文件添加到formData中
            formData.append('id', store.state.user.id); // 将文件添加到formData中
                $.ajax({
                    url:"http://localhost:3000/yolov10/api/",
                    type: "post",
                    data: formData,
                    withCredentials:true,
                    processData: false,  // 不要自动处理数据
                    contentType: false,  // 不要设置 Content-Type
                success(resp){
                    image_url.value="http://localhost:3000/media/"+resp.path;
                    if (resp.message === "成功识别") {
                        console.log(resp.path);
                        console.log(resp.type);
                        console.log("成功识别");
                        store.state.user.is_pull = false;
                    } 
                    else
                    {
                        console.log("未成功识别");
                    }
                },
                error(){

                    console.log("未成功识别");
                }
                })
           }
        
           const logout=()=>{
            store.dispatch("logout",{
                    id:store.state.user.id,
                    success(resp){
                        console.log(store.state.user.is_login);
                        console.log(resp+"退出成功");
                    },
                    error(resp){
                        console.log(store.state.user.is_login);
                        console.log(resp+"退出失败");
                    }
                },
                router.push({name:"frontpage"})
               
            )
        }
           
           return{
                    router,
                    store,
                    toFirstReport,
                    toUserManage,
                    logout,
                    yolov10,
                    fileInput,
                    image_url
                }
        }
    }
    </script>
    
    <style scoped>

.btn{
    margin-top:20px ;
}

.videomethod{
    font-size: 25px;
font-weight: bold;
}

.info{
    color: black;
    margin-bottom: 10px;
}

.col-9{
    margin-left: 45px;
}

.col-2{
    margin-right: 45px;
}

.manager{
    margin-bottom: 30px;
}

    </style>