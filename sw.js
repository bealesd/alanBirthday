const cacheName = `alansBirthday`;
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(cacheName).then(cache => {
      return cache.addAll([
        `/`,
        `./index.html`,
        `./style.css`,
        `./bdayMeal.js`,
        `./alan192.png`,
        `./alan144.png`,
        `./alan96.png`
      ])
          .then(() => 
            self.skipWaiting());
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(cacheName)
      .then(cache => 
        cache.match(event.request, {ignoreSearch: true}))
      .then(response => {
        return response || fetch(event.request);
    })
  );
});