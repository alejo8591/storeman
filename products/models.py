# -*- coding: utf-8 -*-
from django.db import models
from datetime import date, datetime, time
"""
    Modelo para lo referente al Producto: Organizado en Catalogo para tener multiples
    opciones de cuando se quiera publicar un articulo.
"""

#Catalogos relacionados con el producto
class Catalog(models.Model):
    st_c_name = models.CharField(max_length=255, verbose_name='Nombre', help_text="Nombre del Catálogo")
    st_c_slug = models.SlugField(max_length=150, verbose_name='Título URL', help_text="Título del Catálogo para la URL, separar por '-'")
    st_c_publisher = models.CharField(max_length=150, verbose_name='Nombre', help_text="Nombre del editor del Catálogo")
    st_c_description = models.TextField(verbose_name='Descripción', help_text="Descripción del Catálogo")
    st_c_pub_date = models.DateTimeField(default=datetime.now, editable=False, verbose_name='Fecha de Creación Catalogo')
    
    def __unicode__(self):
        return u'%s' %(self.st_c_name)
    class Meta:
        ordering = ['st_c_pub_date']
        verbose_name = "Catalogo de Producto"

        
class CatalogCategory(models.Model):
    st_cc_catalog = models.ForeignKey('Catalog', related_name='categories', verbose_name='Catálogo', help_text="Catálogo al que pertenece el Producto")
    st_cc_parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name='Producto Padre', help_text="Si existe un Producto Padre este")
    st_cc_name = models.CharField(max_length=255, verbose_name='Nombre', help_text="Nombre de la Categoría del Producto")
    st_cc_slug = models.SlugField(max_length=150, verbose_name='Título URL', help_text="Título de Categoría para la URL, separar por '-'")
    st_cc_description = models.TextField(blank=True, verbose_name='Descripción', help_text="Descripción del Producto")
    st_cc_pub_date = models.DateTimeField(default=datetime.now, editable=False, verbose_name='Fecha de Creación')
    
    def save(self, *args, **kwargs):
        r = CatalogCategory.objects.all()
        if(len(r)==0): id=1
        super(CatalogCategory, self).save(*args, **kwargs)
    
    def __unicode__(self):
        if self.st_cc_parent:
            return u'%s %s - %s' %(self.st_cc_name, self.st_cc_parent, self.st_cc_name)
        return u'%s: %s' % (self.st_cc_parent, self.st_cc_name)
    class Meta:
        ordering = ['st_cc_pub_date']
        verbose_name = "Categoria"
        
#Descripción formal del Producto
class Product(models.Model):
    st_p_category = models.ForeignKey('CatalogCategory', related_name='products', verbose_name='Categoría del Producto', help_text="Nombre de la Categoría del Producto, que pertenece")
    st_p_name = models.CharField(max_length=255, verbose_name='Nombre', help_text="Nombre del Producto")
    slug = models.SlugField(max_length=150, verbose_name='Título URL', help_text="Título del Producto para la URL, separar por '-'")
    st_p_description = models.TextField(verbose_name='Descripción', help_text="Descripción del Producto")
    st_p_photo = models.ImageField(upload_to='product_photo', verbose_name='Foto', help_text="Foto del Producto maximo 2MB")
    st_p_manufacturer = models.CharField(max_length=300, verbose_name='Marca', help_text="Nombre de la Marca o Fabricante del Producto")
    st_p_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio', help_text="Precio del Producto")
    st_p_pub_date = models.DateTimeField(default=datetime.now, editable=False, verbose_name='Fecha de Creación')
    
    def __unicode__(self):
        return u'%s %s %s' %(self.st_p_name, self.st_p_pub_date, self.st_p_description)
    class Meta:
        ordering = ['st_p_pub_date']
        verbose_name = "Producto"
        
class ProductAttribute(models.Model):
    """
        El modelo ``ProductAttribute`` representa una clase de features acerca de un producto.
    """
    st_pa_name = models.CharField(max_length=300, verbose_name='Nombre', help_text="Nombre del Atributo del Producto")
    st_pa_description = models.TextField(blank=True, verbose_name='Descripción', help_text="Descripción Adicional del Atributo del Producto")
    
    def __unicode__(self):
            return u'%s' %(self.st_pa_name)
    class Meta:
        ordering = ['st_pa_name']
        verbose_name = "Atributos Adicionales de los Producto"
        
class ProductDetail(models.Model):
    """
        El modelo ``ProductDetail`` representa info unica o especifica de un Producto. Este modelo
        extiende la información contenida en ``Product`` con detalles extras y especificos
    """
    st_pd_product = models.ForeignKey(Product, related_name='details', verbose_name='Producto', help_text="Producto que quiere extender detalle")
    st_pd_attribute = models.ForeignKey('ProductAttribute', verbose_name='Atributo', help_text="Producto que quiere extender atributo")
    st_pd_value = models.CharField(max_length=500, verbose_name='Valorar', help_text="Valor que quiere extender del producto")
    st_pd_description = models.TextField(verbose_name='Descripción', help_text="Descripción extendida del producto")
    st_pd_pub_date = models.DateTimeField(default=datetime.now, editable=False, verbose_name='Fecha de Creación')
    
    def __unicode__(self):
            return u'%s: %s - %s' %(self.st_pd_product, self.st_pd_attribute, self.st_pd_value)
    class Meta:
        ordering = ['st_pd_product']
        verbose_name = "Descripción extendida de Producto"