import $ from 'jquery'



export default {
    state: {
        is_login:false,
        photo:"",
        is_front:true,
        identity:"",
        username:"",
        sex:"",
        bir:"",
        email:'',
        phone:"",
        id:"",
        is_pull:false,
        is_asking:false,
        posts_total:"",
        posts:[],
        ai_answer:[],
        questions:[],
        saved_QAs:[],
    },
    getters: {
    },
    mutations: {
        updateQuesSaved(state,ques) {
           state.saved_QAs = ques;
        },
        updateQues(state,ques) {
            state.questions[4] = state.questions[3];
            state.questions[3] = state.questions[2];
            state.questions[2] = state.questions[1];
            state.questions[1] = state.questions[0];
            state.questions[0] = ques.ques;
        },
        updateAiAnswer(state,AiAnswer) {
            state.ai_answer[4] = state.ai_answer[3];
            state.ai_answer[3] = state.ai_answer[2];
            state.ai_answer[2] = state.ai_answer[1];
            state.ai_answer[1] = state.ai_answer[0];
            state.ai_answer[0] = AiAnswer.ai_answer;
        },
        clearAiAnswer(state) {
            state.ai_answer = [];
        },
        clearquestions(state) {
            state.questions = [];
        },
        updateUserPostsTotal(state,posts_total) {
            state.posts_total = posts_total;
        },
        updateUserPosts(state,posts) {
            state.posts = posts;
        },
        updateIsLogin(state,is_login) {
            state.is_login = is_login;
        },
        updateUsername(state,username) {
            state.username = username;
        },
        updateIsFront(state,is_front) {
            state.is_front = is_front;
        },
        updatePhoto(state,photo) {
            state.photo = photo;
        },
        updateSex(state,sex) {
            state.sex = sex;
        },
        updateBir(state,bir) {
            state.bir = bir;
        },
        updateEmail(state,email) {
            state.email = email;
        },
        updatePhone(state,phone) {
            state.phone = phone;
        },
        updateId(state,id) {
            state.id = id;
        },
        updateIdentity(state,identity) {
            state.identity = identity;
        },
       
    },
    actions: {
        login(context,data){
            $.ajax({
                url: "http://localhost:3000/user/log/",
                type: "get",
                data:{
                    username:data.username,
                    password:data.password,
                },
                success(resp){
                    if (resp.message === "成功登录") {
                        data.success(resp);
                        context.commit("updateIsLogin",true);
                        context.commit("updateIsFront",false);
                        context.commit("updateIdentity",resp.identity);
                        context.commit("updateSex",resp.sex);
                        context.commit("updateBir",resp.bir);
                        context.commit("updateEmail",resp.email);
                        context.commit("updateId",resp.id);
                        context.commit("updatePhoto",resp.photo);
                        context.commit("updatePhone",resp.phone);
                        context.commit("updateUsername",data.username);
                    } 
                    else
                    {
                        data.error(resp);
                    }
                },
                error(resp){
                    data.error(resp);
                }
            })
        },
        logout(context,data){
            $.ajax({
                url: "http://localhost:3000/user/logout/",
                type: "get",
                data:{
                    id:data.id,
                },
                success(resp){
                    if (resp.message === "成功退出") {
                        data.success(resp);
                        context.commit("updateIsLogin",false);
                        context.commit("updateIsFront",true);
                        context.commit("updateIdentity","");
                        context.commit("updateSex","");
                        context.commit("updateBir","");
                        context.commit("updateEmail","");
                        context.commit("updateId","");
                        context.commit("updatePhoto","");
                        context.commit("updatePhone","");
                        context.commit("updateUsername","");
                        context.commit("clearAiAnswer");
                        context.commit("clearquestions");
                    } 
                    else
                    {
                        data.error(resp);
                    }
                },
                error(resp){
                    data.error(resp);
                }
            })
        },
        reg(context,data){
            $.ajax({
                url: "http://localhost:3000/user/reg/",
                type: "get",
                data:{
                    username:data.username,
                    password:data.password,
                    passwordConf:data.passwordConf,
                },
                success(resp){
                    console.log(resp.message+"成功");
                    if (resp.message === "成功注册") {
                        data.success(resp);
                        context.commit("updateIsLogin",true);
                        context.commit("updateUsername",data.username);
                        context.commit("updateId",resp.id);
                        context.commit("updateIsFront",false);
                        context.commit("updatePhoto",resp.photo);
                    } 
                    else
                    {
                        data.error(resp);
                    }
                },
                error(resp){
                    console.log(resp.message+"失败");
                    data.error(resp);
                }
            })
        },
        setInfo(context,data){
            $.ajax({
                url: "http://localhost:3000/user/setinfo/",
                type: "get",
                data:{
                    id:data.id,
                    username:data.username,
                    password:data.password,
                    sex:data.sex,
                    bir:data.bir,
                    email:data.email,
                    phone:data.phone,
                    manufacturer:data.manufacturer,
                    pro_date:data.pro_date
                },
                success(resp){
                    if (resp.message === "修改个人信息成功") {
                        data.success(resp);
                        context.commit("updateUsername",data.username);
                        // context.commit("updatePhoto",data.photo);
                        context.commit("updateSex",data.sex);
                        context.commit("updateBir",data.bir);
                        context.commit("updateEmail",data.email);
                        context.commit("updatePhone",data.phone);
            
                    } 
                    else
                    {
                        data.error(resp);
                    }
                },
                error(resp){
                    data.error(resp);
                }
            })
        },
    },
    modules: {

    }
  }
  