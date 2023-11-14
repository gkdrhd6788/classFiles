import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const articles =ref([
    //임시 데이터(앞으로는 Django Server에서 받음)
    // { id:1, title:'Article 1',content:'Content 1'},
    // { id:2, title:'Article 2',content:'Content 2'},
  
  ])
  const API_URL = 'http://127.0.0.1:8000'
  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function(){
    axios({
      method:'get',
      url : `${API_URL}/api/v1/articles/`,
    })
    .then ((res)=>{
      // console.log(res)
      articles.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }
  return { articles, API_URL, getArticles}
}, { persist: true })
