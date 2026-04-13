<template>
  <header class="site-header" :class="{ solid: isSolid }">
    <div class="shell header-inner">
      <a class="brand" href="#/">
        <svg viewBox="0 0 48 48" aria-hidden="true">
          <path d="M8 36L16 27H32L40 36L24 43Z" fill="currentColor" opacity="0.34" />
          <path d="M24 4C17.4 4 12 9.4 12 16C12 25.1 24 35 24 35C24 35 36 25.1 36 16C36 9.4 30.6 4 24 4Z" fill="currentColor" />
          <path d="M24 9C20 12.2 19.2 16.5 21.3 19.2C22.8 16.8 24.5 14.3 27 11.8C25.8 10.4 24.8 9.1 24 9Z" fill="#9bcf61" />
        </svg>
        <span>GreenPath</span>
      </a>

      <nav class="main-nav" aria-label="Primary">
        <a :class="{ active: currentPath === '/' }" href="#/">Home</a>
        <a :class="{ active: currentPath === '/why-walk' }" href="#/why-walk">Why Walk</a>
        <a :class="{ active: currentPath === '/planner' }" href="#/planner">Plan a Route</a>
      </nav>
    </div>
  </header>
</template>

<script setup>
defineProps({
  currentPath: {
    type: String,
    required: true
  },
  isSolid: {
    type: Boolean,
    default: false
  }
})
</script>
