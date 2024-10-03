from app.src.entities.userEntity import User
from app.infrastructure.db.models import UserModel
from app.src.entities.userEntity import User

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def exists_by_email(self, email: str) -> bool:
        return self.db_session.query(UserModel).filter(UserModel.email == email).first() is not None
    
    def save(self, user: User):
        db_user = UserModel(
            username=user.username,
            email=user.email,
            password=user.password
        )

        self.db_session.add(db_user)
        self.db_session.commit()
        self.db_session.refresh(db_user)