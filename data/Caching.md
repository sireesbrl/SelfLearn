When it comes to web application caching in the backend, there are several methods commonly used to improve performance and reduce load on servers. Some of the key methods include:

**Database Query Result Caching**: This involves caching the results of frequently executed database queries to avoid hitting the database repeatedly for the same data. Tools like Redis or Memcached can be used for this purpose.

**Page Caching**: This technique involves storing the entire HTML content of web pages that are accessed frequently. Cached pages can be served directly to users without re-generating them on every request, reducing server load. Tools like Varnish or built-in caching mechanisms in web frameworks like Rails can be used for page caching.

**Object Caching**: This method involves caching the results of expensive operations or complex computations. By storing the computed result in memory, subsequent requests can retrieve the cached result instead of re-calculating it. Redis or Memcached are commonly used for object caching.

**HTTP Caching**: Utilizing HTTP caching headers like Cache-Control and Expires, along with ETag and Last-Modified headers, helps in storing resources in the browser cache or intermediate caches to reduce the need for subsequent requests to the server.

**Content Delivery Network (CDN) Caching**: Leveraging CDNs to cache static assets like images, CSS, and JavaScript files in edge servers distributed globally can improve load times by serving content from servers closer to the user.

**Session Caching**: Storing session data in a fast, in-memory cache like Redis can reduce the load on the main application server and provide faster access to session-related information.

**Fragment Caching**: This method involves caching specific parts of a web page (fragments) that are expensive to generate. By caching only the dynamic parts of a page, the rest of the page can remain dynamic while improving performance.

These caching methods can be used individually or in combination to optimize the performance of web applications, reduce server load, and enhance user experience. The choice of caching method depends on the specific requirements and architecture of the web application.

**Resources**:

* **Client-Side**
    * [Everything You Need to Know About HTTP Caching](https://www.youtube.com/watch?v=HiBDZgTNpXY), etc.

* **Server-Side**
    * [Server-Side Caching](https://www.starwindsoftware.com/resource-library/server-side-caching/)
    * [Server-Side Caching & Client-Side Caching](https://www.codingninjas.com/codestudio/library/server-side-caching-and-client-side-caching), etc.

* **Redis**
    * [Redis Official Website](https://redis.io/)
    * [Redis in 100 Seconds](https://www.youtube.com/watch?v=G1rOthIU-uo), etc.