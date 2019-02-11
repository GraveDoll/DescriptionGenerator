from django.db import models

# Create your models here.

class Gender(models.Model):
    GENDER_CHOICES = (
        ("メンズ", 'メンズ'),
        ("レディース", 'レディース'),
    )
    # name = models.CharField('性別', max_length=255)
    gender = models.CharField(
        max_length=255,
        choices=GENDER_CHOICES
    )
    def __str__(self):
        return self.gender

class MainCategory(models.Model):
    MAIN_CATEGORY_CHOICES = (
        ("トップス", 'トップス'),
        # ("ジャケット/アウター", 'メンズ'),
        ("パンツ", 'パンツ'),
        ("スカート", 'スカート'),
        ("ワンピース", 'ワンピース'),
    )
    main_category = models.CharField(
        max_length=255,
        choices=sorted(MAIN_CATEGORY_CHOICES, key=lambda x: x[0])
    )
    parent = models.ForeignKey(Gender, verbose_name='性別', on_delete=models.PROTECT)
    def __str__(self):
        return self.main_category

class SubCategory(models.Model):
    SUB_CATEGORY_CHOICES = (
        ("シャツ・ブラウス", 'シャツ・ブラウス'),
        ("カットソー", 'カットソー'),
        ("パーカー", 'パーカー'),
        ("デニムパンツ", 'デニムパンツ'),
        ("カーゴパンツ", 'カーゴパンツ'),
        ("チノパンツ", 'チノパンツ'),
        ("スラックス", 'スラックス'),
        ("スカート", 'スカート'),
        ("デニムスカート", 'デニムスカート'),
        ("ワンピース", 'ワンピース'),
        ("シャツワンピース", 'シャツワンピース'),
        ("ジャンパースカート", 'ジャンパースカート'),
        ("チュニック", 'チュニック'),
        ("ドレス", 'ドレス'),
    )
    # name = models.CharField('メインカテゴリ名', max_length=255)
    sub_category = models.CharField(
        max_length=255,
        choices=SUB_CATEGORY_CHOICES
    )
    parent = models.ForeignKey(MainCategory, verbose_name='メインカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.sub_category

class SILHOUETTE(models.Model):
    SILHOUETTE_CHOICES = (
        ("細身", '細身'),
        ("普通", '普通'),
        ("ゆったり", 'ゆったり'),
        ("スキニー", 'スキニー'),
        ("スタンダード", 'スタンダード'),
        ("ワイド", 'ワイド'),

        ("タイト", 'タイト'),
        ("フレア", 'フレア'),
        ("台形", '台形'),
        ("プリーツ", 'プリーツ'),
        ("ティアード", 'ティアード'),
    )
    # name = models.CharField('メインカテゴリ名', max_length=255)
    silhouette = models.CharField(
        max_length=255,
        choices=SILHOUETTE_CHOICES
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(MainCategory, verbose_name='メインカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.silhouette

class DESIGN(models.Model):
    DESIGN_CHOICES = (
        ("無地", '無地'),
        ("ボーダー", 'ボーダー'),
        ("ドット", 'ドット'),
        ("ストライプ", 'ストライプ'),
        ("チェック", 'チェック'),
    )
    # name = models.CharField('メインカテゴリ名', max_length=255)
    design = models.CharField(
        max_length=255,
        choices=DESIGN_CHOICES
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(MainCategory, verbose_name='メインカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.design

class NECK(models.Model):
    NECK_CHOICES = (
        ("クルーネック", 'クルーネック'),
        ("Uネック", 'Uネック'),
        ("Vネック", 'Vネック'),
        ("ボートネック", 'ボートネック'),
    )
    # name = models.CharField('メインカテゴリ名', max_length=255)
    neck = models.CharField(
        max_length=255,
        choices=NECK_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(SubCategory, verbose_name='サブカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.neck

class COLLER(models.Model):
    COLLER_CHOICES = (
        ("レギュラー", 'レギュラー'),
        ("ボタンダウン", 'ボタンダウン'),
        ("オープン", 'オープン'),
        ("スタンド", 'スタンド'),
    )
    # name = models.CharField('メインカテゴリ名', max_length=255)
    coller = models.CharField(
        max_length=255,
        choices=COLLER_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(SubCategory, verbose_name='サブカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.coller

class ZipButton(models.Model):
    ZipButton_CHOICES = (
        ("プルオーバー", 'プルオーバー'),
        ("ジップアップ", 'ジップアップ'),
    )
    zip_button = models.CharField(
        max_length=255,
        choices=ZipButton_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(SubCategory, verbose_name='サブカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.zip_button

class Length(models.Model):
    LENGTH_CHOICES = (
        ("ひざ上", 'ひざ上'),
        ("ひざ丈", 'ひざ丈'),
        ("クロップド", 'クロップド'),
        ("フルレングス", 'フルレングス'),

        ("ショート・ミニ丈", 'ショート・ミニ丈'),
        ("ロング・マキシ丈", 'ロング・マキシ丈'),
        ("ミモレ・半端丈", 'ミモレ・半端丈'),
    )
    length = models.CharField(
        max_length=255,
        choices=LENGTH_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(MainCategory, verbose_name='メインカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.length

class Leg(models.Model):
    LEG_CHOICES = (
        ("テーパード", 'テーパード'),
        ("フレア・ブーツカット", 'フレア・ブーツカット'),
    )
    leg = models.CharField(
        max_length=255,
        choices=LEG_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(MainCategory, verbose_name='メインカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.leg

class Effect(models.Model):
    EFFECT_CHOICES = (
        ("リジッド", 'リジッド'),
        ("ユーズド加工", 'ユーズド加工'),
        ("クラッシュ・ダメージ加工", 'クラッシュ・ダメージ加工'),
    )
    effect = models.CharField(
        max_length=255,
        choices=EFFECT_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        default = ''
    )
    parent = models.ForeignKey(SubCategory, verbose_name='サブカテゴリ', on_delete=models.PROTECT)
    def __str__(self):
        return self.effect

class Post(models.Model):
    m_category = models.ForeignKey(MainCategory, verbose_name='メインカテゴリ', on_delete=models.PROTECT)
    s_category = models.ForeignKey(SubCategory, verbose_name='サブカテゴリ', on_delete=models.PROTECT)
    silhouette = models.ForeignKey(SILHOUETTE, verbose_name='シルエット', on_delete=models.PROTECT)
    design = models.ForeignKey(DESIGN, verbose_name='デザイン', on_delete=models.PROTECT)
    neck = models.ForeignKey(NECK, verbose_name='ネック', on_delete=models.PROTECT)
    coller = models.ForeignKey(COLLER, verbose_name='襟', on_delete=models.PROTECT)
    zip_button = models.ForeignKey(ZipButton, verbose_name='ジップ・ボタン', on_delete=models.PROTECT)
    length = models.ForeignKey(Length, verbose_name='丈', on_delete=models.PROTECT,)
    leg = models.ForeignKey(Leg, verbose_name='膝下', on_delete=models.PROTECT)
    effect = models.ForeignKey(Effect, verbose_name='加工', on_delete=models.PROTECT)
    def __str__(self):
        return self.title
        