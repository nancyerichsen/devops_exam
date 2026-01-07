import os
import shutil
import tempfile
import time
import pytest
from project import create_app


def safe_rmtree(path):
    for _ in range(10):
        try:
            shutil.rmtree(path)
            return
        except PermissionError:
            time.sleep(1)

@pytest.fixture
def app():
    upload_dir = "/tmp/test_uploads"
    os.makedirs(upload_dir, exist_ok=True)

    # Create a temp dir for test databases
    temp_db_dir = tempfile.mkdtemp()
    original_db_dir = os.path.join(os.path.dirname(__file__), "../project/database_file")

    for db_name in ["users.db", "notes.db", "images.db"]:
        shutil.copyfile(
            os.path.join(original_db_dir, db_name),
            os.path.join(temp_db_dir, db_name)
        )


    app = create_app({
    "TESTING": True,
    "UPLOAD_FOLDER": upload_dir,
    "TEST_DB_DIR": temp_db_dir,
})

    yield app

    # Clean up the upload directory after tests
    for f in os.listdir(upload_dir):
        os.remove(os.path.join(upload_dir, f))
    os.rmdir(upload_dir)

    # Clean up the temporary database directory after tests
    safe_rmtree(temp_db_dir)

# Uses for testing routes and endpoints
@pytest.fixture
def client(app):
    return app.test_client()

# Used for testing CLI commands
@pytest.fixture
def runner(app):
    return app.test_cli_runner()