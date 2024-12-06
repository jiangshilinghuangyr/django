<template>

    <div class="container">
        <div class="card">
            <div class="card-body">



                <div class="row" style="display: flex;align-items: center;" >
                    <div class="col-3">

                    </div>

                    <div class="col-6" style="font-size: 20px;font-weight: 900;" >
                        <label for="exampleFormControlTextarea1" class="form-label">向AI提问</label>
                        <textarea v-model="question" class="form-control" id="exampleFormControlTextarea1" rows="4"></textarea>
                        
                    
                    </div>
                        <div class="col-3">
                        <button  class="btn btn-primary" style="margin-left: 6px;margin-top: 30px; " type="button" disabled v-if="store.state.user.is_asking">
                        <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                        <span >请等待</span>
                        </button>
                        <div></div>
                        <button @click="aianswer" style="margin-left: 6px; margin-top: 30px;" type="button" class="btn btn-primary">提交</button>
                        </div>
                </div>






                
                <div style="margin-top: 20px; margin-bottom: 20px;" class="card" v-if="store.state.user.questions[0]!==undefined">
                        <div class="card-body">
                           "Ques:"{{ store.state.user.questions[0] }}
                           <button @click="save(store.state.user.questions[0], store.state.user.ai_answer[0])" style="margin-left: 30px;" type="button" class="btn btn-success">保存此次问答</button>
                        </div>
                        <div class="card-body">
                            "Answer:"{{ store.state.user.ai_answer[0] }}
                        </div>
                    </div>
             


                    




                    
                    <div style="margin-top: 20px; margin-bottom: 20px;" class="card" v-if="store.state.user.questions[1]!==undefined">
                        <div class="card-body">
                            "Ques:"{{ store.state.user.questions[1] }}
                            <button @click="save(store.state.user.questions[1], store.state.user.ai_answer[1])" style="margin-left: 30px;" type="button" class="btn btn-success">保存此次问答</button>
                        </div>
                        <div class="card-body">
                            "Answer:"{{ store.state.user.ai_answer[1] }}
                        </div>
                    </div>
                    
                





                    <div style="margin-top: 20px; margin-bottom: 20px;" class="card" v-if="store.state.user.questions[2]!==undefined">
                        <div class="card-body">
                            "Ques:"{{ store.state.user.questions[2] }}
                            <button @click="save(store.state.user.questions[2], store.state.user.ai_answer[2])" style="margin-left: 30px;" type="button" class="btn btn-success">保存此次问答</button>
                        </div>
                        <div class="card-body">
                            "Answer:"{{ store.state.user.ai_answer[2] }}
                        </div>
                    </div>
                   
        








                    <div style="margin-top: 20px; margin-bottom: 20px;" class="card" v-if="store.state.user.questions[3]!==undefined">
                        <div class="card-body">
                            "Ques:"{{ store.state.user.questions[3] }}
                            <button @click="save(store.state.user.questions[3], store.state.user.ai_answer[3])" style="margin-left: 30px;" type="button" class="btn btn-success">保存此次问答</button>
                        </div>
                        <div class="card-body">
                            "Answer:"{{ store.state.user.ai_answer[3] }}
                        </div>
                    </div>
                  


                    
        







                    <div style="margin-top: 20px; margin-bottom: 20px;" class="card" v-if="store.state.user.questions[4]!==undefined">
                        <div class="card-body">
                            "Ques:"{{ store.state.user.questions[4] }}
                            <button @click="save(store.state.user.questions[4], store.state.user.ai_answer[4])" style="margin-left: 30px;" type="button" class="btn btn-success">保存此次问答</button>
                        </div>
                        <div class="card-body">
                            "Answer:"{{ store.state.user.ai_answer[4] }}
                        </div>
                    </div>
                

                  


                    
        
        

            </div>
        </div>
    </div>



</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import $ from 'jquery'

export default{
    setup() {
        const store=useStore();
        const question = ref("");
        const aianswer = ()=>{
            store.state.user.is_asking = true;
               $.ajax({
                   url:"http://localhost:3000/user/aianswer/",
                   type: "get",
                   data:{
                    question:question.value
                   },
                   success(resp){
                    
                   if (resp.message === "success") {
                    store.commit("updateAiAnswer",{
                        ai_answer:resp.ai_content,
                    });

                    store.commit("updateQues",{
                        ques:question.value,
                    });
                    store.state.user.is_asking = false;
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
          };
          const save = (question,answer)=>{
               $.ajax({
                   url:"http://localhost:3000/user/saveaianswer/",
                   type: "get",
                   data:{
                    userid:store.state.user.id,
                    question:question,
                    answer:answer,
                   },
                   success(){
                   console.log("success");
                    },
                    error(){
                        console.log("未成功");
                    }
                    })
          }

          return{
            store,
            aianswer,
            question,
            save
          }
}
}


</script>

<style scoped>

</style>