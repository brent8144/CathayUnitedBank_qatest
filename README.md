- [CathayUnitedBank_qatest](#CathayUnitedBank_qatest)
  - [Q1](#Q1)
  - [Q2](#Q2)
  - [Project Layout](#project-layout)
--- 

## Q1

來做一棵聖誕樹吧! 這顆聖誕樹中間除了葉子外還掛滿了燈泡，可以透過輸入的參數來決定聖誕樹的高度，以及中間要掛什麼以及葉子的形狀
例如: 輸入*, 0, 5就會得到右邊的形狀!
```shell
輸出：
     *
    *0*
   *0*0*
  *0*0*0*
 *0*0*0*0*
```
解答
```shell
參考Q1_Christmastree.py
```

---

## Q2
在某個魔法世界中，所有的咒語都是由大括號{}，中括號{}，與小括號()組成。
如果一個咒語中，括號的開頭沒有在正確的位置配上對應的結尾的話咒語就會失敗!

寫出一個函式幫助魔法師們確認是否他們搞錯了咒語吧! 正確記得輸出施法成功，失敗記得輸出施法失敗! 
```shell

下列例子都是施法成功: 
()
{{}}
{()}
{([])}

下列例子都是施法失敗:
[)
({[])}
{{}
({)}
```
解答
```shell
參考Q2_Magic.py
```

---

## Project Layout

```text
Pytest
 ├─ README.md                    #
 |─ src                          # 主程式
      ├─ Q1_Christmastree.py     # Q1程式
      ├─ Q2_Magic.py             # Q2程式


```

---
