<template>
  <main class="route-planner-page" :class="{ 'is-route-view': isRouteView }">
    <div class="planner-scene" aria-hidden="true"></div>
    <div class="planner-scene-overlay" aria-hidden="true"></div>

    <section class="planner-shell" v-if="!isRouteView">
      <article class="planner-card planner-start-card">
        <h1>Let's start your journey</h1>
        <p class="planner-start-label">Starting from</p>
        <div class="planner-location-row">
          <div class="planner-location-chip">
            <img class="planner-location-icon" :src="locationIcon" alt="" aria-hidden="true" />
            <div>
              <strong>{{ locationLabel }}</strong>
            </div>
          </div>
          <button class="btn btn-light planner-location-btn" @click="useMyLocation" :disabled="isLocating || isLoadingPlan">
            {{ isLocating ? 'Locating...' : 'Use my current location' }}
          </button>
        </div>
      </article>

      <article class="planner-card planner-type-card-wrap" ref="typeSectionEl">
        <h2>Where would you like to go?</h2>
        <div class="planner-type-grid">
          <button
            v-for="item in destinationTypes"
            :key="item.id"
            class="planner-type-card"
            :class="{ active: selectedType === item.id }"
            :disabled="isLoadingPlan || isLocating"
            @click="selectedType = item.id"
          >
            <span class="planner-type-icon" aria-hidden="true">
              <img :src="item.icon" alt="" />
            </span>
            <span class="planner-type-name">{{ item.label }}</span>
          </button>
        </div>
      </article>

      <section class="planner-result-anchor" ref="resultAnchorEl">
        <article v-if="hasSelectedType && isLoadingPlan" class="planner-card planner-result-loading-card">
          <span class="planner-spinner" aria-hidden="true"></span>
          <h3>Searching route options...</h3>
          <p>Please wait while we find a nearby destination and supporting facilities.</p>
        </article>

        <article v-else-if="hasSelectedType && hasDestination" class="planner-card planner-result-card">
          <figure class="planner-result-image-wrap">
            <img :src="resultImage" :alt="`${selectedTypeLabel} route preview`" loading="lazy" />
            <figcaption>Top pick for accessibility</figcaption>
          </figure>

          <div class="planner-result-content">
            <h3>{{ result.destination.name }}</h3>

            <div class="planner-metric-row">
              <span class="planner-metric-chip">
                <img :src="walkIcon" alt="" aria-hidden="true" />
                <strong>{{ distanceMetric.value }}</strong>
                <em>{{ distanceMetric.unit }}</em>
                <small>away</small>
              </span>
              <span class="planner-metric-chip">
                <img :src="timeIcon" alt="" aria-hidden="true" />
                <strong>{{ walkMetric.value }}</strong>
                <em>{{ walkMetric.unit }}</em>
                <small>walk</small>
              </span>
            </div>

            <div class="planner-feature-grid">
              <div class="planner-feature-item">
                <img :src="benchIcon" alt="" />
                <p>{{ facilityBreakdown.bench }} places to rest</p>
              </div>
              <div class="planner-feature-item">
                <img :src="toiletIcon" alt="" />
                <p>{{ facilityBreakdown.toilet }} public toilets nearby</p>
              </div>
              <div class="planner-feature-item">
                <img :src="slopeIcon" alt="" />
                <p>{{ slopeSummary }}</p>
              </div>
              <div class="planner-feature-item">
                <img :src="treesIcon" alt="" />
                <p>{{ shadeSummary }}</p>
              </div>
            </div>

            <div class="planner-summary-actions">
              <button class="btn btn-primary planner-see-route-btn" @click="openRouteView" :disabled="!canSeeRoute || isLoadingPlan">
                See route
              </button>
              <button class="btn planner-change-btn" @click="clearDestinationChoice" :disabled="isLoadingPlan || isLocating">
                Change destination
              </button>
            </div>
          </div>
        </article>

        <article
          v-else-if="hasSelectedType && hasSearched && !isLoadingPlan && !hasDestination && !errorMessage"
          class="planner-card planner-no-result-card"
        >
          <h3>No nearby {{ selectedTypeLabel.toLowerCase() }} found</h3>
          <p>We could not find a suitable destination near this location. Try another type or update your location.</p>
          <div class="planner-summary-actions">
            <button class="btn planner-change-btn" @click="clearDestinationChoice">Try another type</button>
            <button class="btn btn-light planner-location-btn" @click="useMyLocation" :disabled="isLocating">
              {{ isLocating ? 'Locating...' : 'Update my location' }}
            </button>
          </div>
        </article>

        <article v-else-if="hasSelectedType && hasSearched && !isLoadingPlan && !!errorMessage" class="planner-card planner-no-result-card">
          <h3>Unable to load route right now</h3>
          <p>{{ errorMessage }}</p>
          <div class="planner-summary-actions">
            <button class="btn planner-change-btn" @click="requestPlan">Try again</button>
            <button class="btn btn-light planner-location-btn" @click="useMyLocation" :disabled="isLocating">
              {{ isLocating ? 'Locating...' : 'Update my location' }}
            </button>
          </div>
        </article>
      </section>
    </section>

    <section class="planner-route-shell" v-else>
      <aside class="planner-route-panel rv-panel">
        <button class="planner-back-btn rv-back-btn" @click="isRouteView = false">← Back to search</button>

        <div class="rv-dest-header">
          <div class="rv-dest-icon-wrap">
            <img :src="selectedTypeIconUrl" alt="" />
          </div>
          <div class="rv-dest-info">
            <p class="rv-dest-type-label">{{ selectedTypeLabel }}</p>
            <h2 class="rv-dest-name">{{ result.destination?.name }}</h2>
          </div>
        </div>

        <div class="rv-stats-row">
          <div class="rv-stat-card">
            <strong>{{ walkMinutes }}</strong>
            <span>min walk</span>
          </div>
          <div class="rv-stat-card">
            <strong>{{ distanceMetric.value }}</strong>
            <span>{{ distanceMetric.unit }} away</span>
          </div>
        </div>

        <div class="rv-section">
          <h3>Along the way</h3>
          <div class="rv-fac-grid">
            <div class="rv-fac-card rv-fac-bench" v-if="facilityBreakdown.bench > 0">
              <img :src="benchIcon" alt="" />
              <div>
                <strong>{{ facilityBreakdown.bench }}</strong>
                <span>Benches</span>
              </div>
            </div>
            <div class="rv-fac-card rv-fac-toilet" v-if="facilityBreakdown.toilet > 0">
              <img :src="toiletIcon" alt="" />
              <div>
                <strong>{{ facilityBreakdown.toilet }}</strong>
                <span>Toilets</span>
              </div>
            </div>
            <div class="rv-fac-card rv-fac-fountain" v-if="facilityBreakdown.drinking_fountain > 0">
              <img :src="fountainIcon" alt="" />
              <div>
                <strong>{{ facilityBreakdown.drinking_fountain }}</strong>
                <span>Fountains</span>
              </div>
            </div>
            <div
              v-if="facilityBreakdown.bench === 0 && facilityBreakdown.toilet === 0 && facilityBreakdown.drinking_fountain === 0"
              class="rv-no-facilities"
            >
              No rest stops available along this route
            </div>
          </div>
        </div>

        <div class="rv-section rv-legend-section">
          <h3>Map legend</h3>
          <div class="rv-legend-list">
            <div class="rv-legend-row">
              <div class="rv-legend-icon rv-licon-start">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="white"><circle cx="12" cy="4" r="2.5"/><path d="M10 8.5c-1.1 0-2 .9-2 2v4h2v5h4v-5h2v-4c0-1.1-.9-2-2-2h-4z"/></svg>
              </div>
              You (start)
            </div>
            <div class="rv-legend-row">
              <div class="rv-legend-icon rv-licon-dest">
                <img :src="selectedTypeIconUrl" width="15" height="15" style="filter:invert(1)" />
              </div>
              Destination
            </div>
            <div class="rv-legend-row">
              <div class="rv-legend-icon rv-licon-bench">
                <img :src="benchIcon" width="15" height="15" style="filter:invert(1)" />
              </div>
              Bench
            </div>
            <div class="rv-legend-row">
              <div class="rv-legend-icon rv-licon-toilet">
                <img :src="toiletIcon" width="15" height="15" style="filter:invert(1)" />
              </div>
              Toilet
            </div>
            <div class="rv-legend-row">
              <div class="rv-legend-icon rv-licon-fountain">
                <img :src="fountainIcon" width="15" height="15" style="filter:invert(1)" />
              </div>
              Drinking Fountain
            </div>
            <div class="rv-legend-row">
              <span class="rv-ldot rv-ldot-route"></span>
              Walking route
            </div>
            <div class="rv-legend-row">
              <span class="rv-ldot rv-ldot-shade"></span>
              Tree canopy shade
            </div>
          </div>
          <p class="rv-legend-note">
            Tree canopy data will be supplied by the backend service. This legend item is kept for the map display.
          </p>
        </div>

      </aside>

      <section class="planner-route-map-area">
        <div class="map-chip map-chip-shade">
          <span class="map-chip-dot" aria-hidden="true"></span>
          Shade layer display
        </div>
        <div v-if="isLoadingPlan" class="planner-map-loading" role="status" aria-live="polite">
          <span class="planner-spinner" aria-hidden="true"></span>
          <p>Loading route map...</p>
        </div>
        <div ref="mapEl" class="planner-route-map"></div>
      </section>
    </section>
  </main>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, reactive, ref, watch } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import pharmacyPic from '../assets/pictures/pharmacy.png'
