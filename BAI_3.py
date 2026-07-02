from fastapi import FastAPI,Query
from typing import Optional

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def search_student_by_name(
    keyword:Optional[str] = Query(None), 
    max_price :Optional[int]= Query(None)):

    if max_price is not None and max_price < 0:
        return{
            "detail": "max_price không được âm"
        }

    display_result = []
    for product in products:
        is_match = True        
        if keyword and keyword.strip():
            if keyword.strip().lower() not in product["name"].lower():
                is_match = False
                
        if max_price is not None:
            if product["price"] > max_price:
                is_match = False

        if is_match:
            display_result.append(product)
    

    if len(display_result) == 0:
        return{
            "message" : "Không có kết quả nào",
            "data" : []
        }
    else:
        return {
            "data" : display_result
        }
    
    
#input - một danh sách các sản phẩm  , tham số truy vấn người dungf
# keyword , max_price

#output - kết quả tìm thấy 

# giải pháp 
# dùng kỹ thuật lọc dồn 

#1. tiếp nhận validate -> tiền xử lý dữ liệu -> lọc danh sách -> tả è kết quả