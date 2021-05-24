import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/ping/',
  routes: [
    {
      path: '/',
      name: 'Ping',
      component: () => import('@/components/Ping')
    },
    {
      path: '/pong',
      name: 'Pong',
      component: () => import('@/components/Pong')
    }
  ]
})
