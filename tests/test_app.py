from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    participant = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{participant}")

    assert response.status_code == 200
    assert participant not in response.json()["participants"]
    assert participant not in client.get("/activities").json()[activity_name]["participants"]
