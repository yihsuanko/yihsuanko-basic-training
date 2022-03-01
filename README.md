# yihsuanko-basic-training
## 基本訓練 - 使用VSCode
### 1. 執行程式的方式(一般執行、偵錯模式)
一般執行：開啟[file.py]後直接在terminal執行`python3 file.py`或是按control + f5 <br/>
偵錯執行：開啟[file.py]後，點選要debug的程式碼前方空白，出現紅色小圓點，按上方Run -> start Debugging或是按f5 <br/>
### 2. 設定執行參數(param)
### 3. 設定執行環境變數 (與參數的不同？)
### 4. 快速尋找方法或參數的「源頭」或是「有哪些方法在使用」
### 5. 快速 reformat 程式碼

## 虛擬環境操作(virtualenv)
### 1. 如何判斷目前在正確的虛擬環境中
使用pip安裝virtualenv<br/>
`sudo pip install virtualenv`<br/>
透過virtualenv創造虛擬環境，在啟動虛擬環境的情況下，pip所安裝的套件只存在虛擬環境中，使得專案可以互相獨立，因此不同的專案可以安裝不同版本的使用套件。

建立新的虛擬環境<br/>
```python
cd [資料夾]
python3.9 -m venv venv #Python 3.5 後使用，第二個venv是虛擬環境的名字可以自己取名
../venv/bin/activate #此行venv 是虛擬環境的名字
```
輸入後前面有（venv）或是（自行取的虛擬環境名字）及成功切換到虛擬環境
關閉虛擬環境
```python
deactivate
```
### 2. requirements.txt
使用`pip freeze` 複製一整個已經安裝的套件清單。一個常見的慣例是放這整個清單到一個叫`requirements.txt`的檔案：
```python
pip freeze > requirements.txt
cat requirements.txt  # cat是輸出文件內容的指令
```
`requirements.txt` 用來提交到版本控制，並且作為釋出應用程式的一部分。使其他使用者可以透過 install -r 安裝對應的的套件：
```python
python -m pip install -r requirements.txt
```
## python 操作
1. Package 及 Module
2. 環境變數如何設定與讀取(從 IDE、dotenv 設定)
3. 如何執行一隻 python 程式
4. 直接執行與 if __name__ == '__main__'差別在哪
5. 如何引用套件與使用套件
6. function(使用時機與操作方式)
7. parameter(args, kwargs)
8. return 與 yield
9. Type Hint
## 常見的資料結構(使用時機與操作方式)
1. list
2. set
3. dictionary
## logging
1. 層級與意義
2. 如何輸出至 console
3. 如何輸出至 file

## git
### 1. 如何建立 git repository
進入github個人主頁面，新增repository<br/>
填寫repository name，相當於這個專案的名稱<br/>
git 到想要的本地資料夾
### 2. 全新的專案
如果要建立全新的專案，進入github個人主頁面，新增repository<br/>
```python
cd [資料夾]
git clone [url]  # 在repository有一個綠色code按鈕，點選可以找到url連結 
```
避免多人合作時衝突，如果有修人改過檔案，需要先pull後push
```python
git push <repository> <refspec>
git pull <repository> <refspec>
```
### 3. 已經有用 git 版控的專案
### 4. 如何紀錄(commit)
### 5. 何為衝突(conflict)
