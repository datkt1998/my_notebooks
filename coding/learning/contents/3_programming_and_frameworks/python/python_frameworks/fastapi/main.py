from enum import Enum
from typing import Annotated, Literal

from fastapi import Body, FastAPI, Header, HTTPException, Path, Query
from pydantic import BaseModel, Field

fake_secret_token = "coneofsilence"
fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

# create a FastAPI "instance"
app = FastAPI()


# create a route theo cấu trúc @app.<operation>(path)
@app.get("/")
async def root():
    return {"message": "Hello World"}


### Parameters Path: parameter in path
@app.get("/items_path1/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# testcase: http://127.0.0.1:8000/items/foo


### Parameters Path: parameter validation
@app.get("/items_path2/{item_id}")
async def read_item_validation(item_id: Annotated[str, Field(max_length=5)]):
    return {"item_id": item_id}


# testcase: http://127.0.0.1:8000/items/foofoofoo ----> error


### Parameters Path: Pre-defined parameters value
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # check model name in ModelName
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # or get value from arguments
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# testcase: http://127.0.0.1:8000/models/alexnet ---> Oke
# testcase: http://127.0.0.1:8000/models/lenaddd ---> Error


### Parameters Path: path in parameters
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# testcase: http://127.0.0.1:8000/files/documents/test.txt


### Parameters Path: multiple path parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
):
    item = {"item_id": item_id, "owner_id": user_id}
    return item


# testcase: http://127.0.0.1:8000/users/1/items/foo


### Parameters Query: query parameters with boolean type
@app.get("/items_v2/{item_id}")
async def read_value(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item


# testcase: http://127.0.0.1:8000/items/foo?short=1    ----> short = True
# testcase: http://127.0.0.1:8000/items/foo?short=True ----> short = True
# testcase: http://127.0.0.1:8000/items/foo?short=true ----> short = True
# testcase: http://127.0.0.1:8000/items/foo?short=no  ---> short = False
# testcase: http://127.0.0.1:8000/items/foo?short=yes ---> short = True


### Parameters Query: use `Query` to add metadata for `Annotated`
@app.get("/read_items_query_validation/")
async def read_items_query_validation(
    q: Annotated[str | None, Query(min_length=3, max_length=5)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# testcase: http://127.0.0.1:8000/items/?q=foo ----> Oke
# testcase: http://127.0.0.1:8000/items/?q=fooooo ----> Error


### Parameters Query: use `...` mark as the required value
@app.get("/required_items/")
async def read_required_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# testcase: http://127.0.0.1:8000/required_items/ ----> Error


### Parameters Query: Query parameter is list / multiple values
@app.get("/items_list/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


# testcase: http://127.0.0.1:8000/items_list/?q=foo&q=bar


### Parameters Query: use `alias` as an alias for `Query`
@app.get("/items_alias/")
async def read_items_alias(
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# testcase: http://127.0.0.1:8000/items_alias/?item-query=foo


### Parameters Query: define the query parameter with pydantic model
class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

    # set config for not allow unknown field
    model_config = {"extra": "forbid"}


@app.get("/read_items_pydantic/")
async def read_items_pydantic(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


# testcase: http://127.0.0.1:8000/items/?limit=10&tags=foo&tags=bar ---> Success
# testcase: http://127.0.0.1:8000/items/?order_by=deleted_at ---> Error


### Parameters Body | POST: use pydantic model (as request body) + path + query parameters
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items_pydantic/{item_id}/")
async def create_item_pydantic_model(
    item_id: int, item: Item, q: str | None = None
):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    result = {"item_id": item_id, **item_dict}
    if q:
        result.update({"q": q})
    return result


# testcase: http://127.0.0.1:8000/items_pydantic/1/?q=foo header:Content-Type=application/json name=dat description=dat price=15.0 tax=2.0

### Parameters Path: define Path parameter with Annotated + Path


@app.get("/read_items_path_annotated/{item_id}")
async def read_items_path_annotated(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# testcase: http://127.0.0.1:8000/items/foo?item-query=dat


### Parameters Body | PUT: multiple body parameters
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.post("/items_multiple_body/{item_id}")
async def update_items_multiple_body(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# testcase: http://127.0.0.1:8000/items/1/?q=foo header:Content-Type=application/json name=dat description=dat price=15.0 tax=2.0


### Parameters Body | POST: emmbed body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items_embed_body/{item_id}")
async def update_items_embed_body(
    item_id: int,
    item: Annotated[Item, Body(embed=True)],
    user: Annotated[User, Body(embed=True)],
    importance: Annotated[int, Body(embed=True)],
):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance,
    }
    return results


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=409, detail="Item already exists")
    fake_db[item.id] = item
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
