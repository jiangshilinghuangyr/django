<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#" style="margin-left: 120px;margin-right: 30px;" >智能精准农业系统</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse " id="navbarNavDropdown">
      <ul class="navbar-nav">
       
          <li class="nav-item " style="text-align: center;">
          <router-link class="nav-link " aria-current="page"  :to="{name: 'operationpage'}">图片识别</router-link>
        </li>
        <li class="nav-item" @click="toVerminset" >
          <a class="nav-link"  style="cursor: pointer;" >害虫图鉴</a>
        </li>
        <li class="nav-item" @click="toDynamicSpace">
          <a class="nav-link"  style="cursor: pointer;">动态空间</a>
        </li>
        
      
        <!-- <li class="nav-item">
          <router-link class="nav-link"  :to="{name: 'requesthelp'}">请求帮助</router-link>
        </li>
      -->
        <li class="nav-item">
          <router-link class="nav-link"  :to="{name: 'aianswer'}">AI问答</router-link>
        </li>


  <li class="nav-item " style="margin-left: 700px;cursor: pointer;" >
          <a  v-if="!store.state.user.is_login" class="nav-link "  data-bs-toggle="modal" data-bs-target="#log">登录</a>
        </li>

        <li class="nav-item Float-end" style="cursor: pointer;" >
          <a   v-if="!store.state.user.is_login" class="nav-link"  data-bs-toggle="modal" data-bs-target="#reg">注册</a>
        </li>






        <li  v-if="store.state.user.is_login">
          <img  :src=store.state.user.photo alt="头像">
        </li>
        

          <li class="dropdown" v-if="store.state.user.is_login">
            <a  class="nav-link dropdown-toggle " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            </a>
            <ul class="dropdown-menu dropdown-menu-dark" >
              <li @click="toMySpace"><a class="dropdown-item" href="#">我的空间</a></li>
              <li><router-link class="dropdown-item" href="#" :to="{name: 'userinfo'}">个人中心</router-link></li>
              <li @click="logout" style="cursor: pointer;" ><a class="dropdown-item" >退出登录</a></li>
            </ul>
          </li>



        
        
      
      </ul>
    </div>
  </div>
</nav>




<div class="modal fade" id="log" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered  " style="width: 85%; max-width: 350px;">
    <div class="modal-content ">
      <div class="modal-header" style="display: flex;">
        <h1 class="modal-title fs-5" id="staticBackdropLabel" style="justify-items: center;">登录</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body ">
        <form action="">
          <label for="username" class="form-label">用户名</label>
        <input v-model="username" type="text" class="form-control" id="username" placeholder="请输入用户名" required>
        <label for="password" class="form-label">密码</label>
        <input v-model="password" type="password" class="form-control" id="password" placeholder="请输入密码" required>
     
        </form>
       
      </div>
      <div class="modal-footer">
        <button class="buttonlog btn btn-primary" style="width: 100%;" data-bs-dismiss="modal"  @click="login">提交</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="reg" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered  " style="width: 85%; max-width: 350px;">
    <div class="modal-content ">
      <div class="modal-header" style="display: flex;">
        <h1 class="modal-title fs-5" id="staticBackdropLabel" style="justify-items: center;">注册</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body ">
        <form action="">

          <label for="username" class="form-label">用户名</label>
        <input v-model="username" type="text" class="form-control" id="username" placeholder="请输入用户名" required>
        <label for="password" class="form-label">密码</label>
        <input v-model="password" type="password" class="form-control" id="password" placeholder="请输入密码" required>
        <label for="passwordConf" class="form-label">确认密码</label>
        <input v-model="passwordConf" type="password" class="form-control" id="passwordConf" placeholder="请输入确认密码" required>
        </form>
       
      </div>
      <div class="modal-footer">
        <button class="buttonlog btn btn-primary" style="width: 100%;" data-bs-dismiss="modal"  @click="reg">提交</button>
      </div>
    </div>
  </div>
</div> 
</template>

