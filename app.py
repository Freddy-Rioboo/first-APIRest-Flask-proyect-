from flask import Flask, jsonify, request, json 
from products import guitars


app = Flask(__name__)

@app.route('/')
def main():
    return "welcome to the main page"

#Showing all products available on the database.
@app.route('/products')
def get_guitars():
    return jsonify({"products": guitars, "message": "list of Guitars available"})

# Choosing a product by id.
@app.route('/products/<int:guitar_id>')
def get_guitar(guitar_id):
    result = [guitar for guitar in guitars if guitar['id'] == guitar_id]
    if len(result) > 0:
        return jsonify({"Guitar":result[0]})
    else:
        return({"message": "Product no found in database"})
    
#Choosing a product by model.
@app.route("/products//model/<string:guitar_model>")
def get_guitar_model(guitar_model):
     result = [guitar for guitar in guitars if guitar["model"] == guitar_model]
     if len(result) > 0:
         return jsonify({"Guitar":result})
     else:
         return({"message": "Product no found in database"})

 # Choosing products by color.    
@app.route('/products/color/<string:guitar_color>')
def get_product_by_color(guitar_color):
    result = [guitar for guitar in guitars if guitar["color"] == guitar_color]
    if len(result) >0:
        return jsonify({"Guitar Color":result})
    else:
        return ({"message": "Product not found in database"})

# POST method to insert a new product.
@app.route('/products/insert-new', methods=['POST'])
def insert_new_product():
    if request.data:
        product_data = json.loads(request.data)
       	
        new_id = max([guitar['id'] for guitar in guitars])+1
        model = product_data["model"]
        brand = product_data["brand"]
        color = product_data["color"]
        new_product = {
            "id": new_id,
            "model": model,
            "brand": brand,
            "color": color
     	}
        guitars.append(new_product)
        return jsonify({"message":"product added succesfully","Current Products": new_product}), 200
    else:
        return "400 Bad Request",400
    
# Choosing by name to update a product.
@app.route('/products/update/<int:guitar_id>', methods=['PUT'])
def update_product(guitar_id):
    if request.data:
        product_data = json.loads(request.data)
    
        id = guitar_id
        model = product_data['model']
        brand = product_data['brand']
        color = product_data['color']
        
        product_updated = {
            "id": id,
            "model": model,
            "brand": brand,
            "color": color,
        }
        
        find_product = [product for product in guitars if product["id"] == guitar_id]
        if find_product:
            for i in range(len(guitars)):
                if guitars[i] == find_product:
                    guitars[i] = product_updated
            return jsonify({"message":"product updated successfully",
                        "Prouct detail": product_updated})
        else:
            return jsonify({"message": "Product not updated"})

# Choosing product to deleted it by name.
@app.route("/products/delete/<int:guitar_id>", methods=["DELETE"])
def delete_product(guitar_id):
    guitar = [product for product in guitars if product["id"] == guitar_id]
    if len(guitar) > 0:
        guitars.remove(guitar[0])
        return jsonify({"message": "product deleted successfully"})
    
    return jsonify({"message": "product not deleted"})



if __name__ == '__main__':
    app.run(debug=True)
