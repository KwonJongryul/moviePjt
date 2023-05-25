import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import SearchView from '@/views/SearchView'
import MovieDetailView from '@/views/MovieDetailView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import ReviewView from '@/views/ReviewView';
import ReviewCreate from '@/views/ReviewCreate'
import ReviewDetail from '@/views/ReviewDetail'
import ReviewUpdate from '@/views/ReviewUpdate'
import ProfileView from '@/views/ProfileView'
import ProfileUpdate from '@/views/ProfileUpdate'
import store from "@/store"
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/searchlist/:word',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/review',
    name: 'review',
    component: ReviewView
  },
  {
    path: '/review/create',
    name: 'ReviewCreate',
    component: ReviewCreate,
  },
  {
    path: '/review/:id',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/review/update/:id',
    name: 'ReviewUpdate',
    component: ReviewUpdate
  },
  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/profile/:id/update',
    name: 'ProfileUpdate',
    component: ProfileUpdate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  duplicateNavigationPolicy: 'ignore',
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.islogin
  const authPasges = ['ReviewCreate', 'ReviewDetail', 'ReviewUpdate', 'ProfileView']
  const isAuthReqired = authPasges.includes(to.name)
  if (isAuthReqired && !isLoggedIn){
    alert('로그인이 필요한 페이지입니다')
    store.commit('SET_REDIRECT_PATH', to.fullPath)
    next({
      name:'LoginView',
    })
  }else{
    next()
  }
})

export default router
