#!/usr/bin/env sh

./../rancher-compose --project-name Comment-Django \
    --url http://192.168.99.100:8080/v1/projects/1a5 \
    --access-key C05AC2C401E588F49224 \
    --secret-key 9Foz7tqmHUD9eWeSA6XLr6CidfgQHfBUjwTZh6Jx \
    -f docker-compose2.yml \
    --verbose up \
    -d --force-upgrade \
    --confirm-upgrade
