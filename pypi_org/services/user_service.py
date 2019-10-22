import final.pypi_org.data.db_session as db_session
from final.pypi_org.data.users import User


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()
