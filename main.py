"""
1.khi gọi get/products/1 báo lỗi 404 vì hiện tại điểm endpoint đó chỉ đang khai báo là tên chứ không phải là một tham số truyền vào
2.dòng @app.get đang khai báo sai path parameter
3.vì nó không phải là một tham số truyền vào mà chỉ là một tên endpoint 
4.endpoint cần sửa đúng là phần product_id thành {product_id}
"""
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 350000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]
@app.get("/products/{product_id}")
def get_product_detail(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Không tìm thấy sản phẩm"
    }