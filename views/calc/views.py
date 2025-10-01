from fastapi import APIRouter, Depends
from .schemas import MultyCalc
router = APIRouter(prefix="/calc", tags=["Calc"])


@router.get("/")
def calc(a: int, b: int):
    return {
        "a": a, "b": b, "result": a + b
    }


@router.get("//multy")
def multy_calc(multy: MultyCalc = Depends(MultyCalc)):

    return {
        "multy": multy.model_dump(),
        "result": multy.a + multy.b
    }


@router.post("/add")
def calc_add(data: MultyCalc):
    result = data.model_dump()
    return {'result': result}