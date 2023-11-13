<template>
  <div>
    pinia연습하기
    <ParentPage 
    v-for="familyInfo in store.familyInfos"
    :key = "familyInfo.familyName"
    :familyInfo="familyInfo"
     />
  </div>
</template>

<script setup>
import { useFamilyStore } from '@/stores/family';
import ParentPage from '@/components/ParentPage.vue';

const store = useFamilyStore()

</script>

<style scoped>

</style>