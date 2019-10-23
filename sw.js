const cacheName = `alansBirthday`;
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(cacheName).then(cache => {
      return cache.addAll([
        `./`,
        `./style.css`,
        `./bdayMeal.js`,
      ])
          .then(() => self.skipWaiting());
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(cacheName)
      .then(cache => cache.match(event.request, {ignoreSearch: true}))
      .then(cachedFiles => {
        console.log(`Event.request: ${event.request}`);
        console.log(`response: ${response}`);
        if (cachedFiles) {return cachedFiles;}
        else {
            return fetch(event.request);
        }

    }).catch(error => {
        console.log(`Files not cached and you are offline. Meesage: ${error}`);
    })
  );
});

// if (event.request.method === 'GET' &&
//         event.request.headers.get('accept').indexOf('text/html') !== -1){

//         }