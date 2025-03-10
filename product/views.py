import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

from category.models import CategoryVO
from product.models import ProductVO
from subcategory.models import SubCategoryVO

IMAGE_UPLOAD_PATH = os.path.join(settings.BASE_DIR, 'static', 'product_image')

def admin_load_product(request):
    category_vo_lst = CategoryVO.objects.filter(is_deleted=False)
    subcategory_vo_lst = SubCategoryVO.objects.filter(is_deleted=False)
    print(category_vo_lst)  # Debugging line
    print(subcategory_vo_lst)
    return render(request, 'admin/product_templates/addProduct.html',
                  {'category_vo_lst': category_vo_lst,
                   'subcategory_vo_lst': subcategory_vo_lst})


def admin_load_ajax(request):
    product_category_id = request.GET.get('product_category_id')

    subcategories = SubCategoryVO.objects.filter(
        subcategory_category_vo_id=product_category_id,  # Corrected field
        is_deleted=False
    )

    subcategory_list = [{'subcategory_id': subcategory.subcategory_id,
                         'subcategory_name': subcategory.subcategory_name}
                        for subcategory in subcategories]

    print("Fetched subcategories:", subcategory_list)  # Debugging line

    return JsonResponse(subcategory_list,
                        safe=False)  # Returning JSON response


def admin_insert_product(request):
    if request.method == 'POST' and request.FILES.get('product_image'):
        product_name = request.POST.get('productName')
        product_description = request.POST.get('productDescription')
        product_price = request.POST.get('productPrice')
        product_quantity = request.POST.get('productQuantity')
        product_category_id = request.POST.get('product_category_id')
        product_subcategory_id = request.POST.get('product_subcategory_id')

        product_image = request.FILES['product_image']

        if not os.path.exists(IMAGE_UPLOAD_PATH):
            os.makedirs(IMAGE_UPLOAD_PATH,
                        exist_ok=True)  # Use exist_ok=True to avoid errors

        image_save_path = os.path.join(IMAGE_UPLOAD_PATH, product_image.name)
        with open(image_save_path, 'wb+') as destination:
            for chunk in product_image.chunks():
                destination.write(chunk)

        product_vo = ProductVO(
            product_name=product_name,
            product_description=product_description,
            product_price=product_price,
            product_quantity=product_quantity,
            product_image_name=product_image.name,  # Only the file name
            product_image_path=os.path.join('static', 'product_image',
                                            product_image.name),
            # Relative path
            product_category_id=CategoryVO.objects.get(
                category_id=product_category_id),
            product_subcategory_id=SubCategoryVO.objects.get(
                subcategory_id=product_subcategory_id),
        )
        product_vo.save()

        # Redirect to the product view page to refresh the list
        return redirect('admin_view_product')

    return render(request, 'admin/product_templates/addProduct.html')


def admin_view_product(request):
    product_vo_lst = ProductVO.objects.filter(is_deleted=False)
    print(f"Products with is_deleted=False: {len(product_vo_lst)}")
    return render(request, 'admin/product_templates/viewProduct.html',
                  {'product_vo_lst': product_vo_lst})


def admin_delete_product(request):
    product_id = request.POST.get('product_id')
    product_vo = ProductVO.objects.get(product_id=product_id, is_deleted=False)
    product_vo.is_deleted = True
    product_vo.save()
    return redirect('admin_view_product')


def admin_edit_product(request, product_id):
    product_vo_lst = ProductVO.objects.get(product_id=product_id)
    category_vo_lst = CategoryVO.objects.filter(is_deleted=False)

    # Get subcategories based on the selected category of the product
    sub_category_vo_lst = SubCategoryVO.objects.filter(
        subcategory_category_vo=product_vo_lst.product_category_id,
        is_deleted=False
    )

    return render(request, 'admin/product_templates/updateProduct.html', {
        'product_vo_lst': product_vo_lst,  # Pass the product for use in the template
        'category_vo_lst': category_vo_lst,
        'sub_category_vo_lst': sub_category_vo_lst
    })


def admin_update_product(request, product_id):
    if request.method == 'POST':
        product_vo = ProductVO.objects.get(product_id=product_id,
                                           is_deleted=False)

        # Update product fields
        product_vo.product_name = request.POST.get('productName')
        product_vo.product_description = request.POST.get('productDescription')
        product_vo.product_price = request.POST.get('productPrice')
        product_vo.product_quantity = request.POST.get('productQuantity')

        # Update category and subcategory
        product_category_id = request.POST.get('product_category_id')
        product_subcategory_id = request.POST.get('product_subcategory_id')

        product_vo.product_category_id = CategoryVO.objects.get(
            category_id=product_category_id)
        product_vo.product_subcategory_id = SubCategoryVO.objects.get(
            subcategory_id=product_subcategory_id)

        # Handle new image upload
        if 'productImage' in request.FILES:
            product_image = request.FILES['productImage']

            # Ensure upload directory exists
            if not os.path.exists(IMAGE_UPLOAD_PATH):
                os.makedirs(IMAGE_UPLOAD_PATH, exist_ok=True)

            image_save_path = os.path.join(IMAGE_UPLOAD_PATH,
                                           product_image.name)
            with open(image_save_path, 'wb+') as destination:
                for chunk in product_image.chunks():
                    destination.write(chunk)

            # Update product image fields
            product_vo.product_image_name = product_image.name
            product_vo.product_image_path = os.path.join('static',
                                                         'product_image',
                                                         product_image.name)

        product_vo.save()  # Save updated product details

        return redirect('admin_view_product')

    else:
        product_vo = ProductVO.objects.get(product_id=product_id)
        category_vo_lst = CategoryVO.objects.filter(is_deleted=False)
        sub_category_vo_lst = SubCategoryVO.objects.filter(
            subcategory_category_vo=product_vo.product_category_id,
            is_deleted=False
        )

        return render(request, 'admin/product_templates/updateProduct.html', {
            'product_vo': product_vo,
            'category_vo_lst': category_vo_lst,
            'sub_category_vo_lst': sub_category_vo_lst
        })
