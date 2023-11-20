#!/bin/bash

bench init --skip-redis-config-generation --frappe-branch develop bench

cd bench

bench new-site datingapp.site --admin-password apple --db-root-password apple

bench use datingapp.site

bench set-config -g developer_mode 1

bench --site datingapp.site add-to-hosts

bench get-app https://github.com/rahul007-bit/datingapp

bench --site datingapp.site install-app datingapp
