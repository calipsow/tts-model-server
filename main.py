from server_api.server import run_server_api
import subprocess


def run_setup():
    try:
        # Define the command you want to execute
        command = ["python", "setup.py", "install"]

        # Use subprocess.run to execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            print("initial tts setup done")
            # print("Output:", result.stdout)
        else:
            print("Error installing setup.py")
            print("Error:", result.stderr)
    except Exception as e:
        print(f"failed to run setup {e}")


if __name__ == "__main__":
    run_setup()
    run_server_api()
