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


# 輸入咒語
spell = input("請輸入咒語（僅限括號符號）：")
check_spell(spell)

# 20250722