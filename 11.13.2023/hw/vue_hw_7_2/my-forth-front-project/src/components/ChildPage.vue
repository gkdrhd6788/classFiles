<template>
  <div>
    <p>자식 페이지</p>
    {{ child.name }}
  </div>
</template>

<script setup>
  defineProps({
    child:Object
  })
</script>

<style scoped>

</style>