from django.urls import path, include

from .views import SearchResultsView, render_search, PublicationCreate, PublicationUpdate, PublicationDelete, PublicationDetailView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('publication/new/', login_required(PublicationCreate.as_view()), name='publication-new'),
    path('publication/show/', login_required(SearchResultsView.as_view()), name='publication-show'), 
    path('publication/<int:pk>/detail_view/', login_required(PublicationDetailView.as_view()), name='publication-detail'),
    path('publication/<int:pk>/edit/', login_required(PublicationUpdate.as_view()), name='publication-update'),
    path('publication/<int:pk>/delete/', PublicationDelete, name='publication-delete'),
    path('author/new/', login_required(views.AuthorCreate.as_view()), name='author-new'),
    path('author/show/', login_required(views.AuthorShow.as_view()), name='author-show'),
    path('author/<int:pk>/edit/', login_required(views.AuthorUpdate.as_view()), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete, name='author-delete'),    
    path('translator/new/', login_required(views.TranslatorCreate.as_view()), name='translator-new'),
    path('translator/show/', login_required(views.TranslatorShow.as_view()), name='translator-show'),
    path('translator/<int:pk>/edit/', login_required(views.TranslatorUpdate.as_view()), name='translator-update'),
    path('translator/<int:pk>/delete/', views.TranslatorDelete, name='translator-delete'), 
    path('form_of_publication/new/', login_required(views.FormOfPublicationCreate.as_view()), name='form-of-publication-new'),
    path('form_of_publication/show/', login_required(views.FormOfPublicationShow.as_view()), name='form-of-publication-show'),
    path('form_of_publication/<int:pk>/edit/', login_required(views.FormOfPublicationUpdate.as_view()), name='form-of-publication-update'),
    path('form_of_publication/<int:pk>/delete/', views.FormOfPublicationDelete, name='form-of-publlication-delete'),    
    path('city/new/', login_required(views.CityCreate.as_view()), name='city-new'),
    path('city/show/', login_required(views.CityShow.as_view()), name='city-show'),
    path('city/<int:pk>/edit/', login_required(views.CityUpdate.as_view()), name='city-update'),
    path('city/<int:pk>/delete/', views.CityDelete, name='city-delete'),    
    path('genre/new/', login_required(views.GenreCreate.as_view()), name='genre-new'),
    path('genre/show/', login_required(views.GenreShow.as_view()), name='genre-show'),
    path('genre/<int:pk>/edit/', login_required(views.GenreUpdate.as_view()), name='genre-update'),
    path('genre/<int:pk>/delete/', views.GenreDelete, name='genre-delete'),    
    path('church/new/', login_required(views.ChurchCreate.as_view()), name='church-new'),
    path('church/show/', login_required(views.ChurchShow.as_view()), name='church-show'),
    path('church/<int:pk>/edit/', login_required(views.ChurchUpdate.as_view()), name='church-update'),
    path('church/<int:pk>/delete/', views.ChurchDelete, name='church-delete'), 
    path('language/new/', login_required(views.LanguageCreate.as_view()), name='language-new'),
    path('language/show/', login_required(views.LanguageShow.as_view()), name='language-show'),
    path('language/<int:pk>/edit/', login_required(views.LanguageUpdate.as_view()), name='language-update',),
    path('language/<int:pk>/delete/', views.LanguageDelete, name='language-delete'), 
    path('special_occasion/new/', login_required(views.SpecialOccasionCreate.as_view()), name='special-occasion-new'),
    path('special_occasion/show/', login_required(views.SpecialOccasionShow.as_view()), name='special-occasion-show'),
    path('special_occasion/<int:pk>/edit/', login_required(views.SpecialOccasionUpdate.as_view()), name='special-occasion-update',),
    path('special_occasion/<int:pk>/delete/', views.SpecialOccasionDelete, name='special-occasion-delete'),     
    path('owner/new/', login_required(views.OwnerCreate.as_view()), name='owner-new'),
    path('owner/show/', login_required(views.OwnerShow.as_view()), name='owner-show'),
    path('owner/<int:pk>/edit/', login_required(views.OwnerUpdate.as_view()), name='owner-update',),
    path('owner/<int:pk>/delete/', views.OwnerDelete, name='owner-delete'),
    path('uploadedfile/new/', login_required(views.UploadedFileCreate.as_view()), name='uploadedfile-new'),
    path('uploadedfile/show/', login_required(views.UploadedFileShow.as_view()), name='uploadedfile-show'),
    path('uploadedfile/<int:pk>/edit/', login_required(views.UploadedFileUpdate.as_view()), name='uploadedfile-update',),
    path('uploadedfile/<int:pk>/delete/', views.UploadedFileDelete, name='uploadedfile-delete'),    
    path('illustration_layout_type/new/', login_required(views.IllustrationLayoutTypeCreate.as_view()), name='illustration-layout-type-new'),
    path('illustration_layout_type/show/', login_required(views.IllustrationLayoutTypeShow.as_view()), name='illustration-layout-type-show'),
    path('illustration_layout_type/<int:pk>/edit/', login_required(views.IllustrationLayoutTypeUpdate.as_view()), name='illustration-layout-type-update',),
    path('illustration_layout_type/<int:pk>/delete/', views.IllustrationLayoutTypeDelete, name='illustration-layout-type-delete'),
    path('', render_search, name='index'),
]