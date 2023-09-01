import os
import subprocess

output_file_path = "robocop_output.txt"

# Delete the old output file (if it exists)
if os.path.exists(output_file_path):
    os.remove(output_file_path)

# Get the current working directory
current_dir = os.getcwd()

def run_robocop_on_directory(directory):
    with open(output_file_path, "a") as output_file:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".robot"):
                    robot_file_path = os.path.join(root, filename)
                    
                    robocop_command = ["robocop", "--reports", "timestamp,all", robot_file_path]
                    robocop_output = subprocess.run(robocop_command, capture_output=True, text=True, check=False)
                    
                    output_file.write(robocop_output.stdout + "\n" + robocop_output.stderr + "\n")
                    output_file.write("-" * 80 + "\n\n")
                    
                    print(f"Robocop check completed for {robot_file_path}")

# Perform Robocop checks on the current directory and its subdirectories
run_robocop_on_directory(current_dir)

# Perform Robocop checks on all subdirectories within the current directory
for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    if os.path.isdir(item_path):
        run_robocop_on_directory(item_path)

print(f"All Robocop checks completed. Output saved in {output_file_path}")
