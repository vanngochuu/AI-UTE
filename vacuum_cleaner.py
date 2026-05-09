import random

# =========================
# ENVIRONMENT
# 0 = CLEAN
# 1 = DIRTY
# =========================

floor = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

m = len(floor)
n = len(floor[0])

# Vị trí ban đầu của máy hút bụi
x, y = 1, 1


# =========================
# PRINT ENVIRONMENT
# =========================

def print_floor():

    for i in range(m):

        row = ""

        for j in range(n):

            if i == x and j == y:
                row += " A "
            else:
                row += f" {floor[i][j]} "

        print(row)

    print()


# =========================
# RULES
# =========================

def possible_move(x, y):

    move = []

    if x > 0:
        move.append("UP")

    if x < m - 1:
        move.append("DOWN")

    if y > 0:
        move.append("LEFT")

    if y < n - 1:
        move.append("RIGHT")

    return move


# =========================
# SIMPLE REFLEX AGENT
# =========================

def reflex_agent(x, y):

    state_value = floor[x][y]

    moves = possible_move(x, y)

    # RULE 1
    if state_value == 0:

        action = random.choice(moves)

    # RULE 2
    elif state_value == 1:

        # hút bụi
        floor[x][y] = 0

        action = random.choice(moves)

    return action


# =========================
# MOVE AGENT
# =========================

def move_agent(x, y, action):

    if action == "UP":
        x -= 1

    elif action == "DOWN":
        x += 1

    elif action == "LEFT":
        y -= 1

    elif action == "RIGHT":
        y += 1

    return x, y


# =========================
# RUN AGENT
# =========================

print("Initial Environment:")
print_floor()

for step in range(15):

    print(f"STEP {step+1}")

    print("Current Position:", (x, y))
    print("Current State:", floor[x][y])

    action = reflex_agent(x, y)

    print("Action:", action)

    x, y = move_agent(x, y, action)

    print_floor()
