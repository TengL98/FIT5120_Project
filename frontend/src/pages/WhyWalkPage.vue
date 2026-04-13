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
    <section class="section bg-white text-center">
      <div class="container">
        <h2 class="section-title">The Current Challenge</h2>
        <p class="section-desc">Among adults aged 65 and older in Australia:</p>
        
        <div class="stat-banner">
          <div class="stat-number">57%</div>
          <div class="stat-text">Do not meet physical activity guidelines.</div>
        </div>
        
        <p class="stat-note">
          Without regular movement, our bodies stiffness increases, and our social connections can fade. But every small step counts toward reversing this.
        </p>
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
    <section class="section bg-white">
      <div class="container">
        <h2 class="section-title text-center">Benefits Backed by Data</h2>
        
        <div class="benefits-grid">
          <div class="benefit-card">
            <div class="b-icon">❤️</div>
            <h4 class="b-title">19% Lower Heart Risk</h4>
            <p class="b-text">
              Walking about 30 minutes a day, 5 days a week lowers the risk of coronary heart disease. No gym, no heavy equipment, just walking.
            </p>
          </div>
          <div class="benefit-card">
            <div class="b-icon">😌</div>
            <h4 class="b-title">Significantly Less Anxiety</h4>
            <p class="b-text">
              Regular physical activity significantly reduces anxiety and depression in older adults. Sunlight and fresh air naturally lift your mood.
            </p>
          </div>
          <div class="benefit-card">
            <div class="b-icon">👥</div>
            <h4 class="b-title">Stronger Connections</h4>
            <p class="b-text">
              A wave to a neighbour, sitting in the park, or a cup of tea at a café — these small moments are among the most effective ways to combat loneliness.
            </p>
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
  max-width: 900px;
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

/* Stat Box */
.stat-banner {
  background-color: var(--primary-light);
  border-radius: 16px;
  padding: 40px 24px;
  margin: 0 auto 24px;
  max-width: 500px;
  border: 2px solid #cce0cc;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.stat-number {
  font-size: 4.5rem;
  font-weight: 900;
  color: var(--primary-color);
  line-height: 1;
  margin-bottom: 12px;
}
.stat-text {
  font-size: 1.35rem;
  font-weight: 600;
}
.stat-note {
  max-width: 600px;
  margin: 0 auto;
  font-size: 1.1rem;
  color: var(--text-muted);
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

/* Benefits Grid */
.benefits-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  margin-top: 40px;
}
@media (min-width: 768px) {
  .benefits-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
.benefit-card {
  background: var(--bg-soft);
  padding: 32px 24px;
  border-radius: 12px;
  text-align: center;
  border: 1px solid #e5e5e5;
  transition: transform 0.2s ease;
}
.benefit-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}
.b-icon {
  font-size: 3.5rem;
  margin-bottom: 16px;
}
.b-title {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--text-main);
}
.b-text {
  font-size: 1.1rem;
  color: var(--text-muted);
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
  left: -110px; /* Offset to the left of the border */
  top: 0;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--primary-color);
  width: 80px;
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
  background-color: var(--primary-color);
  color: white;
  padding: 80px 24px;
}
.cta-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 24px;
  color: white;
}
.cta-desc {
  font-size: 1.35rem;
  opacity: 0.9;
  max-width: 700px;
  margin: 0 auto 40px;
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