<script setup>
import { ref, onMounted } from 'vue';

const showAnimation = ref(false);

onMounted(() => {
  setTimeout(() => {
    showAnimation.value = true;
  }, 100);
});
</script>

<template>
  <main class="why-walk-page">
    <!-- Hero Section -->
    <header class="hero-header bg-soft">
      <div class="container hero-container">
        <h1 class="hero-title">Why Getting Outside Matters</h1>
        <p class="hero-subtitle">
          Research shows that just 30 minutes of walking a day can bring remarkable benefits to your body and mind. It's never too late to start reaping the rewards.
        </p>
      </div>
    </header>

    <!-- Stat Section -->
    <section class="section stat-section bg-soft text-center">
      <div class="container container-tight">
        <div class="stat-header">
          <span class="stat-eyebrow">PHYSICAL ACTIVITY AMONG OLDER AUSTRALIANS</span>
        </div>
        <h2 class="stat-title">Among every 10 adults aged 65+...</h2>
        
        <div class="stat-visual-container" :class="{ 'is-visible': showAnimation }">
          <!-- Figures representation -->
          <div class="stat-figures">
            <div class="figures-row">
              <div v-for="i in 10" :key="i" class="figure-wrapper" :style="{ transitionDelay: `${i * 100}ms` }">
                <svg class="figure-icon" :class="i <= 6 ? 'inactive' : 'active'" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <!-- Solid Human Figure -->
                  <circle cx="12" cy="4.5" r="2.5" />
                  <path d="M15 8H9c-1.24 0-2 .8-2 2v6h2.5v7h5v-7H17v-6c0-1.2-.76-2-2-2z" />
                </svg>
              </div>
            </div>
            <div class="figures-legend">
              <span class="legend-item"><span class="dot inactive-dot"></span> Insufficiently active</span>
              <span class="legend-item"><span class="dot active-dot"></span> Sufficiently active</span>
            </div>
            <div class="stat-source text-left">
              Source: ABS 2022 National Health Survey · AIHW analysis
            </div>
          </div>
          
          <!-- Percentage numbers -->
          <div class="stat-numbers-stack">
            <div class="stat-block fade-in-up" style="transition-delay: 1100ms;">
              <div class="stat-huge inactive-text">57%</div>
              <div class="stat-desc">do not meet physical activity guidelines</div>
            </div>
            <div class="stat-block fade-in-up mt-4" style="transition-delay: 1300ms;">
              <div class="stat-huge active-text">39%</div>
              <div class="stat-desc">did zero physical activity in the past week</div>
              <div class="stat-source stat-source-sm">Source: ABS 2022 NHS / AIHW</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contrast Section -->
    <section class="section bg-soft">
      <div class="container">
        <h2 class="section-title text-center">Two Choices, Two Outcomes</h2>
        <p class="section-desc text-center">Regular walking vs. staying indoors leads to very different physical and mental health outcomes over time.</p>
        
        <div class="comparison-grid">
          <div class="card card-good">
            <h3 class="card-title"><span class="icon">🚶</span> Regular Walking</h3>
            <ul class="checklist check-good">
              <li>Stronger heart and lower blood pressure</li>
              <li>Better mood, less anxiety and worry</li>
              <li>Social connection and less loneliness</li>
              <li>Deeper, more restful sleep</li>
              <li>More flexible, joints stay mobile</li>
            </ul>
          </div>
          
          <div class="card card-bad">
            <h3 class="card-title"><span class="icon">🏠</span> Staying Indoors</h3>
            <ul class="checklist check-bad">
              <li>Increased risk of heart disease</li>
              <li>Higher anxiety and low mood</li>
              <li>Social isolation and loneliness</li>
              <li>Poorer sleep quality</li>
              <li>Reduced mobility and stiffness</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Research Benefits -->
    <section class="section bg-white benefits-section-wrapper">
      <div class="container">
        <h2 class="section-title text-center">Every Time You Step Outside</h2>
        <p class="section-desc text-center">Simple walks bring real changes to your health and happiness</p>
        
        <div class="benefits-mosaic">

          <!-- Hero card: A Healthier Heart — occupies full left column -->
          <div class="mosaic-card mc-heart">
            <div class="mi-bg" style="background-image: url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&q=80');"></div>
            <div class="mi-quote-badge">
              <span class="mi-qmark">"</span>
              <span class="mi-qtext">Walking is the best medicine</span>
            </div>
            <div class="mi-body">
              <h4 class="b-title-new">A Healthier Heart</h4>
              <p class="b-text-new">Walking 30 minutes a day, five days a week, keeps your heart strong. No gym membership needed — just your own two feet.</p>
            </div>
          </div>

          <!-- Right column -->
          <div class="mc-right-col">

            <!-- Mood card -->
            <div class="mosaic-card mc-mood">
              <div class="mi-bg" style="background-image: url('https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?w=800&q=80');"></div>
              <div class="mi-body">
                <h4 class="b-title-new">A Lighter Mood</h4>
                <p class="b-text-new">Sunshine and fresh air work wonders. Worries feel smaller, and your spirits naturally lift when you're outdoors.</p>
              </div>
            </div>

            <!-- Bottom row: social card -->
            <div class="mc-bottom-row">
              <div class="mosaic-card mc-social">
                <div class="mi-bg" style="background-image: url('https://images.unsplash.com/photo-1491438590914-bc09fcaaf77a?w=800&q=80');"></div>
                <div class="mi-body">
                  <h4 class="b-title-new">More Company, Less Loneliness</h4>
                  <p class="b-text-new">A friendly wave to a neighbour, or coffee with a friend — these small moments warm the heart.</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- Timeline Outline -->
    <section class="section bg-soft timeline-section">
      <div class="container">
        <h2 class="section-title text-center">30 Minutes, Step by Step</h2>
        <p class="section-desc text-center">Here is what happens to your body when you go for a simple 30-minute walk.</p>
        
        <div class="timeline">
          <div class="time-item">
            <div class="time-marker">5 mins</div>
            <div class="time-content">
              <strong>Heart rate rises mildly.</strong> Blood flows to working muscles, your body warms up, and you start to feel more alert.
            </div>
          </div>
          <div class="time-item">
            <div class="time-marker">15 mins</div>
            <div class="time-content">
              <strong>You hit a steady rhythm.</strong> Oxygen delivery improves, stiff joints loosen up, and your mind feels clearer and calmer.
            </div>
          </div>
          <div class="time-item">
            <div class="time-marker">20 mins</div>
            <div class="time-content">
              <strong>Social moments happen.</strong> You might wave to a neighbour or pass a friendly face. These brief interactions reduce isolation.
            </div>
          </div>
          <div class="time-item">
            <div class="time-marker">30 mins</div>
            <div class="time-content">
              <strong>Heart-healthy workout completed.</strong> You've successfully finished a bout of exercise. Tonight's sleep will be deeper and more restful.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="section hero-cta text-center">
      <div class="container">
        <h2 class="cta-title">Ready to Take the First Step?</h2>
        <p class="cta-desc">
          We can help you find shaded paths, available rest stops, and emergency facilities — everything to walk with confidence.
        </p>
        <a href="#/planner" class="btn btn-primary btn-large">Find Routes Near Me →</a>
      </div>
    </section>
  </main>
