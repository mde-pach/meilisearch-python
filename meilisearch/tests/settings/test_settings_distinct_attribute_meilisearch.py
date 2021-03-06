

NEW_DISTINCT_ATTRIBUTE = 'title'
DEFAULT_DISTINCT_ATTRIBUTE = None

def test_get_distinct_attribute(empty_index):
    """Tests geting the distinct attributes"""
    response = empty_index().get_distinct_attribute()
    assert isinstance(response, object)
    assert response == DEFAULT_DISTINCT_ATTRIBUTE

def test_update_distinct_attribute(empty_index):
    """Tests creating a custom distinct attribute and checks it has been set correctly"""
    index = empty_index()
    response = index.update_distinct_attribute(NEW_DISTINCT_ATTRIBUTE)
    assert isinstance(response, object)
    assert 'updateId' in response
    index.wait_for_pending_update(response['updateId'])
    response = index.get_distinct_attribute()
    assert isinstance(response, object)
    assert response == NEW_DISTINCT_ATTRIBUTE

def test_reset_distinct_attribute(empty_index):
    """Tests resetting distinct attribute"""
    index = empty_index()
    # Update the settings first
    response = index.update_distinct_attribute(NEW_DISTINCT_ATTRIBUTE)
    update = index.wait_for_pending_update(response['updateId'])
    assert update['status'] == 'processed'
    # Check the settings have been correctly updated
    response = index.get_distinct_attribute()
    assert isinstance(response, object)
    assert response == NEW_DISTINCT_ATTRIBUTE
    # Check the reset of the settings
    response = index.reset_distinct_attribute()
    assert isinstance(response, object)
    assert 'updateId' in response
    index.wait_for_pending_update(response['updateId'])
    response = index.get_distinct_attribute()
    assert response == DEFAULT_DISTINCT_ATTRIBUTE
