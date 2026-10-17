# 38-Maktabtest

Responsive frontend for the 38-Maktab Informatika olimpiada quiz.

## Render deploy

This repository includes a Render Blueprint for a static site. The build publishes `index.html` over HTTPS and injects the `API_BASE_URL` Render environment variable into the frontend.

During the initial Render Blueprint setup, provide `API_BASE_URL` as the deployed backend HTTPS base URL, without `/api/questions` (for example, `https://38-maktabtest-backend.onrender.com`).

The backend's `ALLOWED_ORIGINS` must include this site's exact HTTPS origin. If Render assigns a different frontend hostname, update that backend environment variable and restart/redeploy the backend.

The frontend contains no Gemini API key. It gets questions from the backend and performs answer checking in the browser using the returned answer key.
