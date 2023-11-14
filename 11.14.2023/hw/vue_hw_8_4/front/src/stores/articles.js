import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then((res) => {
      console.log(res)
      articles.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  const createArticles = function(title,content){
    axios({
      method:'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title, 
        content,
      }
    })
    .then((res)=>{
      // console.log('생성 성공')
      router.push({name:'home'})
    })
    .catch((err)=>{
      console.log('생성 실패')
    })
  }

  return { articles, getArticles, createArticles }
})
