from django.shortcuts import redirect
from django.shortcuts import render

from utils.my_logger import get_logger
from .models import CategoryVO

logger = get_logger()


def admin_load_category(request):
    return render(request, "admin/category_templates/addCategory.html")


def admin_insert_category(request):
    category_vo = CategoryVO()
    category_vo.category_name = request.POST.get("categoryName")
    category_vo.category_description = request.POST.get("categoryDescription")
    category_vo.save()
    logger.info("Added category '%s'" % category_vo.category_name)
    return redirect("admin_view_category")


def admin_view_category(request):
    category_dto_lst = CategoryVO.objects.filter(is_deleted=False)
    print(category_dto_lst)
    return render(request, "admin/category_templates/viewCategory.html",
                  {"category_dto_lst": category_dto_lst})


def admin_delete_category(request):
    category_id = request.POST.get("category_id")
    category_vo = CategoryVO.objects.get(category_id=category_id)
    category_vo.is_deleted = True
    category_vo.save()
    return redirect("admin_view_category")


def admin_edit_category(request):
    category_id = request.GET.get("category_id")
    category = CategoryVO.objects.get(category_id=category_id)
    return render(request, "admin/category_templates/updateCategory.html",
                  {"category": category})


def admin_update_category(request):
    if request.method == 'POST':
        category_id = request.POST.get("category_id")
        category_vo = CategoryVO.objects.get(category_id=category_id)
        category_vo.category_name = request.POST.get("categoryName")
        category_vo.category_description = request.POST.get(
            "categoryDescription")
        category_vo.save()
        return redirect(
            'admin_view_category')  # Redirect to the view category page after updating
    else:
        # Handle the case where the method is not POST (for GET requests)
        category_id = request.GET.get('category_id')
        category = CategoryVO.objects.get(category_id=category_id)
        return render(request, 'admin/category_templates/updateCategory.html',
                      {'category': category})
