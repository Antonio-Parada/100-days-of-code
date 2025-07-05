import random

class FlappyBirdAI:
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 0.1

    def get_state(self, bird_y, bird_y_velocity, pipes):
        if not pipes:
            return (bird_y, bird_y_velocity, None, None)
        pipe = pipes[0]
        return (bird_y, bird_y_velocity, pipe.x, pipe.height)

    def choose_action(self, state):
        if random.random() < self.exploration_rate:
            return random.choice([True, False])
        q_values = self.q_table.get(state, {True: 0, False: 0})
        return max(q_values, key=q_values.get)

    def update_q_table(self, state, action, reward, next_state):
        old_value = self.q_table.get(state, {}).get(action, 0)
        next_max = max(self.q_table.get(next_state, {True: 0, False: 0}).values())
        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount_factor * next_max)
        if state not in self.q_table:
            self.q_table[state] = {True: 0, False: 0}
        self.q_table[state][action] = new_value
