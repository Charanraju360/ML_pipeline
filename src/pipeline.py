from prefect import flow, task
import subprocess

# Step 1: run preprocess
@task
def run_preprocess():
    print("Running preprocess...")
    subprocess.run([r"C:\Users\Charan\endtoend\.venv\Scripts\python.exe", "src/preprocess.py"], check=True)

# Step 2: run training
@task
def run_train():
    print("Running training...")
    subprocess.run([r"C:\Users\Charan\endtoend\.venv\Scripts\python.exe", "src/train.py"], check=True)

# Main flow
@flow
def ml_pipeline():
    run_preprocess()
    run_train()

if __name__ == "__main__":
    ml_pipeline()