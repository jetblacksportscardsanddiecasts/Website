# Jet Black Sports Cards & DieCasts website

Public storefront source with the Jet Black emblem and marketplace links.

## Open, review, and test the website

1. From the Website folder, run `python3 preview.py`. Any terminal works.
2. Open [http://127.0.0.1:8001/](http://127.0.0.1:8001/).
3. Check the logo, resize the window for the mobile layout, and try the eBay, Whatnot, and Instagram links.
4. Stop the preview with **Control+C** in the terminal that started it.

From a second terminal, run `curl -fsS -o /dev/null http://127.0.0.1:8001/` and `curl -fsS -o /dev/null http://127.0.0.1:8001/style.css` to check HTTP delivery. If port 8001 is already in use, run `python3 preview.py --port 8002` and use the address it prints. The preview serves the public HTML and stylesheet only.

## Future hosting

GitHub Pages is available at no additional hosting cost for public repositories, but its usage rules exclude sites primarily directed at facilitating sales. This storefront directs shoppers to marketplaces. The repository stays as the source for the site, with Pages disabled. [GitHub Pages usage limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

A static Cloudflare Pages preview is an alternative. With approval, publish only `index.html` and `style.css` to the provider's preview address. It needs no server functions or domain change, and Cloudflare lists static asset requests as free. Keep the Shopify domain as-is and host the owner dashboard separately. Add an Owner Login link only after a protected owner URL is available. [Cloudflare Pages pricing](https://developers.cloudflare.com/pages/functions/pricing/)

Build a public-only upload ZIP with `python3 package_storefront.py /tmp/jet-black-storefront.zip`. Use a new filename if it already exists. In Cloudflare, go to **Workers & Pages → Create application → Get started → Drag and drop your files**, upload the ZIP, and select **Deploy site**. Check the assigned `pages.dev` URL in a signed-out browser. Direct Upload requires no Git connection, and switching to Git integration later requires a new Cloudflare project. [Direct Upload guide](https://developers.cloudflare.com/pages/get-started/direct-upload/)
