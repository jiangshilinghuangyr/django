


export default {

    state: {
        verminset:[],
        current_page:"",
        total_pages:"",
        total_vermin:"",


    },
    getters: {
     
    },
    mutations: {
        updateverminset(state,VerminSet){
            state.verminset = VerminSet;
        },
        updateCurrentPage(state,currentPage){
            state.current_page = currentPage;
        },
        updateTotalPages(state,totalPages){
            state.total_pages = totalPages;
        },
        updateTotalVermins(state,total_vermin){
            state.total_reports = total_vermin;
        }

    },
    actions: {
        updateTotalVermins(context,vermins){
            context.commit("updateverminset",vermins.vermins);
            context.commit("updateCurrentPage",vermins.currentPage);
            context.commit("updateTotalPages",vermins.totalPages);
            context.commit("updateTotalVermins",vermins.total_vermins);

        }

        
    },
    modules: {
     
      
    }
  }
  