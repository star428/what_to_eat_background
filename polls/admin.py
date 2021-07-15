from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Comments, Favorite, Menu, Shop, ShopTag, Tag, UserReference, Users

admin.site.site_header = '今天吃什么后台'  # 设置header
admin.site.site_title = '今天吃什么后台'  # 设置title
admin.site.index_title = '今天吃什么后台'
############################
class CommentsAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('comment_id', 'shop', 'user', 'content','star','vote')

admin.site.register(Comments, CommentsAdmin)
############################

class FavoriteAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('user','shop')

admin.site.register(Favorite, FavoriteAdmin)
############################

class MenuAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('shop', 'meal_name', 'meal_pic', 'meal_comment', 'meal_price', 'meal_id','image_data')
    readonly_fields =  ('image_data',)

admin.site.register(Menu, MenuAdmin)
############################
class ShopAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('shop_id', 'shop_name', 'shop_pic', 'shop_comment','image_data')
    readonly_fields = ('image_data',)

admin.site.register(Shop, ShopAdmin)
################################
class ShopTagAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('tag', 'shop', 'vote')

admin.site.register(ShopTag, ShopTagAdmin)
################################
class TagAdmin(admin.ModelAdmin):
    fields = ['tag_id', 'tag_name']
    list_display = ('tag_id', 'tag_name')

admin.site.register(Tag, TagAdmin)
################################
class UserReferenceAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('user', 'tag', 'weight')


admin.site.register(UserReference, UserReferenceAdmin)
################################

class UsersAdmin(admin.ModelAdmin):
    # fields = ['tag_id', 'tag_name']
    list_display = ('user_id', 'username', 'email', 'user_pic','image_data')
    readonly_fields = ('image_data',)


admin.site.register(Users, UsersAdmin)