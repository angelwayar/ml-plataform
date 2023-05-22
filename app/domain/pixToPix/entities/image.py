import copy
from datetime import datetime
from typing import Any, Callable

from app.domain.pixToPix.entities.image_command import ImageUpdateCommand


class ImageEntity:
    def __init__(
            self,
            id: int | None,
            owner_id: int | None,
            image_base: str,
            created_at: datetime | None = None,
            update_at: datetime | None = None,
            is_deleted: bool | None = False
    ):
        self.id = id
        self.owner_id = owner_id
        self.image_base = image_base
        self.created_at = created_at
        self.update_at = update_at
        self.is_deleted = is_deleted

    def update_entity(
            self,
            entity_update_model: 'ImageUpdateCommand',
            get_update_data_fn: Callable[['ImageUpdateCommand'], dict[str, Any]]
    ) -> 'ImageEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'ImageEntity':
        if self.is_deleted:
            raise
        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity
