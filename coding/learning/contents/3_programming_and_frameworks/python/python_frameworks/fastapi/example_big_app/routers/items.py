from dependencies import get_token_header
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/items",  # tất cả các router khi chạy ở main đều có path đứng đầu là "items"
    tags=["items"],  # tất cả các config đều có tag là items
    dependencies=[Depends(get_token_header)],  # Extra responses
    responses={
        404: {"description": "Not found"}
    },  # they all need that X-Token dependency we created.
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],  # add more tags
    responses={
        403: {"description": "Operation forbidden"}
    },  # add more responses
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
