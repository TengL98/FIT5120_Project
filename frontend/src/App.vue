<template>
  <div class="app-wrap">
    <AppHeader :current-path="currentPath" :is-solid="isSolidHeader" />

    <component :is="currentView" />

    <AppFooter />
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import HomePage from './pages/HomePage.vue'
import WhyWalkPage from './pages/WhyWalkPage.vue'
import PlannerPage from './pages/PlannerPage.vue'

const getHashPath = () => {
  const raw = window.location.hash.replace(/^#/, '') || '/'
  return raw.startsWith('/') ? raw : `/${raw}`
}

const currentPath = ref(getHashPath())
const isSolidHeader = ref(false)

const routes = {
  '/': HomePage,
  '/why-walk': WhyWalkPage,
  '/planner': PlannerPage
}

const syncRoute = () => {
  currentPath.value = getHashPath()
  if (!routes[currentPath.value]) {
    window.location.hash = '#/'
    currentPath.value = '/'
  }
  window.scrollTo({ top: 0, behavior: 'auto' })
}

const onScroll = () => {
  isSolidHeader.value = window.scrollY > 24
}

const currentView = computed(() => routes[currentPath.value] || HomePage)

onMounted(() => {
  window.addEventListener('hashchange', syncRoute)
  window.addEventListener('scroll', onScroll)
  syncRoute()
  onScroll()
})

onBeforeUnmount(() => {
  window.removeEventListener('hashchange', syncRoute)
  window.removeEventListener('scroll', onScroll)
})
</script>
