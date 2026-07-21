# AGENTS.md

## Cursor Cloud specific instructions

This is a static personal portfolio site built with **Astro 6** and deployed to **Cloudflare Workers** (static assets via `wrangler.jsonc`). There is no backend/database.

- Dev server: `npm run dev` serves at `http://localhost:4321/` (see `README.md` for the full command table).
- Build: `npm run build` outputs static files to `./dist/` (git-ignored).
- Preview production build: `npm run preview`.
- There is no configured lint script. `npm run astro -- check` (type checking) requires `@astrojs/check` + `typescript`, which are NOT in `package.json`; installing them triggers an interactive prompt, so it is not part of the standard workflow.
- Node `>=22.12.0` is required (see `engines` in `package.json`).
- Pages live in `src/pages/`; project sub-pages resolve at routes like `/projects/lunar-lander/`.
