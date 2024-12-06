<template>

    <div class="row">
      

        <div class="col-9" style="margin-left: 13%"  >
            <ContentBase>

            <div class="row">
                <table class="table table-striped table-hover" style="text-align: center;">


<thead>
    <tr>
        <th class="col-4">害虫名称</th>
        <th class="col-4">害虫图片</th>

        <th class="col-4">操作</th>
    </tr>
</thead>



<tbody>
   
    <tr v-for="vermin in verminset" :key="vermin.id">
        <td>
            {{ vermin.vermin_name }}
        </td>
        <td>
            <img style="width: 100px;" :src=vermin.image_url alt="害虫图片">
        </td>
        <td>
            <button type="button" class="btn  btn-success"  @click="getDetailedVermin(vermin.id)">下载详细信息</button>
        </td >
        
           

       
    </tr>
   

</tbody>
</table>

            </div>



            
        <nav aria-label="...">
        <ul class="pagination" style="float: left;">
            <li class="page-item" >
                <a class="page-link" href="#"  @click="ToOpera">返回</a>
            </li>
         
    
        </ul>
        </nav>


        <nav aria-label="...">
        <ul class="pagination" style="float: right;">
            <li class="page-item"  v-if="current_page!==1">
                <a class="page-link" href="#"  @click="pageUp">前一页</a>
            </li>
            <li class="page-item" >
                <a class="page-link" href="#">{{ current_page }}</a>
            </li>
            <li class="page-item" v-if="current_page!==total_pages">
                <a class="page-link" href="#" @click="pageDown">后一页</a>
            </li>
        </ul>
        </nav>
            </ContentBase>
        </div>
       

      
    </div>

        

    </template>
    
    <script>

 import { useRouter } from 'vue-router';
 import { useStore } from 'vuex';
 import ContentBase from '@/components/ContentBase.vue'
import $ from 'jquery'
import { Document, Packer, Paragraph, TextRun } from "docx";
import { saveAs } from "file-saver";
import { ref } from 'vue'



    export default{
        components:{
   ContentBase
        },
        setup(){
           
            const router = useRouter();
            const store = useStore();

            const verminset = ref([]);
            verminset.value=store.state.vermin.verminset;

            const current_page = ref(0);
            current_page.value = store.state.vermin.current_page;
            
            const total_vermins = ref(0);
            total_vermins.value = store.state.vermin.total_vermin;

            const total_pages = ref(0);
            total_pages.value = store.state.vermin.total_pages;


            const getDetailedVermin = (id)=>{
                $.ajax({
                    url: "http://localhost:3000/user/checkvermin/",
                    type:"get",
                    data:{
                        id:id
                    },
                    success(resp){
                        const generateWord = () => {
                            const doc = new Document({
                                sections: [
                                {
                                    properties: {},
                                    children: [

                              


                                    new Paragraph({
                                        children: [
                                        new TextRun({
                                            text: "害虫名称:"+resp.vermin_name,
                                            bold: true,
                                            font: "Microsoft YaHei", // 设置字体支持中文
                                        }),
                                        ],
                                    }),
                                    new Paragraph({
                                    children: [], // 这就是空段落
                                }),


                                    new Paragraph({
                                        children: [
                                        new TextRun({
                                            text: "害虫图片url: "+resp.image_url,
                                            bold: true,
                                            font: "Microsoft YaHei", // 设置字体支持中文
                                        }),
                                        ],
                                    }),
                                    new Paragraph({
                                    children: [], // 这就是空段落
                                }),


                                    new Paragraph({
                                        children: [
                                        new TextRun({
                                            text: "害虫基本信息:"+resp.base_info,
                                            bold: true,
                                            font: "Microsoft YaHei", // 设置字体支持中文
                                        }),
                                        ],
                                    }),
                                    new Paragraph({
                                    children: [], // 这就是空段落
                                }),


                                    new Paragraph({
                                        children: [
                                        new TextRun({
                                            text: "害虫治理方法:"+resp.suggested_measure,
                                            bold: true,
                                            font: "Microsoft YaHei", // 设置字体支持中文
                                        }),
                                        ],
                                    }),
                                    new Paragraph({
                                    children: [], // 这就是空段落
                                }),





                                    ],
                                },
                                ],
                            });

                                Packer.toBlob(doc).then((blob) => {
                                    saveAs(blob, resp.vermin_name+"害虫信息.docx");
                                    console.log("Word文档已生成！");
                                });
                                };

                            setTimeout(()=>{     generateWord() }, 1000)
                    },
                    error(resp){
                       console.log(resp);
                    }});
            };



            const pageUp=()=>{
          $.ajax({
                url:"http://localhost:3000/user/verminpageup/",
                type:"get",
                data:{
                    page:store.state.vermin.current_page
                },
                success(resp){
                    if (resp.message === "success") {
                        store.dispatch("updateTotalVermins",{
                            vermins:resp.vermins,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            total_vermins:resp.total_vermins
                        })

                verminset.value=store.state.vermin.verminset;
                current_page.value = store.state.vermin.current_page;
                total_vermins.value = store.state.vermin.total_vermin;
                total_pages.value = store.state.vermin.total_pages;

               
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


        const pageDown=()=>{
            $.ajax({
                url:"http://localhost:3000/user/verminpagedown/",
                type:"get",
                data:{
                    page:store.state.record.current_page,
                },
                success(resp){
                    if (resp.message === "success") {
                        store.dispatch("updateTotalVermins",{
                            vermins:resp.vermins,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            total_vermins:resp.total_vermins
                        })
                      

                verminset.value=store.state.vermin.verminset;
                current_page.value = store.state.vermin.current_page;
                total_vermins.value = store.state.vermin.total_vermin;
                total_pages.value = store.state.vermin.total_pages;


                      
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

        const ToOpera=()=>{
            router.push({name:"operationpage"})
        }


       
       

            return{
                    router,
                    store,
                    getDetailedVermin,
                    total_pages,
                    total_vermins,
                    verminset,
                    pageUp,
                    pageDown,
                    current_page,
                    ToOpera,
              
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