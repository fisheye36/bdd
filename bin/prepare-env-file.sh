#!/usr/bin/env bash

if ! [ -e bdd/.env ]; then
  cp bdd/.env.example bdd/.env
  "$EDITOR" bdd/.env
fi
