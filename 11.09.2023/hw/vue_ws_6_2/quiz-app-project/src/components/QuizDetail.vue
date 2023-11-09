<template>
    <div>
         <p> {{ quiz.pk }}번 문제. {{ quiz.question }} </p>
        <label :for="quiz.pk" >정답 입력</label>
        <input type="text" :id="quiz.pk">
    </div>
</template>

<script setup>
defineProps({
    quiz: Object
})
</script>

<style scoped>

</style>