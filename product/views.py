import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

from category.models import CategoryVO
from product.models import ProductVO
from subcategory.models import SubCategoryVO
from utils.custome_exception import AppServices
from utils.my_logger import get_logger

logger = get_logger()
IMAGE_UPLOAD_PATH = os.path.join(settings.BASE_DIR, 'static', 'product_image')


def admin_load_product(request):
    try:
        logger.info("Loading product form")
        category_vo_lst = CategoryVO.objects.filter(is_deleted=False)
        subcategory_vo_lst = SubCategoryVO.objects.filter(is_deleted=False)
        return render(request, 'admin/product_templates/addProduct.html',
                      {'category_vo_lst': category_vo_lst,
                       'subcategory_vo_lst': subcategory_vo_lst})
    except Exception as e:
        logger.error("Failed to load product form", exc_info=True)
        return AppServices.handle_exception("Failed to load product form", 500,
                                            e)


def admin_load_ajax(request):
    try:
        product_category_id = request.GET.get('product_category_id')
        logger.info(
            f"Fetching subcategories for category ID: {product_category_id}")
        subcategories = SubCategoryVO.objects.filter(
            subcategory_category_vo_id=product_category_id, is_deleted=False)
        subcategory_list = [{'subcategory_id': subcategory.subcategory_id,
                             'subcategory_name': subcategory.subcategory_name}
                            for subcategory in subcategories]
        return JsonResponse(subcategory_list, safe=False)
    except Exception as e:
        logger.error("Failed to load subcategories via AJAX", exc_info=True)
        return AppServices.handle_exception(
            "Failed to load subcategories via AJAX", 500, e)


def admin_insert_product(request):
    try:
        if request.method == 'POST' and request.FILES.get('product_image'):
            logger.info("Inserting new product")
            product_vo = ProductVO(
                product_name=request.POST.get('productName'),
                product_description=request.POST.get('productDescription'),
                product_price=request.POST.get('productPrice'),
                product_quantity=request.POST.get('productQuantity'),
                product_category_id=CategoryVO.objects.get(
                    category_id=request.POST.get('product_category_id')),
                product_subcategory_id=SubCategoryVO.objects.get(
                    subcategory_id=request.POST.get('product_subcategory_id')),
            )
            product_image = request.FILES['product_image']
            os.makedirs(IMAGE_UPLOAD_PATH, exist_ok=True)
            image_save_path = os.path.join(IMAGE_UPLOAD_PATH,
                                           product_image.name)
            with open(image_save_path, 'wb+') as destination:
                for chunk in product_image.chunks():
                    destination.write(chunk)
            product_vo.product_image_name = product_image.name
            product_vo.product_image_path = os.path.join('static',
                                                         'product_image',
                                                         product_image.name)
            product_vo.save()
            logger.info(
                f"Product '{product_vo.product_name}' inserted successfully")
            return redirect('admin_view_product')
        return render(request, 'admin/product_templates/addProduct.html')
    except Exception as e:
        logger.error("Failed to insert product", exc_info=True)
        return AppServices.handle_exception("Failed to insert product", 400, e)


def admin_view_product(request):
    try:
        logger.info("Fetching all products")
        product_vo_lst = ProductVO.objects.filter(is_deleted=False)
        return render(request, 'admin/product_templates/viewProduct.html',
                      {'product_vo_lst': product_vo_lst})
    except Exception as e:
        logger.error("Failed to view products", exc_info=True)
        return AppServices.handle_exception("Failed to view products", 400, e)


def admin_delete_product(request):
    try:
        product_vo = ProductVO.objects.get(
            product_id=request.POST.get('product_id'), is_deleted=False)
        product_vo.is_deleted = True
        product_vo.save()
        logger.info(f"Deleted product '{product_vo.product_name}'")
        return redirect('admin_view_product')
    except Exception as e:
        logger.error("Failed to delete product", exc_info=True)
        return AppServices.handle_exception("Failed to delete product", 400, e)


def admin_edit_product(request, product_id):
    try:
        logger.info(f"Loading edit form for product ID: {product_id}")
        product_vo = ProductVO.objects.get(product_id=product_id)
        category_vo_lst = CategoryVO.objects.filter(is_deleted=False)
        sub_category_vo_lst = SubCategoryVO.objects.filter(
            subcategory_category_vo=product_vo.product_category_id,
            is_deleted=False)
        return render(request, 'admin/product_templates/updateProduct.html', {
            'product_vo_lst': product_vo,
            'category_vo_lst': category_vo_lst,
            'sub_category_vo_lst': sub_category_vo_lst
        })
    except Exception:
        logger.error("Failed to edit product", exc_info=True)
        return AppServices.handle_exception("Failed to edit product", 400)


def admin_update_product(request, product_id):
    try:
        if request.method == 'POST':
            product_vo = ProductVO.objects.get(product_id=product_id,
                                               is_deleted=False)
            product_vo.product_name = request.POST.get('productName')
            product_vo.product_description = request.POST.get(
                'productDescription')
            product_vo.product_price = request.POST.get('productPrice')
            product_vo.product_quantity = request.POST.get('productQuantity')
            product_vo.product_category_id = CategoryVO.objects.get(
                category_id=request.POST.get('product_category_id'))
            product_vo.product_subcategory_id = SubCategoryVO.objects.get(
                subcategory_id=request.POST.get('product_subcategory_id'))
            if 'productImage' in request.FILES:
                product_image = request.FILES['productImage']
                os.makedirs(IMAGE_UPLOAD_PATH, exist_ok=True)
                image_save_path = os.path.join(IMAGE_UPLOAD_PATH,
                                               product_image.name)
                with open(image_save_path, 'wb+') as destination:
                    for chunk in product_image.chunks():
                        destination.write(chunk)
                product_vo.product_image_name = product_image.name
                product_vo.product_image_path = os.path.join('static',
                                                             'product_image',
                                                             product_image.name)
            product_vo.save()
            logger.info(
                f"Updated product '{product_vo.product_name}' successfully")
            return redirect('admin_view_product')
        return render(request, 'admin/product_templates/updateProduct.html')
    except Exception as e:
        logger.error("Failed to update product", exc_info=True)
        return AppServices.handle_exception("Failed to update product", 400, e)
