import random

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]   # 0 là ô trống
]


class EightPuzzleAgent:

    def __init__(self, state):
        self.state = state

    # Tìm vị trí ô trống
    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    # Kiểm tra trạng thái đích
    def is_goal(self):
        return self.state == GOAL_STATE

    # Lấy các hành động hợp lệ
    def possible_actions(self):
        x, y = self.find_blank()

        actions = []

        if x > 0:
            actions.append("UP")
        if x < 2:
            actions.append("DOWN")
        if y > 0:
            actions.append("LEFT")
        if y < 2:
            actions.append("RIGHT")

        return actions

    # Thực hiện hành động
    def move(self, action):
        x, y = self.find_blank()

        new_x, new_y = x, y

        if action == "UP":
            new_x -= 1
        elif action == "DOWN":
            new_x += 1
        elif action == "LEFT":
            new_y -= 1
        elif action == "RIGHT":
            new_y += 1

        # Hoán đổi ô trống
        self.state[x][y], self.state[new_x][new_y] = \
            self.state[new_x][new_y], self.state[x][y]

    # Simple Reflex Agent
    def reflex_action(self):

        actions = self.possible_actions()

        # Luật đơn giản:
        # chọn ngẫu nhiên 1 hành động hợp lệ
        return random.choice(actions)

    # In bàn cờ
    def display(self):
        for row in self.state:
            print(row)
        print()


# Trạng thái ban đầu
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

agent = EightPuzzleAgent(initial_state)

print("Initial State:")
agent.display()

# Chạy agent
for step in range(10):

    if agent.is_goal():
        print("Goal reached!")
        break

    action = agent.reflex_action()

    print(f"Step {step+1}: {action}")

    agent.move(action)

    agent.display()