</template>

<style scoped>
/* Page Specific Variables */
.why-walk-page {
  --primary-color: #2b5b2c;
  --primary-light: #e6f0e6;
  --text-main: #1a1a1a;
  --text-muted: #4a4a4a;
  --bg-soft: #faf8f5;
  --bg-white: #ffffff;
  --danger-color: #d32f2f;
  
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: var(--text-main);
  line-height: 1.6;
  font-size: 1.125rem; /* Larger base font for older adults */
}

/* Typography and Spacing */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}
.section {
  padding: 60px 0;
}
.bg-soft {
  background-color: var(--bg-soft);
}
.bg-white {
  background-color: var(--bg-white);
}
.text-center {
  text-align: center;
}
.section-title {
  font-size: 2.25rem;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--primary-color);
  line-height: 1.2;
}
.section-desc {
  font-size: 1.25rem;
  color: var(--text-muted);
  margin-bottom: 40px;
  max-width: 700px;
  margin-inline: auto;
}

/* Hero Section */
.hero-header {
  padding: 80px 0;
  text-align: center;
  border-bottom: 4px solid var(--primary-light);
}
.hero-container {
  padding-top: 20px;
}
.hero-title {
  font-size: 3rem;
  font-weight: 800;
  color: var(--primary-color);
  margin-bottom: 24px;
  line-height: 1.1;
}
.hero-subtitle {
  font-size: 1.35rem;
  max-width: 760px;
  margin: 0 auto;
  color: var(--text-muted);
}

