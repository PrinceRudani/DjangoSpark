# subcategory/views.py
from django.shortcuts import render, redirect

from category.models import CategoryVO  # Import the CategoryVO model
from subcategory.models import SubCategoryVO


def admin_load_subcategory(request):
    subcategory_vo = CategoryVO.objects.filter(is_deleted=False).all()
    return render(request, 'admin/subcategory_templates/addSubCategory.html',
                  {'subcategory_vo': subcategory_vo, })


def admin_insert_subcategory(request):
    subcategory_vo = SubCategoryVO()
    subcategory_vo.subcategory_name = request.POST.get("subCategoryName")
    subcategory_vo.subcategory_description = request.POST.get(
        "subCategoryDescription")
    subcategory_category_vo = request.POST.get("subCategoryCategoryName")
    category_vo = CategoryVO.objects.get(category_id=subcategory_category_vo)
    subcategory_vo.subcategory_category_vo = category_vo

    subcategory_vo.save()
    return redirect('admin_view_subcategory')


def admin_view_subcategory(request):
    subcategory_vo = SubCategoryVO.objects.filter(is_deleted=False).all()
    return render(request, 'admin/subcategory_templates/viewSubCategory.html',
                  {'subcategory_vo': subcategory_vo})


def admin_delete_subcategory(request):
    subcategory_id = request.POST.get("subcategory_id")
    subcategory_vo = SubCategoryVO.objects.get(subcategory_id=subcategory_id)
    subcategory_vo.is_deleted = True
    subcategory_vo.save()
    return redirect('admin_view_subcategory')


def admin_edit_subcategory(request):
    subcategory_id = request.GET.get("subcategory_id")
    subcategory_vo = SubCategoryVO.objects.filter(
        subcategory_id=subcategory_id).first()

    # Debugging: Print the subcategory_vo to check if it's being fetched correctly
    print("Subcategory VO:", subcategory_vo)

    category_vo_lst = CategoryVO.objects.filter(is_deleted=False)
    return render(request,
                  'admin/subcategory_templates/updateSubCategory.html', {
                      'subcategory_vo': subcategory_vo,
                      'category_vo_lst': category_vo_lst
                  })


def admin_update_subcategory(request, subcategory_id):
    subcategory_vo = SubCategoryVO.objects.filter(
        subcategory_id=subcategory_id).first()

    subcategory_vo.subcategory_category_vo = CategoryVO.objects.get(
        category_id=request.POST['subCategoryCategoryId'])
    subcategory_vo.subcategory_name = request.POST['subCategoryName']
    subcategory_vo.subcategory_description = request.POST[
        'subCategoryDescription']
    subcategory_vo.save()

    return redirect('admin_view_subcategory')
