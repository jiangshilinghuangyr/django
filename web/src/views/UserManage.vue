<template>

    <div class="row">
        <div class="col-11">
            <ContentBase>
                <table class="table table-striped table-hover" style="text-align: center;">

            <thead>
                <tr>
                    <th>注册日期</th>
                    <th>最近上线时间</th>
                    <th>用户名</th>
                    <th>性别</th>
                    <th>电话号码</th>
                    <th>在线状态</th>
                    <th>删除</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                     2024/10/24 17：26
                    </td>
                    <td>
                    2024/10/27 20：28
                    </td>
                    <td>
                        Klassisk
                    </td>
                    <td>
                        男
                    </td>
                    <td>
                       15576611234
                    </td>
                    <td>
                       在线
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" @click="deleteUser">删除用户</button>
                    </td>
                </tr>

                <tr>
                    <td>
                     2024/10/24 17：26
                    </td>
                    <td>
                    2024/10/27 20：28
                    </td>
                    <td>
                        Klassisk
                    </td>
                    <td>
                        男
                    </td>
                    <td>
                       15576611234
                    </td>
                    <td>
                       在线
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" @click="deleteUser">删除用户</button>
                    </td>
                </tr>


                <tr>
                    <td>
                     2024/10/24 17：26
                    </td>
                    <td>
                    2024/10/27 20：28
                    </td>
                    <td>
                        Klassisk
                    </td>
                    <td>
                        男
                    </td>
                    <td>
                       15576611234
                    </td>
                    <td>
                       在线
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" @click="deleteUser">删除用户</button>
                    </td>
                </tr>


                <tr>
                    <td>
                     2024/10/24 17：26
                    </td>
                    <td>
                    2024/10/27 20：28
                    </td>
                    <td>
                        Klassisk
                    </td>
                    <td>
                        男
                    </td>
                    <td>
                       15576611234
                    </td>
                    <td>
                       在线
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" @click="deleteUser">删除用户</button>
                    </td>
                </tr>


                <tr>
                    <td>
                     2024/10/24 17：26
                    </td>
                    <td>
                    2024/10/27 20：28
                    </td>
                    <td>
                        Klassisk
                    </td>
                    <td>
                        男
                    </td>
                    <td>
                       15576611234
                    </td>
                    <td>
                       在线
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" @click="deleteUser">删除用户</button>
                    </td>
                </tr>


                <tr>
                    <td>
                     2024/10/24 17：26
                    </td>
                    <td>
                    2024/10/27 20：28
                    </td>
                    <td>
                        Klassisk
                    </td>
                    <td>
                        男
                    </td>
                    <td>
                       15576611234
                    </td>
                    <td>
                       在线
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" @click="deleteUser">删除用户</button>
                    </td>
                </tr>
          
            </tbody>
        </table>
            </ContentBase>
        </div>
       

      
    </div>

        

    </template>
    
    <script>

 import { useRouter } from 'vue-router';
 import { useStore } from 'vuex';
 import ContentBase from '@/components/ContentBase.vue'
    export default{
        components:{
   ContentBase
        },
        setup(){
            const router = useRouter();
            const store = useStore();
            const deleteUser = ()=>{
                console.log("删除用户")
            };

            return{
                    router,
                    store,
                    deleteUser,
                }
        
        }
    }
    </script>
    
    <style scoped>
.btn1{
    margin-top:20px ;
}

.row{
    margin-left: 45px;
    margin-right: 45px;
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

    </style>