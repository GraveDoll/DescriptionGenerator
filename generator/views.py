from django.shortcuts import render

from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404, reverse
from generator.models import Gender, MainCategory, SubCategory, SILHOUETTE, DESIGN, NECK, COLLER, ZipButton, Length, Leg, Effect
from generator.forms import PostCreateForm
from generator.consts import *
import json
import logging

# Create your views here.

def index(request):
    response = ""
    form = PostCreateForm()

    if request.method == 'POST':
        try:
            result_res_main_category = request.POST['main_category']
            result_res_sub_category = request.POST['sub_category']
            result_res_silhouette = request.POST['silhouette']
            result_res_design = request.POST['design']
            result_res_neck = request.POST['neck']
            result_res_coller = request.POST['coller']
            result_res_zipbutton = request.POST['zipbutton']
            result_res_length = request.POST['length']
            result_res_leg = request.POST['leg']
            result_res_effect = request.POST['effect']
            
            if result_res_silhouette:
                silhouette = SILHOUETTE.objects.filter(pk=result_res_silhouette).first()
                response += silhouette.description

            if result_res_design:
                design = DESIGN.objects.filter(pk=result_res_design).first()
                response += design.description
                
            if result_res_neck:
                neck = NECK.objects.filter(pk=result_res_neck).first()
                response += neck.description

            if result_res_coller:
                coller = COLLER.objects.filter(pk=result_res_coller).first()
                response += coller.description

            if result_res_zipbutton:
                zipbutton = ZipButton.objects.filter(pk=result_res_zipbutton).first()
                response += zipbutton.description

            if result_res_length:
                length = Length.objects.filter(pk=result_res_length).first()
                response += length.description

            if result_res_leg:
                leg = Leg.objects.filter(pk=result_res_leg).first()
                response += leg.description

            if result_res_effect:
                effect = Effect.objects.filter(pk=result_res_effect).first()
                response += effect.description

        except KeyError:
            logging.debug("KeyError")
            response = ""
        return HttpResponse(response)

    context = {
        'response': response,
        'form': form,
    }
    return render(request, 'generator/index.html', context)

def get_category(request):
    pk = request.POST.get('pk')
    if not pk:
        category_list = []
    # pkがあれば、そのpkでカテゴリを絞り込む
    else:
        category_list = MainCategory.objects.filter(parent__pk=pk).order_by('pk')
    category_list = [{'pk':category.pk, 'main_category':category.main_category} for category in category_list]

    # JSONで返す。値が辞書じゃない場合は、safe=Falseが必要。今回はリストなのでsafe=Falseに。
    return JsonResponse(category_list, safe=False)

def get_sub_category(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk:
        category_list = []
    else:
        category_list = SubCategory.objects.filter(parent__pk=mainCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'sub_category': category.sub_category} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_silhouette(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = SILHOUETTE.objects.filter(parent__pk=mainCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'silhouette': category.silhouette} for category in category_list]

    return JsonResponse(category_list, safe=False)

def get_design(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = DESIGN.objects.filter(parent__pk=mainCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'design': category.design} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_neck(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = NECK.objects.filter(parent__pk=subCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'neck': category.neck} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_coller(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = COLLER.objects.filter(parent__pk=subCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'coller': category.coller} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_zip_button(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = ZipButton.objects.filter(parent__pk=subCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'zip_button': category.zip_button} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_length(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = Length.objects.filter(parent__pk=mainCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'length': category.length} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_leg(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = Leg.objects.filter(parent__pk=mainCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'leg': category.leg} for category in category_list]
    return JsonResponse(category_list, safe=False)

def get_effect(request):
    mainCategoryPk = request.POST.get('mainCategoryPk')
    subCategoryPk = request.POST.get('subCategoryPk')
    if not mainCategoryPk or not subCategoryPk:
        category_list = []
    else:
        category_list = Effect.objects.filter(parent__pk=subCategoryPk).order_by('pk')
    category_list = [{'pk': category.pk, 'effect': category.effect} for category in category_list]
    return JsonResponse(category_list, safe=False)