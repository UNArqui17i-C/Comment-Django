#!/usr/bin/env sh

./../rancher-compose --project-name Comment-Django \
    --url http://192.168.99.100:8080/v1/projects/1a5 \
    --access-key 8F57C9A1CC638B8B6F5C \
    --secret-key 7AxpfFWycEsS85DEZWXRp8smnijGBsiAvJCUoNpi \
    -f docker-compose.yml \
    --verbose up \
    -d --force-upgrade \
    --confirm-upgrade
