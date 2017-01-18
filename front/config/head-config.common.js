/**
 * Configuration for head elements added during the creation of index.html.
 *
 * All href attributes are added the publicPath (if exists) by default.
 * You can explicitly hint to prefix a publicPath by setting a boolean value to a key that has
 * the same name as the attribute you want to operate on, but prefix with =
 *
 * Example:
 * { name: 'msapplication-TileImage', content: '/assets/icon/ms-icon-144x144.png', '=content': true },
 * Will prefix the publicPath to content.
 *
 * { rel: 'apple-touch-icon', sizes: '57x57', href: '/assets/icon/apple-icon-57x57.png', '=href': false },
 * Will not prefix the publicPath on href (href attributes are added by default
 *
 */
 module.exports = {
   link: [
     /** <link> tags for "apple-touch-icon" (AKA Web Clips). **/
     { rel: "apple-touch-icon", sizes: "72x72", href: "/assets/icon/apple-touch-icon-72+%F972.png" },
     { rel: "apple-touch-icon", sizes: "114x114", href: "/assets/icon/apple-touch-icon-114+%F9114.png" },

     /** <link> tags for favicons **/
     { rel: "icon", type: "image/png", sizes: "32x32", href: "/assets/icon/favicon-32x32.png" },
     { rel: "icon", type: "image/png", sizes: "48x48", href: "/assets/icon/favicon-48x48.png" },
     { rel: "icon", type: "image/png", sizes: "16x16", href: "/assets/icon/favicon-16x16.png" },
   ],
   meta: [
     { name: "msapplication-TileColor", content: "#00bcd4" },
     { name: "msapplication-TileImage", content: "/assets/icon/apple-touch-icon-114+%F9114.png", "=content": true },
     { name: "theme-color", content: "#00bcd4" }
   ]
 };
