class UserEntity:
    def __init__(
        self,
        id: int | None,
        username: str,
        password: str
    ):
        self.id = id
        self.username = username
        self.password = password
        
