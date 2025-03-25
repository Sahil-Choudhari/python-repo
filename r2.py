import matplotlib.pyplot as plt

o = [i for i in range(1, 21)]  # Overs (1 to 20)
runs = [i * 10 for i in range(1, 21)]  # Runs scored in each over (multiples of 10)
wickets = [0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1]  # Wickets fell in each over

plt.figure(figsize=(10, 5))

# Plot runs per over
plt.plot(o, runs, marker="D", linestyle="-", color="b", label="Runs per over")

# Mark wickets with red dots
for over, wk in zip(o, wickets):
    for _ in range(wk):
        plt.scatter(over, 0, color="red", marker="o", s=50)

plt.xlabel("Overs")
plt.ylabel("Runs")
plt.title("Runs per over with wickets marked")

# Set x-ticks at overs
plt.xticks(o)

# Add legend
plt.legend()

# Add grid with alpha transparency (light grid lines)
plt.grid(True, linestyle="--", alpha=0.6)

# Show the plot
plt.show()
