# SEM

## installation
pythonのパッケージ管理ツールのインストール
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
# source ~/.bashrc 
source ~/.zshrc
```
ライブラリをインストールし，仮想環境をactivate
```sh
uv sync
source ~/.venv/bin/activate
```

## usage
```sh
python SEM.py --data_path data.csv --diagram_path sem_diagram3.png
```

