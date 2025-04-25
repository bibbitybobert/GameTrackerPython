import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue'),
      meta: {hideNav: true}
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/RegisterView.vue'),
      meta: {hideNav: true}
    },
    {
      path: '/new',
      children: [
        {
          path: 'game',
          component: () => import('@/views/NewGameView.vue'),
        },
        {
          path: 'launcher',
          component: () => import('@/views/NewLauncherView.vue'),
        },
        {
          path: 'tag',
          component: () => import('@/views/NewTagView.vue'),
        }
      ]
    }
  ],
})

export default router
