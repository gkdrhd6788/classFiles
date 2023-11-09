<template>
    <div>
        <h1>학생 상세 정보 목록입니다.</h1>
        <p 
        v-for="student in students"
        @click="goDetail(student.name)"
        > 
        {{ student.name }} 학생 정보 보기 </p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const goDetail = function(studentName){
    router.push({name:'studentsDetail',params:{name:studentName}})
}
const students = ref([
    {name:'김하나'},
    {name:'김두리'},
    {name:'김서이'}
])
</script>

<style scoped>

</style>