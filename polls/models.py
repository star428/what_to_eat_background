# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the tabl
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.html import format_html


class Comments(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=32)
    shop = models.ForeignKey('Shop', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    content = models.CharField(max_length=255, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    vote = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'
        unique_together = (('comment_id', 'shop', 'user'),)


class Favorite(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favorite'
        unique_together = (('user', 'shop'),)


class Menu(models.Model):
    shop = models.ForeignKey('Shop', models.DO_NOTHING)
    meal_name = models.CharField(max_length=255)
    meal_pic = models.CharField(max_length=255, blank=True, null=True)
    meal_comment = models.CharField(max_length=255, blank=True, null=True)
    meal_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    meal_id = models.CharField(primary_key=True, max_length=32)
    sn = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Shop(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=32)
    shop_name = models.CharField(max_length=20, blank=True, null=True)
    shop_pic = models.CharField(max_length=255, blank=True, null=True)
    shop_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'


class ShopTag(models.Model):
    tag = models.OneToOneField('Tag', models.DO_NOTHING, primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    vote = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_tag'
        unique_together = (('tag', 'shop'),)


class Tag(models.Model):
    tag_id = models.CharField(primary_key=True, max_length=32)
    tag_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class UserReference(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_reference'
        unique_together = (('user', 'tag'),)


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=32)
    settings = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    user_pic = models.CharField(max_length=255, blank=True, null=True) # changed

    ###################
    def image_data(self):
        return format_html(
            '<img src="{}" width="100px"/>',
            self.user_pic,
        )

    image_data.short_description = u'图片'
    ###################
    class Meta:
        managed = False
        db_table = 'users'

