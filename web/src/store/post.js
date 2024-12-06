


export default {

    state: {
        posts:[],
        current_page:"",
        total_pages:"",
        total_posts:"",
        usernames:[],


    },
    getters: {
     
    },
    mutations: {
        updatePosts(state,posts){
            state.posts = posts;
        },
        updateUsernames(state,usernames){
            state.usernames = usernames;
        },
        updateCurrentPage(state,currentPage){
            state.current_page = currentPage;
        },
        updateTotalPages(state,totalPages){
            state.total_pages = totalPages;
        },
        updateTotalPosts(state,total_posts){
            state.total_posts = total_posts;
        }

    },
    actions: {
        updateTotalPosts(context,posts){
            context.commit("updatePosts",posts.posts);
            context.commit("updateCurrentPage",posts.currentPage);
            context.commit("updateTotalPages",posts.totalPages);
            context.commit("updateTotalPosts",posts.total_posts);
            context.commit("updateUsernames",posts.usernames);

        }

        
    },
    modules: {
     
      
    }
  }
  