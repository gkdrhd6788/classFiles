<template>
  <div>
    <form @submit.prevent="createTodo()">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter';
  import { ref } from 'vue'
  const todoText = ref('')
  const store = useCounterStore()

  const createTodo = function(){
    store.addTodo(todoText.value)  //혹은 교재처럼 해도 된다.
    todoText.value = '' //혹은 교재처럼 해도 된다.
  }
</script>

<style scoped>

</style>