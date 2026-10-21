
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

    # 黒も白も石を置けなければゲーム終了
    if not field.has_valid_move("B") and not field.has_valid_move("W"):
        break
     # 現在のプレイヤーが石を置けるか確認する
    if not field.has_valid_move(state):
        print("置ける場所がないため、パス")

        if state == "B":
            state = "W"
        else:
            state = "B"

        continue
    # 現在のプレイヤーを表示する
    if state == "B":
        print("黒の番です")
    else:
        print("白の番です")

    # 石を置く位置を入力する
    x = int(input("横の位置を入力してください（0～7）："))
    y = int(input("縦の位置を入力してください（0～7）："))

    # 石を置いて、手番を交代する
    if field.put_koma(x, y, state):
        if state == "B":
            state = "W"
        else:
            state = "B"
    else:
        print("そこには置けません。別の場所を選んでください。")

# 黒と白の石の数を数える
black_count = 0
white_count = 0

for row in field.board:
    for koma in row:
        if koma is not None:
            if koma.state == "B":
                black_count += 1
            else:
                white_count += 1

# 石の数と勝敗を表示する
print("ゲーム終了")
print("黒:", black_count, "個")
print("白:", white_count, "個")

if black_count > white_count:
    print("黒の勝ち")
elif white_count > black_count:
    print("白の勝ち")
else:
    print("引き分け")