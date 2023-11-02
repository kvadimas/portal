from blog.models import Post, Tag


def create_tag():
    return Tag.objects.create(
        name='test-name',
        color='color',
        slug='slug',
    )


def create_post(user):
    return Post.objects.create(
        author=user,
        url='test-slug',
        title='test',
        text='test' * 100,
    )
