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
def draw_christmas_tree(leaf='', ornament='', height=""):
    for i in range(height):

        spaces = ' ' * (height - i - 1)
        row = ''
        for j in range(i + 1):
            row += leaf
            if j < i:
                row += ornament
        print(spaces + row)

# 聖誕樹層數由下方參數調整
# leaf=''，ornament=''，height=
draw_christmas_tree('*', '0', 5)
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
def check_spell(spell):
    pair = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in spell:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pair[char]:
                print("施法失敗")
                return
            stack.pop()
        elif char not in '([{':
            print("施法失敗")
            return

    if not stack:
        print("施法成功")
    else:
        print("施法失敗")


# 手動輸入咒語
spell = input("請輸入咒語（僅限括號符號）：")
check_spell(spell)
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
