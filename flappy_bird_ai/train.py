from flappy_bird import FlappyBird
from ai import FlappyBirdAI

def train_ai():
    ai = FlappyBirdAI()
    num_episodes = 1000

    for episode in range(num_episodes):
        game = FlappyBird()
        state = ai.get_state(game.bird_y, game.bird_y_velocity, game.pipes)
        total_reward = 0

        while not game.game_over:
            action = ai.choose_action(state)
            score, game_over = game.step(action)

            reward = 1 if not game_over else -1000
            next_state = ai.get_state(game.bird_y, game.bird_y_velocity, game.pipes)
            ai.update_q_table(state, action, reward, next_state)

            state = next_state
            total_reward += reward

        print(f"Episode {episode + 1}: Score = {game.score}, Total Reward = {total_reward}")

if __name__ == "__main__":
    train_ai()