<script>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import $ from 'jquery'
export default{

  components:{

  },
  setup(){
    const store=useStore();
    const router=useRouter();
    const username=ref("");
    const password=ref("");
    const passwordConf=ref("");
    const message=ref("");
    const login=()=>{
            store.dispatch("login",{
                username:username.value,
                password:password.value,
                success(resp){
                    message.value="";
                    router.push({name:"operationpage"});
                    console.log(resp.message)
                },
                error(resp){
                    message.value=resp.message;
                }
            })
        };

    const reg=()=>{
        store.dispatch("reg",{
            username:username.value,
            password:password.value,
            passwordConf:passwordConf.value,
            success(resp){
                message.value="";
                router.push({name:"operationpage"});
                console.log(resp.message)
            },
            error(resp){
                message.value=resp.message;
            }
        })
    };
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
        };

        const toVerminset = ()=>{
               $.ajax({
                   url:"http://localhost:3000/user/verminset/",
                   type: "get",
                   success(resp){
                   if (resp.message === "success") {

                    store.dispatch("updateTotalVermins",{
                            vermins:resp.vermins,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            total_vermins:resp.total_vermins
                        })
         
                  
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

       

               
               setTimeout(()=>{ router.push({name:"verminset"});}, 1000)
               
            

           
          }





          const toDynamicSpace = ()=>{
    
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

               setTimeout(()=>{ router.push({name:"dynamicspace"})}, 1000)

          }


          const toMySpace = ()=>{
    
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
    });


    $.ajax({
        url:"http://localhost:3000/user/checkaianswer/",
        type: "get",
        data:{
          userid:store.state.user.id
        },
        success(resp){
        if (resp.message === "success") {
         store.commit("updateQuesSaved",resp.ai_answers);
        } 
        else
        {
            console.log("未成功");
        }
    },
    error(){

        console.log("未成功");
    }
    });





    setTimeout(()=>{ router.push({name:"myspace"})}, 1000);

}

        return {
          login,
          username,
          password,
          passwordConf,
          message,
          reg,
          store,
          router,
          logout,
          toVerminset,
          toDynamicSpace,
          toMySpace
        }
  },

}


</script >

<style scoped>

.dropdown-menu {
  left: 0;
  right: auto;
}


.buttonlog{
  padding: 10px,16px;
  background-color: #66afe9 !important;
}

#div-login-msg, #div-lost-msg, #div-register-msg {
    border: 1px solid #dadfe1;
    height: 30px;
    line-height: 28px;
    transition: all ease-in-out 500ms;
}


.glyphicon {
    position: relative;
    top: 1px;
    display: inline-block;
    font-family: 'Glyphicons Halflings';
    font-style: normal;
    font-weight: 400;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
#icon-login-msg, #icon-lost-msg, #icon-register-msg {
    width: 30px;
    float: left;
    line-height: 28px;
    text-align: center;
    background-color: #dadfe1;
    margin-right: 5px;
    transition: all ease-in-out 500ms;
}
.form-control {
    display: block;
    width: 100%;
    height: 34px;
    /* margin: 10px 0px 0px; */
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.42857143;
    color: #555;
    background-color: #fff;
    background-image: none;
    border: 1px solid #ccc;
    border-radius: 4px;
    -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
    -webkit-transition: border-color ease-in-out .15s, -webkit-box-shadow ease-in-out .15s;
    -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
    transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.navbar {

      border: none;
      box-shadow: none;
    }

    /* 调整导航文字样式 */
    .navbar-nav .nav-link {
      font-weight: bold;
      font-size: 18px;
    }

    /* 鼠标悬停效果 */
    .navbar-nav .nav-link:hover {
      text-decoration: underline;
    }


img{
  width: 30px;
  border-radius: 50%;

}

/* .text1{
        margin-left: 45px;
        color: white;
    }


     
    .title{
        font-size: 20px;
        font-weight: 900;
        color: black;
    }
    .function{
        font-size: 12px;
        font-weight: 900;
        color: black;
    } */

</style>