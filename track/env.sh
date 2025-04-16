#!/bin/bash

export LDFLAGS="-L$(brew --prefix tcl-tk)/lib"
export CPPFLAGS="-I$(brew --prefix tcl-tk)/include"
export PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"
export PYENV_ROOT="$(pwd)/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Optional: for pyenv-virtualenv
if command -v pyenv virtualenv-init &>/dev/null; then
  eval "$(pyenv virtualenv-init -)"
fi
