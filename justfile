@migrate:
    uv run python manage.py migrate --noinput

@makemigrate:
    uv run python manage.py makemigrations

@rebuild:
    docker compose rm --force web utility
    docker compose build --force-rm

@build:
    docker compose build

@down:
    docker compose down

@up *ARGS:
    docker compose up {{ ARGS }}
