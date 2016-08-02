from django.contrib import admin

def application(request):
    app_list = admin.site.get_app_list(request)
    return {
        'ghoster_app_list': app_list,
    }