/* Visualization Styles */
.stat-section {
  background-color: #faf8f5;
  padding: 80px 0;
}
.stat-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 48px;
}
.stat-header::before,
.stat-header::after {
  content: '';
  flex: 1;
  height: 1px;
  background-color: #d1d8d1;
}
.stat-eyebrow {
  font-size: 0.9rem;
  font-weight: 700;
  color: #2b5b3a;
  letter-spacing: 1px;
  text-transform: uppercase;
}
.stat-title {
  font-family: 'Georgia', serif;
  font-variant-numeric: lining-nums; /* Ensures numbers like 6 and 5 align on the same baseline */
  font-size: clamp(2rem, 4.5vw, 3.5rem);
  white-space: nowrap;
  font-weight: 700;
  color: #1a2f1c;
  margin-bottom: 60px;
  text-align: left;
}
.stat-visual-container {
  display: flex;
  flex-direction: column;
  gap: 40px;
  align-items: center;
  justify-content: space-between;
}
@media (min-width: 900px) {
  .stat-visual-container {
    flex-direction: row;
    align-items: center; /* Changed from flex-start to vertically center */
    gap: 60px;
  }
}
.stat-figures {
  flex: 1; /* Changed from 1.2 to give equal or less space compared to text */
  text-align: center;
}
.figures-row {
  display: flex;
  justify-content: center;
  gap: 0px; /* Reduced gap to bring figures closer */
  margin-bottom: 32px;
}
.figure-wrapper {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.is-visible .figure-wrapper {
  opacity: 1;
  transform: translateY(0);
}
.figure-icon {
  width: 64px; /* Scaled up from 44px */
  height: 96px; /* Scaled up from 66px */
  fill: currentColor;
}
.figure-icon.inactive {
  color: #d04a32;
}
.figure-icon.active {
  color: #8da495; /* Lighter green for sufficiently active people */
}
.figures-legend {
  display: flex;
  justify-content: center;
  gap: 24px;
  margin-bottom: 12px;
  font-size: 1rem;
  color: #666;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
}
.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
}
.inactive-dot {
  background-color: #d04a32;
}
.active-dot {
  background-color: #556c5c;
}
.stat-source {
  font-size: 0.85rem;
  color: #888;
  text-align: center;
}
.stat-numbers-stack {
  flex: 1.1; /* Gives more room to the descriptions */
  display: flex;
  flex-direction: column;
  gap: 40px;
  text-align: left;
}
.stat-block {
  display: flex;
  flex-direction: column;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.is-visible .stat-block {
  opacity: 1;
  transform: translateY(0);
}
.stat-huge {
  font-family: 'Georgia', serif;
  font-size: 6rem;
  font-weight: 700;
  line-height: 0.9;
  letter-spacing: -2px;
  margin-bottom: 12px;
}
.inactive-text {
  color: #d04a32;
}
.active-text {
  color: #3e6b4e;
}
.stat-desc {
  font-size: 1.6rem; /* Increased significantly for readability */
  line-height: 1.3;
  color: #333;
}
.stat-source-sm {
  margin-top: 16px;
  font-size: 0.8rem;
  text-align: left;
}

/* Comparison Grid */
.comparison-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
}
@media (min-width: 768px) {
  .comparison-grid {
    grid-template-columns: 1fr 1fr;
  }
}
.card {
  background: white;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  border: 2px solid transparent;
}
.card-good {
  border-color: var(--primary-color);
}
.card-bad {
  border-color: #f5c6c6;
  background-color: #fdfafb;
}
.card-title {
  font-size: 1.75rem;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.card-good .card-title {
  color: var(--primary-color);
}
.card-bad .card-title {
  color: var(--danger-color);
}
.icon {
  font-size: 2.5rem;
}
.checklist {
  list-style: none;
  padding: 0;
  margin: 0;
}
.checklist li {
  font-size: 1.25rem;
  margin-bottom: 16px;
  padding-left: 36px;
  position: relative;
}
.check-good li::before {
  content: '✓';
  position: absolute;
  left: 0;
  top: 0;
  color: white;
  background-color: var(--primary-color);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  text-align: center;
  line-height: 24px;
  font-size: 14px;
  font-weight: bold;
}
.check-bad li::before {
  content: '✕';
  position: absolute;
  left: 0;
  top: 0;
  color: white;
  background-color: var(--danger-color);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  text-align: center;
  line-height: 24px;
  font-size: 14px;
  font-weight: bold;
}

/* ── Benefits Mosaic Layout ───────────────────────────── */
.benefits-mosaic {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 20px;
  margin-top: 56px;
  align-items: stretch;
}

/* Right column stacks mood + bottom row */
.mc-right-col {
  display: grid;
  grid-template-rows: 1fr 1fr;
  gap: 20px;
}

/* Bottom row inside right col */
.mc-bottom-row {
  display: block;
  min-height: 0;
}

/* ── Base card ─────────────────────────────────────────── */
.mosaic-card {
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0,0,0,0.13);
  transition: transform 0.35s ease, box-shadow 0.35s ease;
}
.mosaic-card:hover {
  transform: translateY(-7px);
  box-shadow: 0 18px 52px rgba(0,0,0,0.22);
}

/* Individual cards — irregular radii for visual tension */
.mc-heart {
  min-height: 580px;
  border-radius: 28px 28px 72px 28px;
}
.mc-mood {
  height: 100%;
  min-height: 0;
  border-radius: 28px;
}
.mc-social {
  width: 100%;
  height: 100%;
  min-height: 0;
  border-radius: 20px 52px 20px 20px;
}

