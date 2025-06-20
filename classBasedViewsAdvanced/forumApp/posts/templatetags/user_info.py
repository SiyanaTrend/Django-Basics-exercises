from django import template

register = template.Library()

'''when log in admin site:'''

@register.inclusion_tag('common/user-info.html')
def user_information(user):
    if user.is_authenticated:
        return {
            'username': user.username,
        }

    return {
        'username': "Anonymous",
    }


# @register.inclusion_tag('common/user-info.html', takes_context=True)
# def user_information(context, user):
#     # print(context)
#     if user.is_authenticated:
#         return {
#             'username': user.username,
#         }
#
#     return {
#         'username': "Anonymous",
#     }

# @register.inclusion_tag('common/user-info.html', takes_context=True)
# def user_information(context):
#     if context.request.user.is_authenticated:
#         return {
#             'username': context.request.user.username,
#         }
#
#     return {
#         'username': "Anonymous",
#     }