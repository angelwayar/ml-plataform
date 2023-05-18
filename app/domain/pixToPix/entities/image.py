class ImageEntity:
    def __init__(
            self,
            id: int | None,
            user_id: int | None,
            image_base: str
    ):
        self.id = id
        self.user_id = user_id
        self.image_base = image_base
