import io

from fastapi import status, Depends, HTTPException, File, UploadFile
from fastapi.responses import Response

from app.api.pixToPix.routes import router_pix_to_pix
from app.dependencies import (
    get_create_image_use_case,
    get_images_use_case,
    get_image_use_case,
    get_update_image_use_case,
    get_delete_image_use_case,
    get_improve_image_rain_use_case,
)
from app.domain.pixToPix.entities.image_command import ImageCommand, ImageUpdateCommand
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.usecases.create_image_use_case import CreateImageUseCase
from app.domain.pixToPix.usecases.delete_image_use_case import DeleteImageUseCase
from app.domain.pixToPix.usecases.get_image_use_case import GetImageUseCase
from app.domain.pixToPix.usecases.get_images_use_case import GetImagesUseCase
from app.domain.pixToPix.usecases.improve_the_image_of_rain_use_case import ImproveImageRainUseCase
from app.domain.pixToPix.usecases.update_image_use_case import UpdateImageUseCase


@router_pix_to_pix.post(
    '/',
    response_model=ImageResult,
    status_code=status.HTTP_201_CREATED,
)
def create_image(
        data: ImageCommand,
        create_image_use_case: CreateImageUseCase = Depends(get_create_image_use_case),
):
    try:
        result = create_image_use_case((data,))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return ImageResult(
        id=result.id,
        image=result.image,
        is_deleted=result.is_deleted,
    )


@router_pix_to_pix.get(
    '/',
    response_model=list[ImageResult],
    status_code=status.HTTP_200_OK,
)
def get_images(
        images_use_case: GetImagesUseCase = Depends(get_images_use_case)
):
    try:
        images = images_use_case(None)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not images:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return images


@router_pix_to_pix.get(
    '/{id}/',
    response_model=ImageResult,
    status_code=status.HTTP_200_OK,
)
def get_image(
        id: int,
        image_use_case: GetImageUseCase = Depends(get_image_use_case)
):
    try:
        image = image_use_case((id,))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return image


@router_pix_to_pix.put(
    '/{id}/',
    response_model=ImageResult,
    status_code=status.HTTP_200_OK,
)
async def update_image(
        id: int,
        data: ImageUpdateCommand,
        update_image_use_case: UpdateImageUseCase = Depends(get_update_image_use_case)
):
    try:
        image = update_image_use_case((id, data))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return image


@router_pix_to_pix.delete(
    '/{id}/',
    response_model=ImageResult,
    status_code=status.HTTP_200_OK,
)
def delete_image(
        id: int,
        delete_image_use_case: DeleteImageUseCase = Depends(get_delete_image_use_case)
):
    try:
        image = delete_image_use_case((id,))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return image


@router_pix_to_pix.post('/image/')
async def upload_image(
        file: UploadFile = File(...),
        improve_image_rain_use_case: ImproveImageRainUseCase = Depends(get_improve_image_rain_use_case)
):
    try:
        img_byte_arr = io.BytesIO()
        result = improve_image_rain_use_case((file,))
        result.save(img_byte_arr, format='JPEG')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return Response(content=img_byte_arr.getvalue(), media_type="image/png")
