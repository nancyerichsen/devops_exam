import os
import shutil
import tempfile
import atexit
from project import create_app

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    temp_db_dir = tempfile.mkdtemp(prefix="playwright-db-")
    upload_dir = tempfile.mkdtemp(prefix="playwright-uploads-")

    # Cleanup hook
    @atexit.register
    def cleanup():
        print(f"Cleaning up test DB at {temp_db_dir} and upload dir at {upload_dir}")
        shutil.rmtree(temp_db_dir, ignore_errors=True)
        shutil.rmtree(upload_dir, ignore_errors=True)

    # Set up the test database directory
    original_db_dir = os.path.join(base_dir, "project", "database_file")
    for db_name in ["users.db", "notes.db", "images.db"]:
        shutil.copyfile(
            os.path.join(original_db_dir, db_name),
            os.path.join(temp_db_dir, db_name)
        )

    # Configure the app for testing
    app = create_app({
        "TESTING": True,
        "TEST_DB_DIR": temp_db_dir,
        "UPLOAD_FOLDER": upload_dir,  # Absolute path already from tempfile
    })

    app.run(debug=True, port=5001)
