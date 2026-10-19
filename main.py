from field import Field

field = Field()
state = "B"

while True:
    print()

    # 盤面を表示する
    for row in field.board:
        for koma in row:
            if koma is None:
                print(".", end=" ")
            else:
                print(koma.state, end=" ")
        print()

    # 現在のプレイヤーを表示する
    if state == "B":
        print("黒の番です")
    else:
        print("白の番です")

    # 駒を置く場所を入力する
    x = int(input("横の位置を入力してください（0～7）："))
    y = int(input("縦の位置を入力してください（0～7）："))

    # 駒を置けるか確認する
    if field.put_koma(x, y, state):
        # 黒と白を交代する
        if state == "B":
            state = "W"
        else:
            state = "B"
    else:
        print("そこには置けません。別の場所を選んでください。")