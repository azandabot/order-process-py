from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Order
import requests

def index(request):
    # Fetch data from the API
    api_url = "https://dummyjson.com/products"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        products = data.get("products", [])
        context = {"products": products}
        return render(request, 'index.html', context)
    else:
        # Handle API request failure
        error_message = f"Failed to fetch data from API. Status code: {response.status_code}"
        context = {"error_message": error_message}
        return render(request, 'error.html', context)
    
def add_to_products(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title', '')
        product_description = request.POST.get('product_description', '')
        product_price = request.POST.get('product_price', '')

        try:
            # Add your logic to save the product to the database (similar to what you did in the index view)
            # If there's an error, raise an exception
            # For example:
            product = Product(name=product_title, price=product_price, description=product_description)
            product.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error_message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'error_message': 'Invalid request method'})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        customer_name = request.POST.get('customer_name', '')
        address = request.POST.get('address', '')

        order = Order(product=product, quantity=quantity, customer_name=customer_name, address=address)
        order.save()

        return redirect('order_list')

    return render(request, 'order_create.html', {'product': product})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
