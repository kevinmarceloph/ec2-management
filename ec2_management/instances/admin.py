from django.contrib import admin
from .models import Instance


class InstanceAdmin(admin.ModelAdmin):
    """
    ModelAdmin to exclude instance.running and include the launch action.
    """
    fields = ('ami_id', 'instance_type', 'availability_zone', 'access_key_id', 'secret_access_key')
    list_display = ('ami_id', 'running')
    actions = ('launch',)

    def launch(self, request, queryset):
        """
        Launches all checked instances.
        """
        launched = 0
        for instance in queryset:
            if not instance.running:
                launched += 1
            instance.launch()

        self.message_user(request, '{} instances successfully launched.'.format(launched))
    launch.short_description = 'Launch instances'


admin.site.register(Instance, InstanceAdmin)
