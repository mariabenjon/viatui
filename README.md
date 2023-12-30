# viatui

Add a viatuix.json.

```
{
  "username": "<username>",
  "password": "<password>",
  "url2": "<login_page>"
}
```

Build.

```
docker-compose build
```

Run script.

```
docker-compose run -d viatui bash -c "sleep 20 && /root/.local/bin/poetry run python scripts/share.py"
```

