<template>
    <div>
        <h1>QuizCreate</h1>
        <form @submit.prevent="createQuiz">
            <label for="create_problem">문제</label>
            <textarea name="prob" id="create_problem" cols="30" rows="10" v-model="createdProb"></textarea>
            <label for="create_answer">답안</label>
            <input type="text" id="create_answer" v-model="createdAnsw">
            <button>퀴즈 생성</button>
        </form>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    const createdProb = ref('')
    const createdAnsw = ref('')

    const emit = defineEmits()
    const createQuiz = function(event){
        emit('createQuiz',{ question: createdProb.value,answer: createdAnsw.value,})
        createdProb.value = ''
        createdAnsw.value = ''

}
</script>

<style scoped>

</style>