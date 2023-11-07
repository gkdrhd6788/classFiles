<template>
    <div>
        <h1>가수 목록</h1>
        <SingerDetail v-for="singer in singers"/>

    </div>
</template>

<script setup>
 import { ref } from 'vue'
 import SingerDetail from './singer/SingerDetail.vue';
 const singers = ref([{name:'adele'},{name:'maroon5'},{name:'Dua Lipa'}])

</script>
<style scoped>
    * {
        text-align: center;
    }
    h1 {
        color: orangered;
    }
</style>