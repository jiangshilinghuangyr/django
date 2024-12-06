<template>

    <div class="row">
      

        <div class="col-9" style="margin-left: 13%"  >
            <ContentBase>

            <div class="row">



                <table class="table table-striped table-hover" style="text-align: center;">

<thead>
    <tr>
        <th class="col-2">日期</th>
        <th class="col-2">报告id</th>
        <th class="col-2">温度</th>
        <th class="col-4">操作</th>
   
      
    </tr>
</thead>
<tbody>
   
    <tr v-for="report in reports" :key="report.id">
        <td>
            {{ report.gen_date }}
        </td>
        <td>
            {{ report.id }}
        </td>
        <td>
            {{ report.temperature }}
        </td>
        <td>
            <button type="button" class="btn  btn-success" style="margin-left: 150px" @click="getDetailedRecord(report.id)">下载详细报告</button>
            <button type="button" class="btn btn-secondary"  style="margin-left: 5px;" @click="deleteRecord(report.id)">删除报告</button>
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

            const reports = ref([]);
            reports.value=store.state.record.reports;

            const current_page = ref(0);
            current_page.value = store.state.record.current_page;
            
            const total_reports = ref(0);
            total_reports.value = store.state.record.total_reports;

            const total_pages = ref(0);
            total_pages.value = store.state.record.total_pages;


            const getDetailedRecord = (id)=>{
                $.ajax({
                    url: "http://localhost:3000/user/checkrecord/",
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
                                            text: "报告日期:"+resp.date,
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
                                            text: "天气："+resp.weather+"   温度："+resp.temperature,
                                            bold: true,
                                            font: "Microsoft YaHei", // 设置字体支持中文
                                            break: 1
                                        }),
                        
                                        ],
                                    }),
                                    new Paragraph({
                                    children: [], // 这就是空段落
                                }),
                     
                           


                                    new Paragraph({
                                        children: [
                                        new TextRun({
                                            text: "无人机类型:"+resp.drone_pro+"       无人机生产日期:"+resp.drone_date+"           无人机名称:"+resp.drone_name,
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
                                            text: "图片url:http://localhost:3000/media/"+resp.photo,
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
                                            text: "土壤种类:"+resp.soil_name+"   "+"土壤湿度:"+resp.soil_moisture,
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
                                            text: "作物名称:"+resp.crop_name,
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
                                            text: "作物基本信息:"+resp.crop_basic,
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
                                            text: "作物生长习性:"+resp.crop_habit,
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
                                            text: "害虫基本信息:"+resp.vermin_basic,
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
                                            text: "害虫治理方法:"+resp.vermin_measure,
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
                                    saveAs(blob, id+"报告.docx");
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
                url:"http://localhost:3000/user/recordpageup/",
                type:"get",
                data:{
                    id:store.state.user.id,
                    page:store.state.record.current_page
                },
                success(resp){
                    if (resp.message === "success") {
                        store.dispatch("updateTotalRecord",{
                            reports:resp.records,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            totalReports:resp.total_reports
                        })


                         reports.value = store.state.record.reports;
                        current_page.value = store.state.record.current_page;
                        total_reports.value = store.state.record.total_reports;
                        total_pages.value = store.state.record.total_pages;

               
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
                url:"http://localhost:3000/user/recordpagedown/",
                type:"get",
                data:{
                    id:store.state.user.id,
                    page:store.state.record.current_page
                },
                success(resp){
                    if (resp.message === "success") {
                        store.dispatch("updateTotalRecord",{
                            reports:resp.records,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            totalReports:resp.total_reports
                        })
                        reports.value = store.state.record.reports;
                        current_page.value = store.state.record.current_page;
                        total_reports.value = store.state.record.total_reports;
                        total_pages.value = store.state.record.total_pages;


                      
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


        const  deleteRecord=(id)=>{
            $.ajax({
                url:"http://localhost:3000/user/deleterecord/",
                type:"post",
                data:{
                    id:id,
                },
                success(resp){
                    if (resp.message === "success") {
                        

                        $.ajax({
                url:"http://localhost:3000/user/recordpagedown/",
                type:"get",
                data:{
                    id:store.state.user.id,
                    page: Number(store.state.record.current_page)-1
                },
                success(resp){
                    if (resp.message === "success") {
                        store.dispatch("updateTotalRecord",{
                            reports:resp.records,
                            currentPage:resp.current_page,
                            totalPages:resp.total_pages,
                            totalReports:resp.total_reports
                        })
                        reports.value = store.state.record.reports;
                        current_page.value = store.state.record.current_page;
                        total_reports.value = store.state.record.total_reports;
                        total_pages.value = store.state.record.total_pages;


                      
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

                
                }
          })
        }
      
       

            return{
                    router,
                    store,
                    getDetailedRecord,
                    total_pages,
                    total_reports,
                    reports,
                    pageUp,
                    pageDown,
                    current_page,
                    ToOpera,
                    deleteRecord
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

    </style>