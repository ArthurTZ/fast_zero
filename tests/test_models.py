from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.models import User


def test_create_user(session: Session):
    user = User(username='arthur', password='123', email='testes@example.com')
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'testes@example.com')
    )
    assert result.username == 'arthur'
