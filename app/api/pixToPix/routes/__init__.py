from fastapi import APIRouter

router_pix_to_pix = APIRouter(
    prefix='/image',
    tags=['pix_to_pix']
)
