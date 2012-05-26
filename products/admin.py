from django.contrib import admin
from django.db import models
from products.models import Catalog, CatalogCategory, Product, ProductAttribute, ProductDetail

class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('st_cc_name', 'st_cc_name')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('st_p_name', 'st_p_pub_date', 'st_p_description')
    
#class ProductAttributeAdmin(admin.ModelAdmin):
#    list_display = ('st_pa_name')
    
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('st_pd_product', 'st_pd_attribute', 'st_pd_value')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Catalog)
admin.site.register(CatalogCategory, CatalogCategoryAdmin)
admin.site.register(ProductAttribute)
admin.site.register(ProductDetail, ProductDetailAdmin)