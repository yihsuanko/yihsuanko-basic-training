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
### 1. list
List(串列)是一個資料型態，用來存放多個不同資料型態的資料(元素)。list 可以用來儲存一連串有順序性的元素。<br/>
List的特性：<br/>
    1. Iterable(可疊代的)：所以for迴圈可以應用在串列上。<br/>
    2. Modifiable(可修改的)：串列中的元素可以透過Python提供的串列方法(Method)來進行修改。<br/>

建立List的方法：<br/>
    1. 以逗號分隔並且用 [] 符號將所有元素括起來。 `a = [1,2,3]`
    2. 使用Python的list()，傳入Iterable(可疊代的)物件來建立串列。`a = list(range(10))`

存取使用List的方法：<br/>
    1. Python串列的位置索引值從0開始，假設 `a = [1,2,3]`，想要得到1，`print(a[0])`
    2. 使用 `[:]` 符號並傳入索引值，包含前不包含後
    3. 使用append()，將元素新增至串列的最後。 `a.append(4)  # print(a) -> [1,2,3,4]`
    4. 使用insert()，將元素新增至串列的特定位置。`a.instert(1,4)  # print(a) -> [1,4,2,3]`
    5. 使用index()，可以將要尋找的串列元素傳入，它會回傳該元素的位置索引值，如果要尋找的串列元素不在串列中，則會出現錯誤訊息。如果此元素在串列中有多個，index()只會找第一個出現的。`print(a.index(1)) -> 0`

修改刪除List的方法：<br/>
    1. 使用 [] 符號存取想修改的索引值，接著指派新的值 `a[1] = 1  # print(a) -> [1,1,3]`
    2. 使用pop()，將串列的最後一個元素刪除。如果想刪除特定位置的元素，則傳入位置索引值。
    3. 使用del 指令，指定要刪除的範圍位置索引值。
    4. 使用remove()，傳入想刪除的元素。如果此元素在串列中有多個，remove()只會刪除第一個出現的。

### 2. set
Python set 物件是無序的集合(unordered collection)，**set集合不會包含重複的資料**。

建立set的方法：<br/>
    1. 以逗號分隔並且用 {} 符號將所有元素括起來。 `b = {1,2,3}`
    2. 使用Python的set()，傳入Iterable(可疊代的)物件。 `b = set((1,2,3))`

使用set的方法：<br/>
    1. 使用remove()，傳入想刪除的元素。
    2. 取 set 的交集要使用 & 符號就會取出兩集合中相同的元素。
    3. 取 set 的聯集要使用 | 符號就會取出兩集合中所有的元素。
    4. 取 set 的差集要使用 - 符號就會取出集合與另外一個集合的差集。

### 3. dictionary
dictionary (dict)是一個 key-value 對應的容器，能用key來查詢對應的value，所以一個dict裡的 key 是不會重複的，具有唯一性。,<br/>
dict可以動態地新增與刪除資料，且資料儲存沒有順序性。

建立dict的方法：<br/>
    1. 使用{}建立空dict，或包含key-value `c = {}`, `c = {"apple":1, "banana":2, "car":3}`
    2. 使用dict()建立空dict `c = dict()`

使用dict的方法：<br/>
    1. 新增資料：c["key"] = value `c["duck"] = 5`
    2. 刪除資料：del c["key"] `del c["duck"]`
    3. 測試key有沒有存在dict裡 `value1 = c.get('apple')`，如果 key 有存在的話就回傳該value，如果key沒有存在的話就回傳預設值，沒有給定預設值的話會回傳None。

## logging
### 1. 層級與意義
### 2. 如何輸出至 console
### 3. 如何輸出至 file

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
git pull 
git branch -M main  # 轉到要push的分支
# git push 方式
git add .
git commit -m "message"  # 紀錄commit的方式
git push -u origin main
```
### 3. 已經有用 git 版控的專案
```python
git remote add origin <your url>
```
### 4. 如何紀錄(commit)
```python
git commit -m "message"  # 將跟改內容簡單記錄，方便其他人理解跟改內容
```
### 5. 何為衝突(conflict)
當上傳內容與原本內容不同時，會出現衝突
