from fastmcp import FastMCP
import mlflow

mcp = FastMCP("experiment_tracker")

@mcp.tool
def log_runs():
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("experiment_runs")

    for i in range(3):
        with mlflow.start_run():
            mlflow.log_param("lr", 0.01 * (i + 1))
            mlflow.log_metric("accuracy", 0.8 + i * 0.05)

    print("Logging 3 runs completed.")

if __name__ == "__main__":
    log_runs()