
NEW_STOP_WORDS = ['of', 'the']

def test_get_stop_words_default(empty_index):
    """Tests getting stop words by default."""
    response = empty_index().get_stop_words()
    assert isinstance(response, object)
    assert response == []

def test_update_stop_words(empty_index):
    """Tests updating the stop words."""
    index = empty_index()
    response = index.update_stop_words(NEW_STOP_WORDS)
    assert isinstance(response, object)
    assert 'updateId' in response
    update = index.wait_for_pending_update(response['updateId'])
    assert update['status'] == 'processed'
    response = index.get_stop_words()
    assert isinstance(response, object)
    for stop_word in NEW_STOP_WORDS:
        assert stop_word in response

def test_reset_stop_words(empty_index):
    """Tests resetting the stop words."""
    index = empty_index()
    # Update the settings first
    response = index.update_stop_words(NEW_STOP_WORDS)
    update = index.wait_for_pending_update(response['updateId'])
    assert update['status'] == 'processed'
    # Check the settings have been correctly updated
    response = index.get_stop_words()
    assert isinstance(response, object)
    for stop_word in NEW_STOP_WORDS:
        assert stop_word in response
    # Check the reset of the settings
    response = index.reset_stop_words()
    assert isinstance(response, object)
    assert 'updateId' in response
    update = index.wait_for_pending_update(response['updateId'])
    assert update['status'] == 'processed'
    response = index.get_stop_words()
    assert response == []