import groceryPic from '../assets/pictures/grocery.png'
import clinicPic from '../assets/pictures/clinic.png'
import parkPic from '../assets/pictures/park.png'
import cafePic from '../assets/pictures/cafe.png'
import pharmacyIcon from '../assets/svg/pharmacy.svg'
import groceryIcon from '../assets/svg/grocery.svg'
import clinicIcon from '../assets/svg/clinic.svg'
import parkIcon from '../assets/svg/park.svg'
import cafeIcon from '../assets/svg/break-cafe.svg'
import locationIcon from '../assets/svg/location-icon.svg'
import benchIcon from '../assets/svg/bench-icon.svg'
import toiletIcon from '../assets/svg/toilet-icon.svg'
import fountainIcon from '../assets/svg/drinking-fountain-icon.svg'
import slopeIcon from '../assets/svg/slope-icon.svg'
import treesIcon from '../assets/svg/trees-icon.svg'
import walkIcon from '../assets/svg/walk.svg'
import timeIcon from '../assets/svg/time-icon.svg'

const DEFAULT_LOCATION = { lat: -37.8136, lng: 144.9631 }
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:5000'

const destinationTypes = [
  { id: 'pharmacy', label: 'Pharmacy', icon: pharmacyIcon, image: pharmacyPic },
  { id: 'grocery', label: 'Grocery', icon: groceryIcon, image: groceryPic },
  { id: 'clinic', label: 'Clinic', icon: clinicIcon, image: clinicPic },
  { id: 'garden', label: 'Park', icon: parkIcon, image: parkPic },
  { id: 'cafe', label: 'Cafe', icon: cafeIcon, image: cafePic }
]

