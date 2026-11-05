# Basketfield: real photograph sources

No generated pictures are used as merchandise. Every product and introductory photo is a genuine existing photograph from Unsplash under the [Unsplash License](https://unsplash.com/license).

The photographs illustrate fictional products; they are not merchant listings, endorsements, or verified merchandise available for purchase.

- **tote**: Yue Iris — https://unsplash.com/photos/beige-tote-bag-N9BYrQ1b78k — `https://images.unsplash.com/photo-1565072893031-7e6b2dacf296?auto=format&fit=crop&w=840&q=78`
- **lamp**: Vladislav Glukhotko — https://unsplash.com/photos/a-lamp-that-is-on-top-of-a-table-SbGLQAtv8Gk — `https://images.unsplash.com/photo-1678819483347-3faeb1e426c0?auto=format&fit=crop&w=840&q=78`
- **mug**: Sixteen Miles Out — https://unsplash.com/photos/tea-filled-white-ceramic-mug-on-white-ceramic-saucer-dPkn4562j3E — `https://images.unsplash.com/photo-1512311734173-51a49c854e78?auto=format&fit=crop&w=840&q=78`
- **audio**: Caleb Wright — https://unsplash.com/photos/a-close-up-of-a-pair-of-headphones-o1tTNjA-6V0 — `https://images.unsplash.com/photo-1697652974624-470e68497990?auto=format&fit=crop&w=840&q=78`
- **book**: Kelly Sikkema — https://unsplash.com/photos/notebook-and-writing-supplies-on-wooden-surface-cGGCg7quYn0 — `https://images.unsplash.com/photo-1743385779392-cab22721fac6?auto=format&fit=crop&w=840&q=78`
- **shoe**: mostafa mahmoudi — https://unsplash.com/photos/a-pair-of-running-shoes-on-a-white-background-W_uDEmTq0po — `https://images.unsplash.com/photo-1637437757614-6491c8e915b5?auto=format&fit=crop&w=840&q=78`

## Privacy consideration

The preview defaults to remote Unsplash photography so the product images load immediately when opened online. This means the browser contacts Unsplash's image server; do not claim the site makes zero third-party requests. User clicks, fictional permissions, rewards choices, and simulated data-scientist decisions stay within the tab and are not sent to Unsplash by our JavaScript.

To remove those external image loads before publication, run `python3 download_photos.py` from the repo root on a computer with internet access. The script downloads the original photographs into `privacy/assets/` and changes their URLs in the privacy HTML to local paths. GitHub Pages will then serve them from the same site.