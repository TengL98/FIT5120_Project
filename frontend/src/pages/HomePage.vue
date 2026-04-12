<template>
  <main>
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="shell hero-content">
        <h1 class="hero-title">
          <span class="hero-title-main">Walk Safely.</span>
          <span class="hero-title-accent">Stay Independent.</span>
        </h1>
        <p class="hero-copy">
          GreenPath helps older adults choose comfortable walking routes with shade, gentler paths,
          and nearby places to rest.
        </p>

        <div class="hero-actions">
          <a class="btn btn-light" href="#/planner">Plan My Walk</a>
          <a class="btn btn-outline-light" href="#/learn-more">Learn More</a>
        </div>

        <div class="hero-stats" aria-label="Key figures">
          <article class="stat-card">
            <p class="stat-value">57%</p>
            <p class="stat-label">of older adults are not active enough</p>
          </article>
          <article class="stat-card">
            <p class="stat-value">19%</p>
            <p class="stat-label">lower heart disease risk with regular walking</p>
          </article>
          <article class="stat-card">
            <p class="stat-value">15 min</p>
            <p class="stat-label">comfortable walking range for nearby needs</p>
          </article>
        </div>
      </div>
      <div class="hero-scroll-hint" aria-hidden="true">
        <svg viewBox="0 0 28 36" role="presentation">
          <path d="M3 4L14 15L25 4" stroke="#f6bf3f" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M3 14L14 25L25 14" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M3 24L14 35L25 24" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <span>Scroll down for more</span>
      </div>
    </section>

    <section class="section challenge-brief">
      <div class="shell">
        <div class="section-head challenge-intro">
          <h2>What gets in the way of walking confidence?</h2>
          <p>
            Destinations may be close, but daily walking can still feel uncertain. These common barriers
            often reduce confidence to go out.
          </p>
        </div>

        <div class="challenge-grid">
          <article class="challenge-card">
            <img
              class="challenge-media"
              src="https://images.pexels.com/photos/11299600/pexels-photo-11299600.jpeg?auto=compress&cs=tinysrgb&w=900&h=520&dpr=1"
              alt="Older adult walking in strong sunlight"
              loading="lazy"
            />
            <div class="challenge-body">
              <h3>Heat and shade</h3>
              <p>Long sunny stretches can feel exhausting.</p>
            </div>
          </article>
          <article class="challenge-card">
            <img
              class="challenge-media"
              src="https://images.pexels.com/photos/13834915/pexels-photo-13834915.jpeg?auto=compress&cs=tinysrgb&w=900&h=520&dpr=1"
              alt="Older adult looking for a bench to rest"
              loading="lazy"
            />
            <div class="challenge-body">
              <h3>Rest options</h3>
              <p>Without clear rest stops, short trips feel hard.</p>
            </div>
          </article>
          <article class="challenge-card">
            <img
              class="challenge-media"
              src="https://images.pexels.com/photos/17491824/pexels-photo-17491824.jpeg?auto=compress&cs=tinysrgb&w=900&h=520&dpr=1"
              alt="Road and footpath conditions"
              loading="lazy"
            />
            <div class="challenge-body">
              <h3>Road conditions</h3>
              <p>Steep slopes and uneven paths reduce confidence.</p>
            </div>
          </article>
          <article class="challenge-card">
            <img
              class="challenge-media"
              src="https://images.pexels.com/photos/24778030/pexels-photo-24778030.jpeg?auto=compress&cs=tinysrgb&w=900&h=520&dpr=1"
              alt="Pedestrians on a street providing passive support"
              loading="lazy"
            />
            <div class="challenge-body">
              <h3>Passive support</h3>
              <p>Streets with moderate foot traffic offer quiet, nearby help.</p>
            </div>
          </article>
        </div>

        <a class="btn btn-primary" href="#/learn-more">Learn More About These Barriers</a>
      </div>
    </section>

    <section class="section purpose-section">
      <div class="shell">
        <div class="purpose-panel">
          <div class="section-head">
            <p class="eyebrow dark">Our Purpose</p>
            <h2>Give every older adult a walk they can trust.</h2>
            <p>
              We focus on what people care about most: comfort, clarity, and confidence from start to finish.
            </p>
          </div>

          <div class="purpose-points">
            <article>
              <div class="icon-box">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C9 4.6 8.5 8.8 10.2 11C11.5 9.7 12.9 8 15 6.4C14.2 4.7 13 2.8 12 2Z"/><path d="M12 22V11"/></svg>
              </div>
              <h3>Comfortable route suggestions</h3>
              <p>Prefer routes with shade and easier walking conditions.</p>
            </article>
            <article>
              <div class="icon-box">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 11H19V16H5Z"/><path d="M7 11V8C7 6.3 8.3 5 10 5H14C15.7 5 17 6.3 17 8V11"/></svg>
              </div>
              <h3>Rest stops along the way</h3>
              <p>Show nearby benches and toilets before people begin walking.</p>
            </article>
            <article>
              <div class="icon-box">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2L4 6V12C4 17.3 7.8 21.8 12 23C16.2 21.8 20 17.3 20 12V6Z"/><path d="M9 12L11.5 14.5L15.5 10.5"/></svg>
              </div>
              <h3>Clear support options</h3>
              <p>Highlight nearby pharmacies and clinics if help is needed.</p>
            </article>
          </div>
        </div>
      </div>
    </section>

    <section class="section steps-section">
      <div class="shell">
        <div class="section-head">
          <p class="eyebrow dark">How It Works</p>
          <h2>From destination to confidence in 5 steps</h2>
        </div>

        <div class="steps-list">
          <article class="step-item">
            <span>Step 1</span>
            <h3>Choose where you want to go</h3>
            <p>Select a daily destination like a pharmacy, park, cafe, or library.</p>
          </article>
          <article class="step-item">
            <span>Step 2</span>
            <h3>Get the best route within 15 minutes</h3>
            <p>GreenPath suggests a route that balances shade, slope, and nearby rest facilities.</p>
          </article>
          <article class="step-item">
            <span>Step 3</span>
            <h3>Follow a more reassuring street path</h3>
            <p>Routes prioritize places with moderate activity so help is closer if needed.</p>
          </article>
          <article class="step-item">
            <span>Step 4</span>
            <h3>Start simple navigation</h3>
            <p>Use turn-by-turn support and see rest points ahead before you arrive.</p>
          </article>
          <article class="step-item">
            <span>Step 5</span>
            <h3>Build confidence and enjoy healthy living</h3>
            <p>Each safe, comfortable walk supports independence and wellbeing over time.</p>
          </article>
        </div>

        <a class="btn btn-primary" href="#/planner">Try the Route Planner</a>
      </div>
    </section>
  </main>
</template>
