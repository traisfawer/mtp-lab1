#!/bin/sh
# Git hook: проверка Python-кода flake8 перед каждым коммитом.
# Коммит отклоняется, если flake8 находит ошибки в добавленных файлах.

files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
[ -z "$files" ] && exit 0

echo "pre-commit: проверка flake8..."
if ! python -m flake8 $files; then
    echo "pre-commit: flake8 нашёл ошибки, коммит отклонён."
    exit 1
fi
echo "pre-commit: flake8 OK"
exit 0
