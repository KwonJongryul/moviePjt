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
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/searchlist',
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
    component: ReviewCreate
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

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
