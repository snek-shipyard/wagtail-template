FROM python:3.9-slim

LABEL description="This container serves as an entry point for our future Django projects."

# Developed for Werbeagentur Christian Aichner by Florian Kleber
# for terms of use have a look at the LICENSE file.
MAINTAINER Florian Kleber <kleberbaum@erebos.xyz>

# Add custom environment variables needed by Django or your settings file here:
ENV DJANGO_DEBUG=on \
    DJANGO_SETTINGS_MODULE=esite.settings.production

# The ASGI configuration (customize as needed):
ENV ASGI_VIRTUALENV=/venv \
	ASGI_CONFIG=bifrost.asgi:application \
    ASGI_HOST=0.0.0.0 \
	ASGI_PORT=8000 \
    ASGI_VERBOSITY=1 \
    ASGI_ACCESS_LOG=-

WORKDIR /code/

# Add pre-installation requirements:
ADD requirements/ /requirements/

# Update, install and cleaning:
ADD requirements/ /requirements/
RUN set -ex \
    && BUILD_DEPS=" \
        build-essential \
        git \
        libexpat1-dev \
        libjpeg62-turbo-dev \
        libpcre3-dev \
        libpq-dev \
        zlib1g-dev \
		libffi-dev \
		tini \

    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && python3 -m venv /venv \
    && /venv/bin/pip install -U pip \
    && /venv/bin/pip install --no-cache-dir -r /requirements/production.txt \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Install packages needed to run your application (not build deps):
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN set -ex \
	&& RUN_DEPS=" \
		libexpat1 \
		libjpeg62-turbo \
		libpcre3 \
		libpq5 \
		mime-support \
		postgresql-client \
		procps \
		zlib1g \
	" \
	&& seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
	&& apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
	&& rm -rf /var/lib/apt/lists/*

#RUN which tini

EXPOSE 8000

VOLUME /code/media

ADD . /code/

# Place init, make it executable and
# make sure venv files can be used by uWSGI process:
RUN mv /code/docker-entrypoint.sh / ;\
    chmod +x /docker-entrypoint.sh ;\
    \
    # Call collectstatic with dummy environment variables:
    DATABASE_URL=postgres://none REDIS_URL=none /venv/bin/python manage.py collectstatic --noinput

# I personally like to start my containers with tini
# which start uWSGI, using a wrapper script to allow us to easily add
# more commands to container startup:
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["$ASGI_VIRTUALENV/bin/daphne", \
		"--verbosity", $ASGI_VERBOSITY, \
		"--access-log", $ASGI_ACCESS_LOG, \ 
		"--bind", $ASGI_HOST, \
		"--port", $ASGI_PORT, \
		"--proxy-headers", $ASGI_CONFIG \
]

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
