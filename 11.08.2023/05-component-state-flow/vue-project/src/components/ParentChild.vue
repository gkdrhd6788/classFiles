<template>
    <div>
        <p> {{ myMsg }} </p>
        <p> {{ dynamicProps }}</p>
        <ParentGrandChild
         :my-msg="myMsg"
         @update-name="updateName"
         />
        <button @click="$emit('someEvent')">클릭</button>
        <button @click="buttonClick">클릭</button>
        <button @click="emitArgs">추가 인자 전달</button>
        
    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// 1. 문자열 배열 선언 방식
//     defineProps(['myMsg'])
// 2. 객체 선언 방식(유효성 검사 가능)-권장
    defineProps({
        // myMsg : String, //기본적
        dynamicProps: String,
        myMsg : {       //유효성 검사
            type: String,
            required:true,
            // validator(value) {
            //     return ['success','waring','danger'].includes(value)
            // }
            validator(value){
                const validValues = ['success','warning','danger']
                if (!validValues.includes(value)){
                    console.error('에러입니다.')
                    return false
                } 
                return true
            }
        }
    })

    //props데이터를 script에서 사용하려면
    // const props = defineProps({
    //     myMsg : String, //기본적
    //     })
    // console.log(props)
    // console.log(props.myMsg)

    // emit 선언 방식
    const emit = defineEmits(['someEvent','emitArgs','updateName'])
    const buttonClick = function(){
        emit('someEvent')
    }
    const emitArgs = function(){
        emit('emitArgs',1,2,3)
    }
    const updateName = function(){
        emit('updateName')
    }
</script>

<style scoped>

</style>