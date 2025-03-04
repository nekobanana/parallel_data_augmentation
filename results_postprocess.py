import os
import json
import matplotlib.pyplot as plt


def read_experiment_results(folder, base_filename):
    results = {}

    for file in os.listdir(folder):
        if file.startswith(base_filename) and file.endswith(".txt"):
            filepath = os.path.join(folder, file)
            with open(filepath, "r") as f:
                data = json.load(f)
                num_proc = data["num_processes"]
                results[num_proc] = data["time"]

    return dict(sorted(results.items()))


def plot_results(results, output_folder, base_filename):
    num_processes = list(results.keys())
    times = list(results.values())

    plt.figure(figsize=(8, 5))
    plt.scatter(num_processes, times, color='dodgerblue', label='Execution Time')
    for i, txt in enumerate(times):
        plt.text(num_processes[i], times[i], f"{txt:.2f}", ha='left', va='bottom')
        plt.vlines(num_processes[i], ymin=0, ymax=times[i], linestyles='dashed', colors='gray')
    plt.xticks(num_processes)
    plt.xlabel("Number of processes")
    plt.ylabel("Execution time (s)")
    plt.title("Execution time")
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(output_folder, f"{base_filename}_execution_time.png"))
    plt.show()

    base_time = times[0]
    speedups = [base_time / t for t in times]

    plt.figure(figsize=(8, 5))
    plt.scatter(num_processes, speedups, color='orange', label='Speedup')
    for i, txt in enumerate(speedups):
        plt.text(num_processes[i], speedups[i], f"{txt:.2f}", ha='left', va='bottom')
        plt.vlines(num_processes[i], ymin=0, ymax=speedups[i], linestyles='dashed', colors='gray')
    plt.xticks(num_processes)
    plt.xlabel("Number of processes")
    plt.ylabel("Speedup")
    plt.title("Speedup")
    plt.grid()
    plt.legend()
    plt.savefig(os.path.join(output_folder, f"{base_filename}_speedup.png"))
    plt.show()


if __name__ == "__main__":
    folder = "./results"
    base_filename = "parallel_trans"
    # base_filename = "parallel_images"
    output_folder = "./plots"
    os.makedirs(output_folder, exist_ok=True)

    results = read_experiment_results(folder, base_filename)
    plot_results(results, output_folder, base_filename)