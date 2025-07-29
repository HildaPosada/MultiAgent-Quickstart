#! /usr/bin/env nix-shell
#! nix-shell -i bash shell.nix

cd "$(dirname $1)"
echo "Running '$1'..."
export PYTHONUNBUFFERED=1
uv run "$(basename $1)"
