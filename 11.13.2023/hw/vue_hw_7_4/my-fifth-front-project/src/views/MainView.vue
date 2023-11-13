<template>
  <h1> 메인 페이지 </h1>
  <MainPage 
  v-for="balance in store.balances"
  :balance="balance"
  />
</template>

<script setup>
  import { useBalanceStore } from '@/stores/balance';
  import MainPage from '@/components/MainPage.vue';

  const store= useBalanceStore()

</script>

<style scoped>

</style>