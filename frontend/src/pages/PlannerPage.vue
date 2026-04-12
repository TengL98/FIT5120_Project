<template>
  <main class="planner-page">
    <section class="inner-hero planner-hero">
      <div class="shell">
        <p class="eyebrow">Step Into Planning</p>
        <h1>Choose a destination, get one trusted route.</h1>
        <p>Route suggestions are kept within practical walking range and designed for comfort and confidence.</p>
      </div>
    </section>

    <section class="section">
      <div class="shell planner-layout">
        <aside class="planner-panel">
          <h2>Step 1: Choose destination type</h2>
          <div class="destinations">
            <button
              v-for="item in destinations"
              :key="item.id"
              class="destination-btn"
              :class="{ active: selected === item.id }"
              @click="selected = item.id"
            >
              {{ item.label }}
            </button>
          </div>

          <div v-if="selectedPlan" class="recommend-card">
            <p class="eyebrow dark">Step 2: Recommended Route</p>
            <h3>{{ selectedPlan.name }}</h3>
            <p>{{ selectedPlan.summary }}</p>

            <div class="recommend-metrics">
              <span>{{ selectedPlan.distance }}</span>
              <span>{{ selectedPlan.time }}</span>
              <span>{{ selectedPlan.restStops }} rest points</span>
            </div>

            <ul>
              <li>Prioritises shade and gentler slope</li>
              <li>Shows nearby benches and toilets</li>
              <li>Highlights nearby support services</li>
            </ul>

            <button class="btn btn-primary" @click="showNavigation = true">Step 4: Start Navigation</button>
          </div>
        </aside>

        <section class="planner-visual">
          <div class="route-stage" v-if="selectedPlan">
            <p class="eyebrow dark">Step 3: Confidence-Focused Guidance</p>
            <h3>{{ selectedPlan.name }} route overview</h3>
            <p>
              The suggested path balances comfort with streets that have moderate pedestrian activity,
              so support is easier to find if needed.
            </p>

            <div class="route-bars">
              <div><span>Shade coverage</span><strong>{{ selectedPlan.shade }}</strong></div>
              <div><span>Slope comfort</span><strong>{{ selectedPlan.slope }}</strong></div>
              <div><span>Public activity</span><strong>{{ selectedPlan.activity }}</strong></div>
            </div>

            <div class="route-strip" aria-hidden="true">
              <span class="dot origin"></span>
              <span class="line"></span>
              <span class="dot rest"></span>
              <span class="line"></span>
              <span class="dot support"></span>
              <span class="line"></span>
              <span class="dot destination"></span>
            </div>

            <div class="strip-labels">
              <span>Start</span>
              <span>Bench</span>
              <span>Clinic</span>
              <span>Destination</span>
            </div>

            <div v-if="showNavigation" class="navigation-box">
              <h4>Navigation started</h4>
              <p>You are now on your selected route. Tap each stop to review rest and support options.</p>
              <p class="confidence-line">Step 5: Keep going, build confidence, enjoy a healthier routine.</p>
            </div>
          </div>

          <div v-else class="empty-state">
            <h3>Start from Step 1</h3>
            <p>Select a destination type to see your recommended route.</p>
          </div>
        </section>
      </div>
    </section>
  </main>
</template>

<script setup>
import { computed, ref, watch } from 'vue'

const destinations = [
  { id: 'pharmacy', label: 'Pharmacy' },
  { id: 'library', label: 'Library' },
  { id: 'park', label: 'Park' },
  { id: 'cafe', label: 'Cafe' },
  { id: 'clinic', label: 'Clinic' }
]

const plans = {
  pharmacy: {
    name: 'Carlton Gardens Pharmacy',
    summary: 'A short route with frequent shade and simple crossings.',
    distance: '850 m',
    time: '12 min',
    restStops: 3,
    shade: 'High',
    slope: 'Gentle',
    activity: 'Moderate'
  },
  library: {
    name: 'Carlton Library',
    summary: 'Balanced route with bench access near key intersections.',
    distance: '920 m',
    time: '14 min',
    restStops: 2,
    shade: 'Medium',
    slope: 'Gentle',
    activity: 'Moderate'
  },
  park: {
    name: 'Princes Park South Entry',
    summary: 'Green corridor route with higher shade and wider footpaths.',
    distance: '780 m',
    time: '11 min',
    restStops: 4,
    shade: 'High',
    slope: 'Flat',
    activity: 'Moderate'
  },
  cafe: {
    name: 'Lygon Street Community Cafe',
    summary: 'Comfortable route with nearby toilets and moderate foot traffic.',
    distance: '990 m',
    time: '15 min',
    restStops: 3,
    shade: 'Medium',
    slope: 'Gentle',
    activity: 'Moderate'
  },
  clinic: {
    name: 'Carlton Medical Clinic',
    summary: 'Direct route with nearby support points and smooth surfaces.',
    distance: '860 m',
    time: '13 min',
    restStops: 3,
    shade: 'Medium',
    slope: 'Gentle',
    activity: 'Moderate'
  }
}

const selected = ref('pharmacy')
const showNavigation = ref(false)

const selectedPlan = computed(() => plans[selected.value])

watch(selected, () => {
  showNavigation.value = false
})
</script>
