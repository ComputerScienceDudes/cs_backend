#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
# CSS is committed so Flask deployments do not need a Sass compiler.
mkdir -p static/css
case "$(sass --version)" in
    *Ruby*) compiler_options="--no-cache --sourcemap=none" ;;
    *) compiler_options="--no-source-map" ;;
esac
for source in static/scss/*.scss; do
    name=$(basename "$source" .scss)
    case "$name" in _*) continue ;; esac
    sass $compiler_options --style compressed "$source" "static/css/$name.css"
done
