# BingeList

BingeList is a social movie and TV tracker built with Flask. Search for titles, build watchlists, write reviews, follow other users, chat with friends, and see how well your taste matches theirs.

Movie and TV data comes from the [TMDB API](https://www.themoviedb.org/documentation/api).

## Features

- **Accounts:** sign up, log in, edit your profile and avatar
- **Search:** find movies, TV shows, and other users, with recent searches and trending titles
- **Lists:** a default Watchlist plus custom lists with cover images
- **Reviews:** rate and review titles in your collection (1 to 10)
- **Social:** follow and unfollow users, view followers and following
- **Messaging:** inbox and one-to-one chat
- **Taste comparison:** compatibility score and badge (Soulmates, Besties, Rivals, and more) based on shared ratings
- **Recommendations:** home page suggestions based on your last search, popular titles, and genre rows
- **Caching and fallback:** TMDB responses are cached in the database, and a built-in catalog keeps the site usable if TMDB is unreachable

## Tech stack

- Python 3.11, Flask
- Flask-SQLAlchemy, Flask-Login, Flask-SocketIO
- PostgreSQL (Neon) in production, SQLite for quick local runs
- Deployed on Vercel

## Project structure

```
BingeList/
├── app.py            # Routes and app setup
├── config.py         # Configuration (reads environment variables)
├── extensions.py     # db and login_manager instances
├── models.py         # SQLAlchemy models
├── requirements.txt
├── templates/        # Jinja2 HTML templates
└── static/           # CSS, JS, uploads
```

## Getting started

### 1. Clone and install

```bash
git clone <your-repo-url>
cd BingeList
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

### 2. Set environment variables

| Variable | Required | Description |
|---|---|---|
| `TMDB_API_KEY` | Yes | Your TMDB v3 API key |
| `SECRET_KEY` | Yes in production | Long random string used to sign sessions |
| `DATABASE_URL` | No | Postgres connection string. Falls back to local SQLite if unset |

Generate a secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

PowerShell example:

```powershell
$env:TMDB_API_KEY="your_tmdb_key"
$env:SECRET_KEY="your_random_string"
$env:DATABASE_URL="postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require"
```

Never commit these values or a `.env` file.

### 3. Run

```bash
python app.py
```

Open http://localhost:5001. Tables are created automatically on first start.

## Deploying to Vercel with Neon

1. Create a Postgres database on [Neon](https://neon.tech) and copy the connection string (pooled, ending in `?sslmode=require`).
2. In Vercel, go to **Settings > Environment Variables** and add `DATABASE_URL`, `SECRET_KEY`, and `TMDB_API_KEY` for all environments.
3. Make sure `requirements.txt` includes a Postgres driver (`psycopg[binary]` or `psycopg2-binary`).
4. Push to `main`. Vercel redeploys automatically. Redeploy manually after changing environment variables.

Notes:

- `db.create_all()` creates missing tables but never alters existing ones. If you change a column size, migrate the table or drop it in a development database.
- Vercel's filesystem is temporary, so uploaded avatars and list covers do not persist. Use external storage (Vercel Blob, Cloudinary, Supabase Storage) for permanent uploads.

## Contributing

1. Create a branch: `git checkout -b my-change`
2. Commit your work and push: `git push -u origin my-change`
3. Open a pull request and reference the issue with `Fixes #N`

## Security

- Keep API keys, database passwords, and `SECRET_KEY` out of the repository and out of logs.
- If a credential is ever exposed, rotate it immediately.

## Acknowledgements

This product uses the TMDB API but is not endorsed or certified by TMDB.
