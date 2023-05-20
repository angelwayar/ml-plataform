class ImageEntity:
    def __init__(
            self,
            id: int | None,
            owner_id: int | None,
            image_base: str
    ):
        self.id = id
        self.owner_id = owner_id
        self.image_base = image_base
