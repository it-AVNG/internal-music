"""
Tests where the Session created performed as intended
"""
from src.mod.session import Session

def test_create_session():
    """Test if created session has diatones and strings attributes"""
    session = Session()
    assert session.diatones == ["C", "D", "E", "F", "G", "A", "B"]
    assert session.gstrings == ["1", "2", "3", "4", "5", "6"] 
