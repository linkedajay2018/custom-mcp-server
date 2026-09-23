import server


def test_add():
    assert server.add(2, 3) == 5
    assert server.add(-1, 1) == 0


def test_save_note():
    server.NOTES.clear()
    result = server.save_note("Groceries", "Buy milk and eggs")
    assert "Groceries" in result
    assert "Total notes: 1" in result
    assert server.NOTES[0]["title"] == "Groceries"


def test_search_notes_finds_match():
    server.NOTES.clear()
    server.save_note("Groceries", "Buy milk and eggs")
    server.save_note("Workout", "Run 5k")
    result = server.search_notes("milk")
    assert "Groceries" in result
    assert "Workout" not in result


def test_search_notes_no_match():
    server.NOTES.clear()
    server.save_note("Groceries", "Buy milk and eggs")
    result = server.search_notes("nonexistent")
    assert "No notes found" in result
