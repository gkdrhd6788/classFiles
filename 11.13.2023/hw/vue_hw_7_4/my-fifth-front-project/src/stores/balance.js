import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
    ])

  const getObject = computed(()=>{
    const func = function (userName) {
      const result = balances.value.find((balance) => {
        return balance.name === userName
      })
      return result
    } 
    return func
  })
  
  const addAccount = function(userName){
    getObject(userName).value.balance += 1000
  }

  return { balances, getObject,addAccount}
})
