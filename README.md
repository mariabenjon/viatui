# viatui

## Quick start

Add a viatuix.json.

```
{
  "username": "<username>",
  "password": "<password>",
  "url2": "<login_page>"
  "url2": "<other_page>
  "sentence1": "some text"
}
```

Build.

```
docker-compose build
```

Run beauty-bot continously, doing its thing every 10 minutes or so, except for between 11pm and 7am.

`pyton beaty-pot.py`

Or manually run the script once.

```
docker-compose run -d viatui bash -c "sleep 20 && /root/.local/bin/poetry run python scripts/share.py"
```

