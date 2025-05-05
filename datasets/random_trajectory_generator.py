import random

FILENAME = "simple_example.dat"
N = 600

# min and max number of points in a trajectory
MIN_NB_POINTS = 1
MAX_NB_POINTS = 20 

# min and max coordinates of a point
MIN_COORDINATE = 0
MAX_COORDINATE = 10

def generate_random_point():
    """Generate a random point with coordinates (x, y)."""
    x = round(random.uniform(MIN_COORDINATE, MAX_COORDINATE), 3)
    y = round(random.uniform(MIN_COORDINATE, MAX_COORDINATE), 3)
    return f"{x},{y}"

def generate_trajectory(index, num_points):
    """Generate a trajectory with the given index and number of points."""
    points = [generate_random_point() for _ in range(num_points)]
    points_str = ";".join(points)
    trajectory = f"# {index}:\n>0:{points_str};"
    return trajectory

def generate_trajectories(N):
    """Generate N trajectories with varying number of points."""
    # generate a random number of points for each trajectory
    num_points_list = [random.randint(MIN_NB_POINTS, MAX_NB_POINTS) for _ in range(N)]
    trajectories = []
    for i in range(N):
        num_points = num_points_list[i] if i < len(num_points_list) else random.randint(MIN_NB_POINTS, MAX_NB_POINTS)
        trajectory = generate_trajectory(i, num_points)
        trajectories.append(trajectory)
    return trajectories

def save_trajectories_to_file(trajectories, filename):
    """Save the generated trajectories to a file."""
    with open(filename, 'w') as file:
        for trajectory in trajectories:
            file.write(trajectory + "\n")

if __name__ == "__main__":
    trajectories = generate_trajectories(N)
    save_trajectories_to_file(trajectories, FILENAME)

    print(f"Trajectories generated and saved to '{FILENAME}'.")
