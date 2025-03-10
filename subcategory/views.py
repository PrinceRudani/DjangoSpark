# subcategory/views.py
from django.shortcuts import render, redirect

from category.models import CategoryVO  # Import the CategoryVO model
from subcategory.models import SubCategoryVO


def admin_load_subcategory(request):
    sub_category_vo = CategoryVO.objects.filter(is_deleted=False).all()
    return render(request, 'admin/subcategory_templates/addSubCategory.html',
                  {'sub_category_vo': sub_category_vo, })


def admin_insert_subcategory(request):
    subcategory_vo = SubCategoryVO()
    subcategory_vo.subcategory_name = request.POST.get("subCategoryName")
    subcategory_vo.subcategory_description = request.POST.get(
        "subCategoryDescription")
    subcategory_category_id = request.POST.get("subCategoryCategoryName")
    category_vo = CategoryVO.objects.get(
        category_id=subcategory_category_id)
    subcategory_vo.subcategory_category_id = category_vo
    subcategory_vo.save()
    return redirect('admin_view_subcategory')


def admin_view_subcategory(request):
    sub_category_vo = SubCategoryVO.objects.filter(is_deleted=False).all()
    return render(request, 'admin/subcategory_templates/viewSubCategory.html',
                  {'sub_category_vo': sub_category_vo})


def admin_delete_subcategory(request):
    subcategory_id = request.POST.get("subcategory_id")
    sub_category_vo = SubCategoryVO.objects.get(subcategory_id=subcategory_id)
    sub_category_vo.is_deleted = True
    sub_category_vo.save()
    return redirect('admin_view_subcategory')


def admin_edit_subcategory(request):
    subcategory_id = request.POST.get("subcategory_id")

    # Get the SubCategoryVO object
    sub_category_vo = SubCategoryVO.objects.get(subcategory_id=subcategory_id)
    # Get the list of CategoryVO objects where 'is_deleted' is False
    category_vo_lst = CategoryVO.objects.filter(is_deleted=False)

    # Render the page with the context
    return render(request, 'admin/subcategory_templates/updateSubCategory.html',
                  {
                      'sub_category_vo': sub_category_vo,
                      'category_vo_lst': category_vo_lst
                  })

def admin_update_subcategory(request):
    subcategory_id = request.POST.get("subcategory_id")
    sub_category_vo = SubCategoryVO.objects.get(subcategory_id=subcategory_id)
    sub_category_vo.subcategory_name = request.POST.get("subCategoryName")
    sub_category_vo.subcategory_description = request.POST.get(
        "subCategoryDescription"

    )