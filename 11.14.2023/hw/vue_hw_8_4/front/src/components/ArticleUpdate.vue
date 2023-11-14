<template>
    <h1>업데이트 하기</h1>
    <form @submit.prevent="update($route.params.id)">
      <div> 
        <label for="text">제목:</label>
        <input id="text" type="text" v-model="title">
      </div>
      <div>
        <label for="content">내용: </label>
        <input  id='content' type="text" v-model="content">
        <input type="submit" value="create">
      </div>
  </form>
</template>

<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { ref ,onMounted } from 'vue'

const route = useRoute()

const article = ref({})
const title = ref('')   //여기서 받아오면 안됨!(순서상)
const content = ref('')


onMounted(()=>{
  axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`
    })
    .then((res) => {
      article.value = res.data
      title.value = res.data.title  //여기서 받아와야한다
      content.value = res.data.content 
      console.log(article.value)
    })
    .catch((err)=>{
      console.log(err)
    })
  })

const update= function(id){
  axios({
    method:'put',
    url: `http://127.0.0.1:8000/api/v1/articles/${id}/`,
    data:{
      title: title.value,
      content: content.value,
    }
  })
    .then((res)=>{
      console.log(res)
      console.log('수정 성공')
    })
    .catch((err)=>{
      console.log(err)
    })
}
</script>

<style scoped>

</style>