<template>
  <h1>데이터 수정 페이지</h1>
  <p>이름: {{ $route.params.name }}</p>
  <p>잔고: {{ object.balance }}</p>
   <button @click="store.addAccount">+</button>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRoute  } from 'vue-router';
  import { useBalanceStore } from '@/stores/balance';
  const route = useRoute()
  const userName = ref(route.params.name)
  const store = useBalanceStore()
  const object = store.getObject(userName.value)

  
</script>

<style scoped>

</style>