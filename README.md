# Jet Black Sports Cards & DieCasts website

## Open, review, and test the website

**This repository contains the public storefront source, not the private business dashboard.** GitHub's file preview is not the deployed website. The source is ready for a static host, but do not assume GitHub Pages is enabled or your business domain points to it.

**Fastest local preview on your Mac (no API keys):**

1. Open the Jet Black workspace in VS Code and open a terminal in the `Website` repository folder.
2. Run:

   ```sh
   python3 -m http.server 8001 --bind 127.0.0.1
   ```

3. Open **http://127.0.0.1:8001/** in your browser.
4. Review the logo, layout, mobile sizing, and the eBay/Whatnot links. Stop the preview with **Control+C** in the terminal.

You can also [review the website source on GitHub](https://github.com/jetblacksportscardsanddiecasts/Website), but GitHub's **Code** tab is a source-code viewer, not a running website. This preview has no owner login, product-sync backend, or private customer/finance access.

**Future web access:** GitHub Pages can host this *public static* page after separately enabling Pages in this repository's Settings → Pages, selecting deployment from `main` and `/(root)`. Confirm the published URL after deployment; do **not** replace the existing Shopify domain or change DNS without approval. Pages is **not suitable for hosting the private admin backend or secret-bearing marketplace API integration**.

Public storefront landing page for Jet Black Sports Cards & DieCasts. It directs shoppers to eBay and Whatnot. The page uses HTML and CSS and needs no build or backend.

Run `python3 -m http.server 8001 --bind 127.0.0.1` from this directory and open `http://127.0.0.1:8001/` to preview.

The source is ready for GitHub Pages from `main` at the repository root. The existing business domain can continue serving its current site while the Pages preview is reviewed. Any later backend can provide public product data via an API. Keep private inventory, financial reports and API credentials in the private systems.
