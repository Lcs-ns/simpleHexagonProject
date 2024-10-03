from app.src.entities.userEntity import User
from app.src.exceptions import userExeption
import hashlib

class SignUpUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user: User):
        if self.user_repository.exists_by_email(user.email):
            raise userExeption(f"User with email {user.email} already exists")

        hashed_password = self.hash_password(user.password)
        user.password = hashed_password

        self.user_repository.save(user)

    def hash_password(self, password: str) -> str:
        hashed_pass = password
        hash_str = hashlib.sha256()
        hash_str.update(hashed_pass)
        return hashed_pass
    
