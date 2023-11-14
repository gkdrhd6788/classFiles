import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdate from '@/components/ArticleUpdate.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/update/:id',
      name: 'update',
      component: ArticleUpdate
    },

  ]
})

export default router
