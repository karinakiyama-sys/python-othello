
import random
from field import Field


field = Field()

# CPUは黒、人間は白
CPU = "B"
HUMAN = "W"

state = "B"

while True:
    print()
    field.display()

    # 両方とも置けなければ終了
    if (
        not field.has_valid_move("B")
        and not field.has_valid_move("W")
    ):
        break

    # 今の番の人が置けなければパス
    if not field.has_valid_move(state):
        if state == CPU:
            print("CPUは置ける場所がないためパス")
        else:
            print("置ける場所がないためパス")

        state = "W" if state == "B" else "B"
        continue

    # CPUの番
    if state == CPU:
        moves = field.get_valid_moves(CPU)
        x, y = random.choice(moves)

        print(f"CPUが置きました：横{x}、縦{y}")
        field.put_koma(x, y, CPU)

    # 人間の番
    else:
        print("あなた（白）の番です。")

        try:
            x = int(input("横の位置を入力してください（0～7）："))
            y = int(input("縦の位置を入力してください（0～7）："))
        except ValueError:
            print("数字を入力してください。")
            continue

        if not field.put_koma(x, y, HUMAN):
            print("そこには置けません")
            continue

    # 次の番へ
    state = "W" if state == "B" else "B"


# ゲーム終了
print()
print("ゲーム終了！")
field.display()

black_count = field.count_stones("B")
white_count = field.count_stones("W")

print(f"黒（CPU）：{black_count}個")
print(f"白（あなた）：{white_count}個")

if black_count > white_count:
    print("CPUの勝ち")
elif white_count > black_count:
    print("あなたの勝ち")
else:
    print("引き分け")
