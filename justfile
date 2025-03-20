compose := "docker compose run --rm --no-deps utility"
manage := compose + " python manage.py"

@_default:
    just --list

# Runs migrations
@migrate:
    docker compose run --rm web python manage.py migrate --noinput

@makemigrations:
    docker compose run --rm web python manage.py makemigrations

@rebuild:
    docker compose rm --force web
    docker compose build --force-rm

@build:
    docker compose build

@down:
    docker compose down

@up *ARGS:
    docker compose up {{ ARGS }}

[doc("Runs `python manage.py` inside the container")]
@run +ARGS="--help":
    {{ manage }} {{ ARGS }}

# uv --quiet tool run --with pre-commit-uv pre-commit autoupdate

# Run pre-commit hooks on all files in the repository
# @lint:
#     uv --quiet tool run --with pre-commit-uv pre-commit run --all-files