const selectedType = ref('')
const isLoadingPlan = ref(false)
const isLocating = ref(false)
const isRouteView = ref(false)
const hasSearched = ref(false)

const userLocation = reactive({
  lat: DEFAULT_LOCATION.lat,
  lng: DEFAULT_LOCATION.lng,
  source: 'default'
})

const result = reactive({
  destination: null,
  facilities: [],
  route: []
})

const errorMessage = ref('')
const infoMessage = ref('')
const resultAnchorEl = ref(null)
const typeSectionEl = ref(null)

const mapEl = ref(null)
let map = null
let userLayer = null
let destinationLayer = null
let facilitiesLayer = null
let routeLayer = null
let activeRequestId = 0

const hasSelectedType = computed(() => !!selectedType.value)
const hasDestination = computed(() => !!result.destination)

const selectedTypeLabel = computed(() => {
  const item = destinationTypes.find((d) => d.id === selectedType.value)
  return item ? item.label : 'Destination'
})

const locationLabel = computed(() => (userLocation.source === 'live' ? 'Current location' : 'Melbourne CBD (Default)'))

const resultImage = computed(() => {
  const match = destinationTypes.find((item) => item.id === selectedType.value)
  return match?.image || parkPic
})

const routeDistanceMeters = computed(() => {
  if (result.route.length > 1) {
    let total = 0
    for (let i = 1; i < result.route.length; i += 1) {
      const [lng1, lat1] = result.route[i - 1]
      const [lng2, lat2] = result.route[i]
      total += haversineMeters(lat1, lng1, lat2, lng2)
    }
    return Math.round(total)
  }
  return result.destination?.distanceMeters || 0
})

