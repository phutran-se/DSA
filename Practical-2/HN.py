import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Number of disks for simulation (You can modify this value)
num_disks = 3

# Pegs represented as lists (Stacks)
pegs = {1: list(range(num_disks, 0, -1)), 2: [], 3: []}
moves = []

def hanoi(n, src, aux, dest):
    """Recursive function to generate moves for Towers of Hanoi."""
    if n == 1:
        moves.append((src, dest))
        return
    hanoi(n - 1, src, dest, aux)
    moves.append((src, dest))
    hanoi(n - 1, aux, src, dest)

# Generate moves
hanoi(num_disks, 1, 2, 3)

# Matplotlib Figure and Axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 4)
ax.set_ylim(0, num_disks + 3)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["Peg 1", "Peg 2", "Peg 3"])
ax.set_title("Towers of Hanoi Visualization")

# Create pegs
peg_width = 0.1
peg_height = num_disks + 2
for i in range(1, 4):
    ax.add_patch(patches.Rectangle((i - peg_width / 2, 0), peg_width, peg_height, color="black"))

# Disk Objects
disk_patches = []
disk_colors = plt.cm.viridis_r(range(num_disks))  # Use color gradient
for i, disk_size in enumerate(pegs[1]):
    rect = patches.Rectangle((1 - disk_size / 10, i + 1), disk_size / 5, 0.8, color=disk_colors[i])
    ax.add_patch(rect)
    disk_patches.append(rect)

def update(frame):
    """Animation update function to move disks."""
    if frame >= len(moves):
        return
    src, dest = moves[frame]
    disk = pegs[src].pop()
    pegs[dest].append(disk)

    # Update disk positions
    for peg in range(1, 4):
        for j, disk in enumerate(pegs[peg]):
            disk_patches[disk - 1].set_xy((peg - disk / 10, j + 1))

ani = animation.FuncAnimation(fig, update, frames=len(moves), interval=800, repeat=False)

# Display the animation
plt.show()
