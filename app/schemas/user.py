from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
import string


class BaseUser(BaseModel):
    username: str


class Password(BaseModel):
    new_password: str

    @validator("new_password", always=True)
    def password_validation(cls, value):
        rules = [
            lambda s: any(x.isdigit() for x in s),  # must have at least one digit
            lambda s: len(s.strip())
            == len(s),  # no whitespaces at the beginning and at the end of the string
            lambda s: len(s) >= 12,  # must be at least 12 characters
            lambda s: any(
                x in string.punctuation for x in s
            ),  # must be at least one symbol
        ]

        if not all(rule(value) for rule in rules):
            msg = " must contain 12 characters, at least 1 number, 1 symbol and without spaces at the beginning and at the end of the password"
            raise ValueError(msg)

        return value


class RegisterUser(BaseUser, Password):
    email: EmailStr
    referal_code: str


class CreateUser(BaseUser, Password):
    email: EmailStr
    referal_user_id: Optional[int]


class LoginUser(BaseUser):
    password: str


class UpdateUser(BaseUser):
    email: EmailStr


class ResponseUser(BaseUser):
    email: EmailStr


class ResponseUserRefers(BaseModel):
    users: List[ResponseUser]
