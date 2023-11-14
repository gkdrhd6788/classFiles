<template>
  <h1>게시글 생성 페이지</h1>
  <form @submit.prevent="store.createArticles(title,content)">
    <div> 
      <label for="text">제목:</label>
      <input id="text" type="text" v-model="title">
    </div>
    <div>
      <label for="content">내용: </label>
      <input id='content' type="text" v-model="content">
      <input type="submit" value="create">
    </div>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import { useArticleStore } from '@/stores/articles'
  const title = ref('')
  const content = ref('')
  const store = useArticleStore()



</script>

<style scoped>

</style>