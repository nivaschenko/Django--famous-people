from django.contrib import admin, messages

from women.models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'category', 'brief_info')
    readonly_fields = ['slug']
    list_display_links = ('title',)
    ordering = ('time_create', 'title')
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'category__name']
    list_filter = ['category__name', 'is_published']
    filter_horizontal = ['tags']

    @admin.display(description='Content length (chars)')
    def brief_info(self, women:Women):
        return f'{len(women.content)}'

    @admin.action(description='Publish selected women')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        message = f'{count} row was updated'
        if count > 1:
            message = f'{count} rows were updated'
        self.message_user(request, message)

    @admin.action(description='Set draft selected women')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        message = f'{count} row was updated'
        if count > 1:
            message = f'{count} rows were updated'
        self.message_user(request, message, messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# Register your models here.
# admin.site.register(Women, WomenAdmin)
