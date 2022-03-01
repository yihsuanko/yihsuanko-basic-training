def function_name(name, birth, id=1):  # 使用此function時，一定要輸入name, birth，id如果沒輸入會自動為1
    # 欲執行程式碼
    print(name, birth, id)

function_name(name="Tom", birth="3/1", id=5)  # Tom 3/1 5 
function_name("Tom", "3/1", id=5)  # Tom 3/1 5 
function_name(name="Jack", birth="12/1")