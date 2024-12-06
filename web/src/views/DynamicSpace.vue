<template>

    <div class="row">
     

        <div class="col-9" style="margin-left: 13%"  >
            <ContentBase>

            <div class="row">
             



                <div class="card" v-for="(post,index)  in posts " :key="post.id" style="margin-bottom: 20px;">
                    <div class="card-body" style="padding: 1px;">

                        <div style="font-weight: 900; font-size: 20px; padding: 0px; margin: 0px; display: inline-block;  color: black;text-align: center;line-height: 50px;">
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
                             <div style="display: inline-block; margin-left: 20px;">
                                <button  @click="like(post.id)" type="button" class="btn btn-primary">点个赞吧&#x1F44D;</button>
                            </div> 
                            
                        <hr>
                        <img :src="store.state.user.photo" alt="" style="height: 50px;border-radius: 50% ;margin-top: 10px;">
                           <div style="font-weight: 900; margin-left: 20px; display: inline-block;">
                            {{usernames[index] }}
                           </div>
                          
                           
                            <div>

                            </div>

                            <div style="font-weight: 700; margin: 10px 10px ; display: inline-block;">
                                {{ post.content }}
                            </div> 
                    </div>
                </div>
            </div>
            </ContentBase>
        </div>


        <div class="col-1">
  
  <nav aria-label="..."     style="position: fixed;">
  <ul class="pagination" style="float: left;">
      <li class="page-item" >
          <span style="cursor: pointer; font-weight: 900; font-size: 30px; color: black;"  class="page-link"   @click="ToOpera">返回</span>
      </li>
   

  </ul>
  </nav>

</div>
       

      
    </div>

        

    </template>
    
    <script>

 import { useRouter } from 'vue-router';
 import { useStore } from 'vuex';
 import ContentBase from '@/components/ContentBase.vue';
import { ref } from 'vue';
import $ from 'jquery'



    export default{
        components:{
   ContentBase
        },
        setup(){
           
            const router = useRouter();
            const store = useStore();

            const posts = ref([]);
            posts.value=store.state.post.posts;

            const usernames = ref([]);
            usernames.value=store.state.post.usernames;

            const total_posts = ref(0);
            total_posts.value = store.state.post.total_posts;

            const total_pages = ref(0);
            total_pages.value = store.state.post.total_pages;

            const current_page = ref(0);
            current_page.value = store.state.post.current_page;
        

            // posts.value=store.state.post.posts;
            // usernames.value=store.state.post.usernames;
            // total_posts.value = store.state.post.total_posts;
            // total_pages.value = store.state.post.total_pages;
            // current_page.value = store.state.post.current_page;
        
        

        const ToOpera=()=>{
            router.push({name:"operationpage"})
        }


        const like=(id)=>{
           $.ajax({
            url: "http://localhost:3000/user/postliked/",
            type: "post",
            data:{
                post_id:id
            },
            success(resp){
                if(resp.message === "成功点赞"){
                    $.ajax({
                   url:"http://localhost:3000/user/dynamicspace/",
                   type: "get",
                   success(resp){
                   if (resp.message === "success") {
                    store.dispatch("updateTotalPosts",{
                            posts:resp.posts,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            total_posts:resp.total_posts,
                            usernames:resp.usernames,
                        })
                        posts.value=store.state.post.posts;
            usernames.value=store.state.post.usernames;
            total_posts.value = store.state.post.total_posts;
            total_pages.value = store.state.post.total_pages;
            current_page.value = store.state.post.current_page;

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
            },
            error(){
                console.log("未成功");
            },
           })
        }


       
       

            return{
                    router,
                    store,
                    total_pages,
                    total_posts,
                    posts,
                    current_page,
                    ToOpera,
                    usernames,
                    like
              
                }
        
        }
    }
    </script>
    
    <style scoped>
.btn1{
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
.col-2{
    margin-left: 45px;
}
.title{
    font-size: 17px;
    font-weight: 900;
}

hr{
    margin: 0px;
}

    </style>