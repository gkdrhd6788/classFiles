<template>
    <div>
        <ParentChild 
        my-msg="ssafy" 
        :dynamic-props="name"
        @some-event="someCallBack"
        @emit-args ='getNumbers'
        @update-name = "updateName"
        />
    </div>
</template>

<script setup>
    import ParentChild from '@/components/ParentChild.vue';
    import { ref } from 'vue'
    const name = ref('Alice')
    const someCallBack = function(){
        console.log('ParentChild가 발신한 emit이벤트를 수신했습니다.')
    }
    const getNumbers = function(...args){
        console.log(args)
    }
    const updateName = function(){
        name.value = 'Bella'
    }
</script>

<style scoped>

</style>