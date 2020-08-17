from dto.user_dto import UserDto


def get_users():
    return []


def get_user_by_name(user_name):
    return user_name


def create_user(json):
    user_dto = UserDto(json['lastname'], json['firstname'],
                       json['birth'], json['email'], json['login'], json['password'])
    return user_dto


def update_user(user_id, json):
    user_dto = UserDto(json['lastname'], json['firstname'],
                       json['birth'], json['email'], json['login'], json['password'])
    return user_id


def delete_user(user_id):
    return user_id
