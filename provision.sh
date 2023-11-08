sudo apt update -y

sudo apt install -y  \
     fontconfig       \
     gnome-session     \
     gnome-terminal     \
     python3-pip         \
     python3-venv         \
     language-pack-ja      \
     fonts-noto-cjk-extra   \
     fonts-noto-color-emoji

sudo localectl set-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:
