#!/usr/bin/env bash

if ! [ -e bdd/.env ]; then
  echo "bdd/.env file must exist" >&2
  exit 1
fi

echo -n "Provide new OTP (one-time password) for 2FA: "
read -r NEW_OTP

sed -i "s/AUTH__OTP=.*/AUTH__OTP=$NEW_OTP/g" bdd/.env