const distanceText = computed(() => {
  const meters = routeDistanceMeters.value
  if (!meters) return 'Distance unavailable'
  if (meters >= 1000) return `${(meters / 1000).toFixed(2)} km`
  return `${meters} m`
})

const distanceMetric = computed(() => {
  const meters = routeDistanceMeters.value
  if (!meters) return { value: '--', unit: 'm' }
  if (meters >= 1000) return { value: (meters / 1000).toFixed(2), unit: 'km' }
  return { value: `${meters}`, unit: 'm' }
})

const walkMinutes = computed(() => {
  const meters = routeDistanceMeters.value
  if (!meters) return '--'
  return Math.max(1, Math.round(meters / 78))
})

const walkMetric = computed(() => ({
  value: `${walkMinutes.value}`,
  unit: 'min'
}))

const facilityBreakdown = computed(() => {
  const output = { bench: 0, drinking_fountain: 0, toilet: 0 }
  result.facilities.forEach((item) => {
    if (output[item.type] !== undefined) output[item.type] += 1
  })
  return output
})

const slopeSummary = computed(() => {
  if (!routeDistanceMeters.value) return 'Slope profile unavailable'
  if (routeDistanceMeters.value <= 1000) return 'Mostly flat and easy'
  return 'Gentle slopes likely'
})

const shadeSummary = computed(() => {
  if (selectedType.value === 'garden') return 'Shaded for most of the way'
  if (routeDistanceMeters.value && routeDistanceMeters.value <= 900) return 'Good shade in key sections'
  return 'Some shaded stretches along the route'
})

const canSeeRoute = computed(() => !!result.destination && result.route.length > 1)

const selectedTypeIconUrl = computed(() => {
  const match = destinationTypes.find(d => d.id === selectedType.value)
  return match?.icon || parkIcon
})

const scrollTo = (el) => {
  if (!el) return
  el.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

const clearResult = () => {
  result.destination = null
  result.facilities = []
  result.route = []
}

const fetchJson = async (url, options = {}, timeoutMs = 20000) => {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeoutMs)
  try {
    const response = await fetch(url, { ...options, signal: controller.signal })
    const payload = await response.json().catch(() => ({}))
    if (!response.ok) throw new Error(payload.error || `Request failed (${response.status})`)
    return payload
  } finally {
    clearTimeout(timer)
  }
}

