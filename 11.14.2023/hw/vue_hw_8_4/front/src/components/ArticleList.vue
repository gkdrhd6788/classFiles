<template>
  <div>
    <RouterLink :to="{ name:'create'}"> 게시글 생성 </RouterLink>
    <div v-for="article in store.articles">
      <strong>{{ article.id }}번 게시글</strong>  
      <p> 제목: {{ article.title }}</p>
      <p> 내용: {{ article.content }}</p>
      <button @click="deleteArticle(article.id)">삭제</button>
      <button @click="goUpdate(article.id)">수정</button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { RouterLink, useRouter } from 'vue-router'
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()
const router = useRouter()

const deleteArticle = function (id) {
  axios({
    method:'delete',
    url: `http://127.0.0.1:8000/api/v1/articles/${id}/`
  })
    .then(()=>{
      // console.log('삭제 성공')
      store.getArticles()
      // router.push({name:'home'})
    })
    .catch(()=>{
      console.log('삭제 실패')
    })
}

const goUpdate = function(id){
  router.push({name:'update',params:{id:id}})
}

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

</style>