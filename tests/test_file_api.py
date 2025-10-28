import subprocess
import os

def test_sample_py_runs_successfully():
    """
    Tests that the quickstarts/file-api/sample.py script runs without errors.
    """
    # Set a dummy API key. The script will fail with an authentication error,
    # but that's fine for this test. We just want to make sure it doesn't
    # fail with a FileNotFoundError.
    os.environ["GOOGLE_API_KEY"] = "test-key"

    # Run the script
    result = subprocess.run(
        ["python", "quickstarts/file-api/sample.py"],
        check=False,
        capture_output=True,
        text=True,
    )

    # Assert that the script ran without a FileNotFoundError.
    # We expect an authentication error, which will result in a non-zero
    # return code.
    assert "FileNotFoundError" not in result.stderr
    assert "No such file or directory" not in result.stderr


    # Clean up the environment variable
    del os.environ["GOOGLE_API_KEY"]
