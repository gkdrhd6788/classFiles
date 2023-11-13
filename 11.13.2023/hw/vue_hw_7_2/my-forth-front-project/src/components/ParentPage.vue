<template>
  <div>
    <h1>부모 컴포넌트</h1>
    {{ familyInfo.father }}/
    {{ familyInfo.mother }}
    <ChildPage 
    v-for="child in familyInfo.children"
    :child="child"/>
  </div>
</template>

<script setup>
  import ChildPage from '@/components/ChildPage.vue';
  defineProps ({
    familyInfo : Object
  })
</script>

<style scoped>

</style>