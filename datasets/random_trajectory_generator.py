import random

STATE_FILE = "states.txt" # file when you can find the set of all possibles states, one per line
OUTPUT_FILE = "simple_example.dat"
N = 600

# min and max number of points in a trajectory
MIN_NB_POINTS = 1
MAX_NB_POINTS = 20 

def get_states(state_file):
    """
    Get the list of all possible states (one per line) from a file.
    """
    states = []
    with open(state_file, 'r') as file:
        for line in file:
            states.append(line.strip())
    return states

def generate_trajectory(index, num_states):
    """Generate a trajectory with the given index and number of states."""
    states = get_states(STATE_FILE)
    points = [random.choice(states) for _ in range(num_states)]
    points_str = ";".join(points)
    trajectory = f"# {index}:\n>0:{points_str};"
    return trajectory

def generate_trajectories(N):
    """Generate N trajectories with varying number of states."""
    # generate a random number of states for each trajectory
    num_states_list = [random.randint(MIN_NB_POINTS, MAX_NB_POINTS) for _ in range(N)]
    trajectories = []
    for i in range(N):
        num_states = num_states_list[i] if i < len(num_states_list) else random.randint(MIN_NB_POINTS, MAX_NB_POINTS)
        trajectory = generate_trajectory(i, num_states)
        trajectories.append(trajectory)
    return trajectories

def save_trajectories_to_file(trajectories, filename):
    """Save the generated trajectories to a file."""
    with open(filename, 'w') as file:
        for trajectory in trajectories:
            file.write(trajectory + "\n")

if __name__ == "__main__":
    trajectories = generate_trajectories(N)
    save_trajectories_to_file(trajectories, OUTPUT_FILE)

    print(f"Trajectories generated and saved to '{OUTPUT_FILE}'.")
