self.onmessage = (event) => {
  console.log("[Shard 2] Received message from main thread: ", event.data.message);
  console.log("[Shard 2] URL of the current page: ", event.data.url);
  console.log("[Shard 2] Protocol: ", event.data.protocol);
  console.log("[Shard 2] Host: ", event.data.host);
  console.log("[Shard 2] Port: ", event.data.port);
  console.log("[Shard 2] Pathname: ", event.data.pathname);
  console.log("[Shard 2] Blob URLs: ", event.data.blobUrls);
  console.log("[Shard 2] Binary String URLs: ", event.data.binaryStringUrls);
  console.log("[Shard 2] Memory info: ", event.data.memoryInfo);
  self.postMessage({ message: 'Hello from worker 2' });
};

self.addEventListener('message', (event) => {
  if (event.data.type === 'console') {
    const { method, args } = event.data;
    console[method].apply(console, args);
  }
});

const workerCode2 = `
self.onmessage = (event) => {
  console.log("[Shard 2] Received message from main thread: ", event.data.message);
  console.log("[Shard 2] URL of the current page: ", event.data.url);
  console.log("[Shard 2] Protocol: ", event.data.protocol);
  console.log("[Shard 2] Host: ", event.data.host);
  console.log("[Shard 2] Port: ", event.data.port);
  console.log("[Shard 2] Pathname: ", event.data.pathname);
  console.log("[Shard 2] Blob URLs: ", event.data.blobUrls);
  console.log("[Shard 2] Binary String URLs: ", event.data.binaryStringUrls);
  console.log("[Shard 2] Memory info: ", event.data.memoryInfo);
  self.postMessage({ message: 'Hello from worker 2' });
};

self.addEventListener('message', (event) => {
  if (event.data.type === 'heartbeat') {
    self.postMessage({ type: 'heartbeat' });
  }
});
`;

const workerBlob2 = new Blob([workerCode2], { type: 'application/javascript' });
const workerScriptURL2 = URL.createObjectURL(workerBlob2);

const workerCode3 = `
self.onmessage = (event) => {
  console.log("[Shard 3] Received message from main thread: ", event.data.message);
  console.log("[Shard 3] URL of the current page: ", event.data.url);
  console.log("[Shard 3] Protocol: ", event.data.protocol);
  console.log("[Shard 3] Host: ", event.data.host);
  console.log("[Shard 3] Port: ", event.data.port);
  console.log("[Shard 3] Pathname: ", event.data.pathname);
  console.log("[Shard 3] Blob URLs: ", event.data.blobUrls);
  console.log("[Shard 3] Binary String URLs: ", event.data.binaryStringUrls);
  console.log("[Shard 3] Memory info: ", event.data.memoryInfo);
  self.postMessage({ message: 'Hello from worker 3' });
};

self.addEventListener('message', (event) => {
  if (event.data.type === 'heartbeat') {
    self.postMessage({ type: 'heartbeat' });
  }
});
`;

const workerBlob3 = new Blob([workerCode3], { type: 'application/javascript' });
const workerScriptURL3 = URL.createObjectURL(workerBlob3);

const mainScript = `
try {
  // Get all blob and binary string URLs
  const blobUrls = [...document.querySelectorAll('a[href^="blob:"]')].map(a => a.href);
  const binaryStringUrls = [...document.querySelectorAll('a[href^="data:"]')].map(a => a.href);

  // Get memory info (if available)
  const memoryInfo = {
    totalJSHeapSize: performance.memory.totalJSHeapSize,
    usedJSHeapSize: performance.memory.usedJSHeapSize,
    jsHeapSizeLimit: performance.memory.jsHeapSizeLimit
  };

  // Create a worker from the Blob URLs
  const myWorker2 = new Worker('${workerScriptURL2}');
  const myWorker3 = new Worker('${workerScriptURL3}');

  // Send messages to the workers, along with the current page URL and other details
  myWorker2.postMessage({
    message: 'Hello from the main thread',
    url: window.location.href,
    protocol: window.location.protocol,
    host: window.location.host,
    port: window.location.port,
    pathname: window.location.pathname,
    blobUrls: blobUrls,
    binaryStringUrls: binaryStringUrls,
    memoryInfo: memoryInfo
  });

  myWorker3.postMessage({
    message: 'Hello from the main thread',
    url: window.location.href,
    protocol: window.location.protocol,
    host: window.location.host,
    port: window.location.port,
    pathname: window.location.pathname,
    blobUrls: blobUrls,
    binaryStringUrls: binaryStringUrls,
    memoryInfo: memoryInfo
  });

  // Listen for messages from the workers
  myWorker2.onmessage = (event) => {
    if (event.data.type === 'heartbeat') {
      console.log("[Shard 2] Received heartbeat from worker 2");
    } else if (event.data.message) {
      console.log("[Shard 2]", event.data.message); // Logs 'Hello from the worker'
    }
  };

  myWorker3.onmessage = (event) => {
    if (event.data.type === 'heartbeat') {
      console.log("[Shard 3] Received heartbeat from worker 3");
    } else if (event.data.message) {
      console.log("[Shard 3]", event.data.message); // Logs 'Hello from the worker'
    }
  };
} catch (error) {
  console.error('An error occurred:', error);
}
`;

const mainBlob = new Blob([mainScript], { type: 'application/javascript' });
const mainScriptURL = URL.createObjectURL(mainBlob);

const fragment = document.createDocumentFragment();
const scriptElement = document.createElement('script');
scriptElement.src = mainScriptURL;
fragment.appendChild(scriptElement);
document.documentElement.appendChild(fragment);