const requestPlan = async () => {
  if (!selectedType.value) return

  const requestId = ++activeRequestId
  const requestType = selectedType.value
  const requestLat = Number.isFinite(Number(userLocation.lat)) ? Number(userLocation.lat) : DEFAULT_LOCATION.lat
  const requestLng = Number.isFinite(Number(userLocation.lng)) ? Number(userLocation.lng) : DEFAULT_LOCATION.lng
  const maxAttempts = userLocation.source === 'default' ? 2 : 1

  hasSearched.value = true
  isLoadingPlan.value = true
  errorMessage.value = ''
  infoMessage.value = ''
  clearResult()

  try {
    let payload = null
    for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
      payload = await fetchJson(`${API_BASE_URL}/api/route/plan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: requestType,
          userLat: requestLat,
          userLng: requestLng
        })
      })
      // retry if destination found but route is empty (e.g. ORS cold-start failure)
      const routeReady = payload?.destination && (payload.route?.length ?? 0) > 1
      if (routeReady || !payload?.destination || attempt === maxAttempts) break
      await new Promise((resolve) => setTimeout(resolve, 800))
    }

    if (requestId !== activeRequestId) return

    result.destination = payload?.destination || null
    result.facilities = payload?.facilities || []
    result.route = payload?.route || []
    infoMessage.value = payload?.message || 'Route recommendation is ready.'

    if (isRouteView.value) drawRouteMap()
  } catch (error) {
    if (requestId !== activeRequestId) return
    clearResult()
    errorMessage.value = error instanceof Error
      ? `${error.message}. Make sure backend is running at ${API_BASE_URL}.`
      : 'Unable to load route data.'
  } finally {
    if (requestId !== activeRequestId) return
    isLoadingPlan.value = false
  }
}

const useMyLocation = async () => {
  if (!navigator.geolocation) {
    errorMessage.value = 'Geolocation is unavailable. Using Melbourne CBD default location.'
    return
  }

  isLocating.value = true
  try {
    const position = await new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 300000
      })
    })
    userLocation.lat = position.coords.latitude
    userLocation.lng = position.coords.longitude
    userLocation.source = 'live'
  } catch {
    userLocation.lat = DEFAULT_LOCATION.lat
    userLocation.lng = DEFAULT_LOCATION.lng
    userLocation.source = 'default'
    errorMessage.value = 'Could not detect your location. Using Melbourne CBD default.'
  } finally {
    isLocating.value = false
  }

  if (hasSelectedType.value) requestPlan()
}

const clearDestinationChoice = () => {
  activeRequestId += 1
  selectedType.value = ''
  errorMessage.value = ''
  infoMessage.value = ''
  hasSearched.value = false
  isRouteView.value = false
  clearResult()
  nextTick(() => scrollTo(typeSectionEl.value))
}

const haversineMeters = (lat1, lng1, lat2, lng2) => {
  const toRad = (value) => (value * Math.PI) / 180
  const earth = 6371000
  const dLat = toRad(lat2 - lat1)
  const dLng = toRad(lng2 - lng1)
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLng / 2) ** 2
  return earth * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
}

const calcBearing = ([lat1, lng1], [lat2, lng2]) => {
  const toRad = v => v * Math.PI / 180
  const dLng = toRad(lng2 - lng1)
  const y = Math.sin(dLng) * Math.cos(toRad(lat2))
  const x = Math.cos(toRad(lat1)) * Math.sin(toRad(lat2)) -
            Math.sin(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.cos(dLng)
  return (Math.atan2(y, x) * 180 / Math.PI + 360) % 360
}

const ensureMap = () => {
  if (map || !mapEl.value) return
  map = L.map(mapEl.value, { zoomControl: false }).setView([userLocation.lat, userLocation.lng], 15)

  // CartoDB Positron – clean minimal basemap
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 20
  }).addTo(map)

  L.control.zoom({ position: 'bottomright' }).addTo(map)

  userLayer = L.layerGroup().addTo(map)
  destinationLayer = L.layerGroup().addTo(map)
  facilitiesLayer = L.layerGroup().addTo(map)
  routeLayer = L.layerGroup().addTo(map)
}

const makePinIcon = (html, size, anchor) =>
  L.divIcon({ html, className: '', iconSize: size, iconAnchor: anchor })

const drawRouteMap = () => {
  if (!map) return

  userLayer.clearLayers()
  destinationLayer.clearLayers()
  facilitiesLayer.clearLayers()
  routeLayer.clearLayers()

  const bounds = []

  // ── Route: solid base + animated dashes + direction arrows ─────────
  if (result.route.length > 1) {
    const line = result.route.map(([lng, lat]) => [lat, lng])

    // Solid semi-transparent base
    L.polyline(line, {
      color: '#1b5e20', weight: 7, opacity: 0.22,
      lineCap: 'round', lineJoin: 'round'
    }).addTo(routeLayer)

    // Animated dashed overlay
    const animLine = L.polyline(line, {
      color: '#2e7d32', weight: 5, opacity: 0.95,
      dashArray: '18 13', lineCap: 'round', lineJoin: 'round'
    }).addTo(routeLayer)
    setTimeout(() => {
      const el = animLine.getElement()
      if (el) el.classList.add('rv-route-animated')
    }, 80)

    bounds.push(...line)
  }

  // ── Start marker ─────────────────────────────────────
  const startHtml =
    `<div class="rv-pin-start">` +
    `<svg width="16" height="16" viewBox="0 0 24 24" fill="white">` +
    `<circle cx="12" cy="4" r="2.5"/>` +
    `<path d="M10 8.5c-1.1 0-2 .9-2 2v4h2v5h4v-5h2v-4c0-1.1-.9-2-2-2h-4z"/>` +
    `</svg></div>` +
    `<div class="rv-pin-label rv-pin-label-start">You</div>`
  L.marker([userLocation.lat, userLocation.lng], {
    icon: makePinIcon(startHtml, [44, 54], [22, 48])
  }).addTo(userLayer)
  bounds.push([userLocation.lat, userLocation.lng])

  // ── Destination marker ─────────────────────────────────
  if (result.destination?.lat != null && result.destination?.lng != null) {
    const destHtml =
      `<div class="rv-pin-dest">` +
      `<img src="${selectedTypeIconUrl.value}" width="22" height="22" style="filter:invert(1)"/>` +
      `</div>` +
      `<div class="rv-pin-label rv-pin-label-dest">${selectedTypeLabel.value}</div>`
    L.marker([result.destination.lat, result.destination.lng], {
      icon: makePinIcon(destHtml, [56, 62], [28, 56])
    }).addTo(destinationLayer)
    bounds.push([result.destination.lat, result.destination.lng])
  }

  // ── Facility markers ──────────────────────────────────
  result.facilities.forEach((item) => {
    if (item.lat == null || item.lng == null) return
    let html = ''
    if (item.type === 'bench') {
      html =
        `<div class="rv-pin-fac rv-pin-bench">` +
        `<img src="${benchIcon}" width="14" height="14" style="filter:invert(1)"/></div>`
    } else if (item.type === 'toilet') {
      html =
        `<div class="rv-pin-fac rv-pin-toilet">` +
        `<img src="${toiletIcon}" width="14" height="14" style="filter:invert(1)"/></div>`
    } else if (item.type === 'drinking_fountain') {
      html =
        `<div class="rv-pin-fac rv-pin-fountain">` +
        `<img src="${fountainIcon}" width="14" height="14" style="filter:invert(1)"/></div>`
    }
    if (html) {
      L.marker([item.lat, item.lng], {
        icon: makePinIcon(html, [28, 28], [14, 14])
      }).bindTooltip(item.name, { direction: 'top', offset: [0, -14] })
        .addTo(facilitiesLayer)
      bounds.push([item.lat, item.lng])
    }
  })

  if (bounds.length) map.fitBounds(bounds, { padding: [48, 48] })
  requestAnimationFrame(() => map?.invalidateSize())
}

const openRouteView = async () => {
  if (!canSeeRoute.value) return
  isRouteView.value = true
  await nextTick()
  ensureMap()
  drawRouteMap()
  // double-rAF: wait for browser layout to complete before fixing size
  requestAnimationFrame(() => requestAnimationFrame(() => map?.invalidateSize()))
}

watch(selectedType, async () => {
  if (!selectedType.value) {
    activeRequestId += 1
    clearResult()
    errorMessage.value = ''
    infoMessage.value = ''
    hasSearched.value = false
    return
  }
  requestPlan()
  await nextTick()
  scrollTo(resultAnchorEl.value)
})

watch(
  () => isRouteView.value,
  (visible) => {
    if (!visible) {
      // DOM element will be destroyed by v-else — must destroy map too
      map?.remove()
      map = null
      userLayer = null
      destinationLayer = null
      facilitiesLayer = null
      routeLayer = null
    }
  }
)

onBeforeUnmount(() => {
  map?.remove()
  map = null
})
</script>
