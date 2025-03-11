from django.shortcuts import render, redirect

from category.models import CategoryVO
from subcategory.models import SubCategoryVO
from utils.custome_exception import AppServices
from utils.my_logger import get_logger

logger = get_logger()

def admin_load_subcategory(request):
    try:
        logger.debug("Loading subcategory form")
        subcategory_vo = CategoryVO.objects.filter(is_deleted=False).all()
        return render(request,
                      'admin/subcategory_templates/addSubCategory.html',
                      {'subcategory_vo': subcategory_vo})
    except Exception as e:
        logger.error("Error in admin_load_subcategory: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=True)

def admin_insert_subcategory(request):
    try:
        subcategory_vo = SubCategoryVO()
        subcategory_vo.subcategory_name = request.POST.get("subCategoryName")
        subcategory_vo.subcategory_description = request.POST.get(
            "subCategoryDescription")
        subcategory_category_vo = request.POST.get("subCategoryCategoryName")
        category_vo = CategoryVO.objects.get(
            category_id=subcategory_category_vo)
        subcategory_vo.subcategory_category_vo = category_vo
        subcategory_vo.save()
        logger.info("Added subcategory '%s'", subcategory_vo.subcategory_name)
        return redirect('admin_view_subcategory')
    except Exception as e:
        logger.error("Error in admin_insert_subcategory: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=True)

def admin_view_subcategory(request):
    try:
        logger.debug("Fetching all subcategories")
        subcategory_vo = SubCategoryVO.objects.filter(is_deleted=False).all()
        return render(request,
                      'admin/subcategory_templates/viewSubCategory.html',
                      {'subcategory_vo': subcategory_vo})
    except Exception as e:
        logger.error("Error in admin_view_subcategory: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=True)

def admin_delete_subcategory(request):
    try:
        subcategory_id = request.POST.get("subcategory_id")
        subcategory_vo = SubCategoryVO.objects.get(
            subcategory_id=subcategory_id)
        subcategory_vo.is_deleted = True
        subcategory_vo.save()
        logger.info("Deleted subcategory '%s'", subcategory_vo.subcategory_name)
        return redirect('admin_view_subcategory')
    except Exception as e:
        logger.error("Error in admin_delete_subcategory: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=True)

def admin_edit_subcategory(request):
    try:
        subcategory_id = request.GET.get("subcategory_id")
        subcategory_vo = SubCategoryVO.objects.filter(
            subcategory_id=subcategory_id).first()
        category_vo_lst = CategoryVO.objects.filter(is_deleted=False)
        logger.debug("Editing subcategory '%s'", subcategory_vo.subcategory_name)
        return render(request,
                      'admin/subcategory_templates/updateSubCategory.html', {
                          'subcategory_vo': subcategory_vo,
                          'category_vo_lst': category_vo_lst
                      })
    except Exception as e:
        logger.error("Error in admin_edit_subcategory: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=True)

def admin_update_subcategory(request, subcategory_id):
    try:
        subcategory_vo = SubCategoryVO.objects.filter(
            subcategory_id=subcategory_id).first()
        subcategory_vo.subcategory_category_vo = CategoryVO.objects.get(
            category_id=request.POST['subCategoryCategoryId'])
        subcategory_vo.subcategory_name = request.POST['subCategoryName']
        subcategory_vo.subcategory_description = request.POST[
            'subCategoryDescription']
        subcategory_vo.save()
        logger.info("Updated subcategory '%s'", subcategory_vo.subcategory_name)
        return redirect('admin_view_subcategory')
    except Exception as e:
        logger.error("Error in admin_update_subcategory: %s", str(e))
        return AppServices.handle_exception(exception=e, is_raise=True)