import random


def show(game_field):
    for row in game_field:
        print(*row)

# Блок инициализации

size_field = 4
game_field = [[0 for _ in range(size_field)] for _ in range(size_field)]


for num in random.sample(range(16), 2):
    game_field[num // 4][num % 4] = 2

# game_field = [[2, 4, 0, 0], [2, 0, 0, 0], [4, 0, 4, 0], [4, 0, 0, 0]]

show(game_field)



def move(game_field, key):
    if key == 'w':
        for i in range(size_field):
            active_cell = 0
            for j in range(1, size_field):
                if not game_field[j][i]:
                    continue
                if game_field[active_cell][i] == 0:
                    game_field[active_cell][i] = game_field[j][i]
                else:
                    if game_field[active_cell][i] == game_field[j][i]:
                        game_field[active_cell][i] *= 2
                    else:
                        game_field[active_cell + 1][i] = game_field[j][i]
                    active_cell += 1
                game_field[j][i] = 0


move(game_field, input('Введите направление: '))

show(game_field)


