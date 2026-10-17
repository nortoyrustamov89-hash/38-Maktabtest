# 38-Maktabtest

Responsive frontend for the 38-Maktab Informatika olimpiada quiz.

## Render deploy

This repository includes a Render Blueprint for a static site. It publishes `index.html` over HTTPS. The frontend calls the separate Gemini backend configured in the `quiz-api-base` meta tag.

Default backend URL: `https://38-maktabtest-backend.onrender.com`.

If Render assigns a different backend URL, update the `quiz-api-base` meta tag in `index.html` and redeploy. The backend's `ALLOWED_ORIGINS` must include this site's exact HTTPS origin.

The frontend contains no Gemini API key. It gets questions from the backend and performs answer checking in the browser using the returned answer key.
