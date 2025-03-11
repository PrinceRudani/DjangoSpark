from django.shortcuts import redirect, render

from utils.custome_exception import AppServices
from utils.my_logger import get_logger
from .models import CategoryVO

logger = get_logger()


def admin_load_category(request):
    try:
        logger.debug("Loading category form")
        return render(request, "admin/category_templates/addCategory.html")
    except Exception as e:
        logger.error("Error in admin_load_category: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=False)


def admin_insert_category(request):
    try:
        category_vo = CategoryVO()
        category_vo.category_name = request.POST.get("categoryName")
        category_vo.category_description = request.POST.get(
            "categoryDescription")
        category_vo.save()
        logger.info("Added category '%s'", category_vo.category_name)
        return redirect("admin_view_category")
    except Exception as e:
        logger.error("Error in admin_insert_category: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=False)


def admin_view_category(request):
    try:
        logger.debug("Fetching all categories")
        category_dto_lst = CategoryVO.objects.filter(is_deleted=False)
        return render(request, "admin/category_templates/viewCategory.html",
                      {"category_dto_lst": category_dto_lst})
    except Exception as e:
        logger.error("Error in admin_view_category: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=False)


def admin_delete_category(request):
    try:
        category_id = request.POST.get("category_id")
        category_vo = CategoryVO.objects.get(category_id=category_id)
        category_vo.is_deleted = True
        category_vo.save()
        logger.info("Deleted category '%s'", category_vo.category_name)
        return redirect("admin_view_category")
    except Exception as e:
        logger.error("Error in admin_delete_category: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=False)


def admin_edit_category(request):
    try:
        category_id = request.GET.get("category_id")
        category = CategoryVO.objects.get(category_id=category_id)
        logger.debug("Editing category '%s'", category.category_name)
        return render(request, "admin/category_templates/updateCategory.html",
                      {"category": category})
    except Exception as e:
        logger.error("Error in admin_edit_category: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=False)


def admin_update_category(request):
    try:
        if request.method == 'POST':
            category_id = request.POST.get("category_id")
            category_vo = CategoryVO.objects.get(category_id=category_id)
            category_vo.category_name = request.POST.get("categoryName")
            category_vo.category_description = request.POST.get(
                "categoryDescription")
            category_vo.save()
            logger.info("Updated category '%s'", category_vo.category_name)
            return redirect('admin_view_category')
        else:
            category_id = request.GET.get('category_id')
            category = CategoryVO.objects.get(category_id=category_id)
            logger.debug("Loading update form for category '%s'",
                         category.category_name)
            return render(request,
                          'admin/category_templates/updateCategory.html',
                          {'category': category})
    except Exception as e:
        logger.error("Error in admin_update_category: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=False)
