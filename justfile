compose := "docker compose run --rm --no-deps utility"
manage := compose + " python manage.py"

@_default:
    just --list

# Runs migrations
@migrate:
    docker compose run --rm python manage.py migrate --noinput

@makemigrate:
    docker compose run --rm python manage.py makemigrations

@rebuild:
    docker compose rm --force web
    docker compose build --force-rm

@build:
    docker compose build

@down:
    docker compose down

@up *ARGS:
    docker compose up {{ ARGS }}

@run +ARGS="--help":
    {{ manage }} {{ ARGS }}
