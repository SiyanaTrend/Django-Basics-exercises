from django import template

from posts.models import Post

register = template.Library()


class RecentPostsNode(template.Node):
    def __init__(self, count: str, varname: str):
        self.count = int(count)
        self.varname = varname
    def render(self, context):
        '''
        SELECT * FROM posts ORDER BY created_at DESC LIMIT 5
        '''
        recent_posts = Post.objects.order_by('-created_at')[:self.count]
        context[self.varname] = recent_posts
        return ''

@register.tag
def get_recent_posts(parser, token):
    try:
        tag_name, count, varname = token.split_contents()  # everything is string
    except ValueError:
        raise template.TemplateSyntaxError(
            "Tag 'get_recent_posts' requires exactly 3 arguments"
        )
    return RecentPostsNode(count, varname)
