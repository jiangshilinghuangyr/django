<template>
<div style="margin-top: 20px;" class=" container">
    <div class="row">
       <div class="col-3">
        <div class="card">
            <div class="card-body">
                <img style="margin-left: 12px; width: 90%;height: 250px;" :src="store.state.user.photo" alt="">
           <div>
           </div>
           <div style="margin-left: 10px; margin-top: 2px; font-weight: 900; font-size: 20px; display: inline-block;">
            昵称:{{ store.state.user.username }}
           </div>
           <div style="margin-left: 40px; margin-top: 2px; font-weight: 900; font-size: 20px; display: inline-block;">
            发帖数:{{ store.state.user.posts_total }}
           </div>

           <div>
           </div>

           <div >

                <label style="margin-left: 10px; margin-top: 20px;font-weight: 900; font-size: 15px;" for="exampleFormControlTextarea1" class="form-label">今天也要记得分享</label>
                
                <div style=" margin-left: 10px;margin-top: 20px; height: 20px; width: 120px; display: inline-block;">
                    <select required v-model="post_type" class="form-select form-select-sm" aria-label="Default select example">
                    <option value="求助帖">求助贴</option>
                    <option value="经验贴">经验贴</option>
                    </select>
                </div>
              
                <textarea  required v-model="post_content" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            </div>

            <div style="margin-top: 5px;">
                <button  @click="postAPost" type="button" class="btn btn-primary">提交</button>
            </div>
         

         
            </div>
        </div>

        </div>



        <div class="col-8">
            <div class="card">
                <div class="card-bod">
                    <ul class="nav nav-tabs" id="myTab" role="tablist">
<li class="nav-item" role="presentation">
<button style="font-weight: 900; font-size: 20px;" class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">我的发帖</button>
</li>
<li class="nav-item" role="presentation">
<button style="font-weight: 900; font-size: 20px;" class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">提问记录</button>
</li>
<!-- <li class="nav-item" role="presentation">
<button style="font-weight: 900; font-size: 20px;" class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Contact</button>
</li> -->

</ul>
<div class="tab-content" id="myTabContent">


<div style="margin-top: 20px;" class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
    
    
    <div style="margin:10px 10px;" class="card" v-for="post  in store.state.user.posts " :key="post.id">
        <div class="crad-body">
            <div style="font-weight: 900; font-size: 20px; padding: 0px; margin: 0px 0px 0px 5px; display: inline-block;  color: black;text-align: center;line-height: 50px;">
                {{ post.post_type }} 
            </div>
            
            
            <div style="font-weight: 900; margin-left: 20px; display: inline-block;">
            {{ post.post_date }}
            </div>

            <div style="font-weight: 900; margin-left: 20px; display: inline-block;">
            {{ post.post_time }}
            </div>
            
            <div style="font-weight: 900; margin-left: 10px; display: inline-block;">
            点赞数&#x1F44D;{{ post.like }}
            </div>
                
            
        <hr>
        <img  :src="store.state.user.photo" alt="" style="margin-left: 5px; height: 50px;border-radius: 50% ;margin-top: 10px;">
    
        <div style="margin-left: 15px; display: inline-block;">
            {{ store.state.user.username }}
           </div>
            
            
            <div>

            </div>

            <div style="font-weight: 700; margin: 10px 10px ; display: inline-block;">
                {{ post.content }}
            </div> 





        </div>
    </div>

    
    </div>














<div style="margin-top: 20px;" class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
    
    
    
    <div style="margin:10px 10px;" class="card" v-for="saved_QA  in store.state.user.saved_QAs" :key="saved_QA.id">
        <div class="crad-body">
            <div style="font-weight: 900; font-size: 15px; padding: 0px; margin: 0px 0px 0px 5px; display: inline-block;  color: black;text-align: center;line-height: 50px;">
                Ques:{{ saved_QA.ques }} 
            </div>
        </div>

        <div class="crad-body">
            <div style="font-weight: 900; font-size: 15px; padding: 0px; margin: 0px 0px 0px 5px; display: inline-block;  color: black;text-align: center;line-height: 50px;">
                Answer:{{ saved_QA.ai_answer}} 
            </div>
        </div>
    </div>


</div>













<!-- 
<div style="margin-top: 20px;" class="tab-pane fade" id="contact-tab-pane" role="tabpanel" aria-labelledby="contact-tab" tabindex="0">
    
    
    3</div> -->

</div>
                </div>
            </div>

        

   </div>
  
</div>
</div>


  


    

</template>

<script>
// import ContentBase from '@/components/ContentBase.vue'
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import $ from 'jquery'

        export default{
            components:{
                // ContentBase,
            },
            setup(){
                
                const store = useStore();
                const router=useRouter();

            const posts = ref([]);
            posts.value = store.state.user.posts;

  
            const total_posts = ref(0);
            total_posts.value = store.state.user.posts_total;

            const post_type = ref("");
            const post_content = ref("");
   

            const postAPost = ()=>{
               $.ajax({
                   url:"http://localhost:3000/user/postapost/",
                   type: "post",
                   data:{
                    user_id:store.state.user.id,
                    post_type:post_type.value,
                    post_content:post_content.value
                   },
                   success(resp){
                   if (resp.message === "success") {
                    $.ajax({
                            url:"http://localhost:3000/user/myspace/",
                            type: "get",
                            data:{
                            userid:store.state.user.id
                            },
                            success(resp){
                            if (resp.message === "success") {
                            store.commit("updateUserPostsTotal",resp.total_posts);
                            store.commit("updateUserPosts",resp.posts);
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

                        setTimeout(()=>{ router.push({name:"myspace"})}, 500)

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


          }
           


                return{
                    store,
                    posts,
                    total_posts,
                    postAPost,
                    post_type,
                    post_content,
                    router
                }
            }
            
        }
</script>

<style scoped >

hr{
    margin: 1px;
}
</style>

