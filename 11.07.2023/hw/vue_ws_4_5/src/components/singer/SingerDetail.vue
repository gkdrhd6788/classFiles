<template>
    <div class="card">
        <h2>가수 이름</h2>
        <img src="@/assets/singer.jpg" alt="singer">
        <h3>가수 소개글</h3>
        <singerAlbum/><singerAlbum/>
    </div>
</template>

<script setup>
 import singerAlbum from './singerAlbum.vue';
</script>

<style scoped>
    img {
        width: 200px;
        border-radius: 70%;
    }
    
    .card {
        display: inline-block;
        width: 40%;
        margin: 20px;
        border: 1px solid black;
    }
    
</style>
