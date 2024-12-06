


export default {
    // namespaced: true,
    state: {
        reports:[],
        current_page:"",
        total_pages:"",
        total_reports:"",


    },
    getters: {
     
    },
    mutations: {
        updateReports(state,reports){
            state.reports = reports;
        },
        updateCurrentPage(state,currentPage){
            state.current_page = currentPage;
        },
        updateTotalPages(state,totalPages){
            state.total_pages = totalPages;
        },
        updateTotalReports(state,totalReports){
            state.total_reports = totalReports;
        }

    },
    actions: {
        updateTotalRecord(context,record){
            context.commit("updateReports",record.reports);
            context.commit("updateCurrentPage",record.currentPage);
            context.commit("updateTotalPages",record.totalPages);
            context.commit("updateTotalReports",record.totalReports);

        }

        
    },
    modules: {
     
      
    }
  }
  