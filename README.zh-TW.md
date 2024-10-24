燒瓶節點化器

# Flask Nodezator

> 使用 Nodezator 的 Python Flask 應用程式

開啟此網址`https://github.dev/`而不是`https://github.com/`使用基於 Web 的 Visual Studio Code IDE。

# 執行摘要

按如下方式運行該應用程式：

1) 輸入`flask_app`目錄：`$ cd flask_app`2）如果不存在，則在內部建立一個虛擬環境`flask_app` directory: `$ python3 -m venv .venv`（蘋果系統：`$ virtualenv .venv`)

若出現以下情況，請遵循其建議：

虛擬環境沒有創建成功，因為ensurepip沒有
可用的。

在 Debian/Ubuntu 系統上，需要安裝 python3-venv
使用以下命令進行打包。

    sudo apt-get update
    sudo apt install python3.10-venv

您可能需要將 sudo 與該命令一起使用。  安裝 python3-venv 後
包，重新建立您的虛擬環境。

在 macOS 上請參閱<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3）啟動虛擬環境，輸入：`. .venv/bin/activate`（蘋果系統：`source .venv/bin/activate`)
4) Run `$ pip install -r requirements.txt`5）運行：`$ cd app`然後`$ npm install`最後`$ cd ..`6）將Flask App設定到app目錄：`(.venv) $ export FLASK_APP=app`7）將Flask環境設定為True進行開發：`(.venv) $ export FLASK_DEBUG=True`8) 設定 SQLAlchemy 資料庫 URI：`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`，預設為`sqlite:///app.db`9）設定SQLAlchemy軌道修改：`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10）設定密鑰：`(.venv) $ export SECRET_KEY=********`11）運行燒瓶應用程式：〜`(.venv) $ flask run`~`(.venv) $ python3 run.py`12）根據提示開啟Web介面
13) 使用`CTRL+c`退出網路伺服器。
14) 或運行flask命令列介面：`(.venv) $ flask shell`15) 執行任意 Flask 指令：>>>
16) 使用`exit()`退出命令列介面。

一般來說，在開發 Flask 應用程式時，您可以採取以下步驟來管理資料庫遷移：

1）修改資料庫模型。

2）如果沒有`migrations`目錄還存在於`flask_app`目錄，運行` (.venv) flask_app $ flask db init`.

3) 產生遷移腳本`flask db migrate -m "some comment"`命令。如果自上次遷移以來沒有發生任何更改，系統會提示您`No changes in schema detected.`。因此，您可以毫無恐懼地重複此命令。

4) 檢查產生的遷移腳本並根據需要進行修正。

5) 將變更套用到資料庫`flask db upgrade`命令。

6) 若要還原先前的資料庫版本，請使用`flask db downgrade`命令。

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
