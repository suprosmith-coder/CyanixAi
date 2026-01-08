const CACHE_NAME = 'cyanix-ai-v1.0';

// Files to cache
const urlsToCache = [
  '/CyanixAi/',
  '/CyanixAi/index.html',
  '/CyanixAi/manifest.json',
  '/CyanixAi/icons/icon-192x192.png'
];

// Install Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
      .then(() => self.skipWaiting())
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});