/* Photo background layer */
.mi-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  filter: brightness(0.65);
  transition: transform 0.4s ease, filter 0.3s ease;
}
.mosaic-card:hover .mi-bg {
  transform: scale(1.06);
  filter: brightness(0.55);
}

/* Text body pinned to card bottom */
.mi-body {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 2;
  padding: 28px 32px;
  background: linear-gradient(to top, rgba(0,0,0,0.88) 0%, transparent 100%);
  color: white;
}

.b-title-new {
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 12px;
  color: white;
  text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
}
.b-text-new {
  font-size: 1.2rem;
  line-height: 1.65;
  color: rgba(255,255,255,0.93);
  text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
}

/* Keep right-column card typography consistent and elder-friendly */
.mc-mood .b-title-new,
.mc-social .b-title-new {
  font-size: 1.85rem;
}

.mc-mood .b-text-new,
.mc-social .b-text-new {
  font-size: 1.22rem;
  line-height: 1.68;
}

/* Glass quote badge (top-right of heart card) */
.mi-quote-badge {
  position: absolute;
  top: 24px;
  right: 28px;
  z-index: 3;
  max-width: 175px;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.22);
  border-radius: 16px;
  padding: 14px 18px;
  color: white;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.mi-qmark {
  font-family: Georgia, serif;
  font-size: 2.4rem;
  line-height: 1;
  color: rgba(255,255,255,0.5);
}
.mi-qtext {
  font-size: 0.9rem;
  font-style: italic;
  line-height: 1.4;
}

/* ── Responsive ─────────────────────────────────────── */
@media (max-width: 900px) {
  .benefits-mosaic {
    grid-template-columns: 1fr;
  }
  .mc-right-col {
    display: flex;
    flex-direction: column;
  }
  .mc-heart {
    min-height: 360px;
    border-radius: 24px;
  }
  .mc-bottom-row {
    min-height: 200px;
  }
}
@media (max-width: 560px) {
  .mc-bottom-row {
    min-height: 180px;
  }
}

/* Timeline */
.timeline {
  max-width: 600px;
  margin: 40px auto 0;
  border-left: 4px solid var(--primary-color);
  padding-left: 32px;
  position: relative;
}
.time-item {
  position: relative;
  margin-bottom: 40px;
}
.time-item:last-child {
  margin-bottom: 0;
}
.time-marker {
  position: absolute;
  left: -135px; /* Offset to the left of the border further to prevent overlap */
  top: 0;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--primary-color);
  width: 90px;
  text-align: right;
}
/* For smaller screens where left offset doesn't fit well */
@media (max-width: 640px) {
  .timeline {
    border-left: 4px solid var(--primary-color);
    padding-left: 20px;
    margin-left: 10px;
  }
  .time-marker {
    position: static;
    display: inline-block;
    background-color: var(--primary-light);
    padding: 4px 12px;
    border-radius: 16px;
    margin-bottom: 8px;
    text-align: center;
    width: auto;
  }
}
.time-item::before {
  content: '';
  position: absolute;
  left: -42px;
  top: 4px;
  width: 16px;
  height: 16px;
  background-color: var(--primary-color);
  border-radius: 50%;
  border: 4px solid var(--bg-soft);
}
@media (max-width: 640px) {
  .time-item::before {
    left: -30px;
    top: 6px;
  }
}
.time-content {
  background: white;
  padding: 20px 24px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  font-size: 1.15rem;
}
.time-content strong {
  display: block;
  font-size: 1.25rem;
  margin-bottom: 6px;
  color: var(--text-main);
}

/* CTA */
.hero-cta {
  position: relative;
  overflow: hidden;
  background-image:
    linear-gradient(120deg, rgba(20, 56, 29, 0.82), rgba(32, 87, 48, 0.68)),
    url('https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=2200&q=80');
  background-size: cover;
  background-position: center 40%;
  background-repeat: no-repeat;
  color: white;
  padding: 80px 24px;
}
.hero-cta .container {
  position: relative;
  z-index: 1;
}
.cta-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 24px;
  color: white;
  text-shadow: 1px 2px 8px rgba(0,0,0,0.35);
}
.cta-desc {
  font-size: 1.35rem;
  opacity: 0.96;
  max-width: 700px;
  margin: 0 auto 40px;
  text-shadow: 1px 2px 6px rgba(0,0,0,0.28);
}
.btn-large {
  display: inline-block;
  background-color: white;
  color: var(--primary-color);
  font-size: 1.35rem;
  font-weight: 700;
  padding: 16px 32px;
  border-radius: 30px;
  text-decoration: none;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.btn-large:hover {
  background-color: #f1f1f1;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.2);
}
</style>