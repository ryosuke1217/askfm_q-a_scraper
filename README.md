# askfm_q-a_scraper

## 環境  
* windows 10
* selenium IDE 2.9.1  
* BeautifulSoup  
* python 3.5

## 構築手順  

1. Firefoxでselenium IDEのプラグインを追加する。
2. <https://www.python.org/> からpythonをインストールし、pathを通す。  
3. <https://pypi.python.org/pypi/selenium> からselenium-3.3.1.tar.gz (md5)をダウンロードする。  
4. `gzip -dc filename | tar xvf -`コマンドで解凍する ※リナックス上で解凍してください。  
5. 解凍したseleniumディレクトリを`C:\Python27\Lib`直下にコピペする。  
6. <https://sites.google.com/a/chromium.org/chromedriver/downloads> から最新版のChromeDriverをダウンロードする。  
7. ダウンロードしたChromeDriverを`C:\chromedriver\bin`に置き、pathを通す。  
8. `wget http://peak.telecommunity.com/dist/ez_setup.py -O ez_setup.py` でインストーラをダウンロードする。※pythonインストール時に`C:\Python27\Scripts`にeasy_install.exeがない場合に実行
9. `C:\Python27\Scripts`にpathを通す。  
10. `easy_install pip`でpipをインストールする。  
11. `pip install BeautifulSoup`でBeautifulSoupをインストールする。  
12. `pip install beautifulsoup4`を打つ。  
13. `pip install lxml`を打つ。  


cf.seleniumについて
<http://blog.trident-qa.com/2013/05/so-many-seleniums/>

## 使用方法  
* scraper.py 実行時に引数を1つ入力して下さい。  
* 入力した引数をキーワードに、検索します。  
* 取得した画像はdataディレクトリに格納予定  
