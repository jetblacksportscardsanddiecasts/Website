# Jet Black Sports Cards & DieCasts website

Public storefront source with the Jet Black emblem and marketplace links.

## Open, review, and test the website

1. From the Website folder, run `python3 preview.py`. Any terminal works.
2. Open [http://127.0.0.1:8001/](http://127.0.0.1:8001/).
3. Check the logo, resize the window for the mobile layout, and try the eBay, Whatnot, and Instagram links.
4. Stop the preview with **Control+C** in the terminal that started it.

From a second terminal, run `curl -fsS -o /dev/null http://127.0.0.1:8001/` and `curl -fsS -o /dev/null http://127.0.0.1:8001/style.css` to check HTTP delivery. If port 8001 is already in use, run `python3 preview.py --port 8002` and use the address it prints. The preview serves the public HTML and stylesheet only.

## Future hosting

GitHub Pages can serve the public static page after separate hosting approval. The existing Shopify domain can stay in place while the preview is reviewed. Keep the private dashboard, seller reports, and marketplace credentials in the separate Inventory system.
