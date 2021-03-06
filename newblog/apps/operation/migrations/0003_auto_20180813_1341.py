# Generated by Django 2.0 on 2018-08-13 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20180804_2235'),
        ('operation', '0002_auto_20180804_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('comment_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_blog', to='blog.Blog', verbose_name='评论的博客')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='operation.Comment', verbose_name='上一级回复的评论')),
                ('reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='回复用户')),
                ('root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_comment', to='operation.Comment', verbose_name='顶级的评论')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论的用户')),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='likenum',
            options={'verbose_name': '点赞数量', 'verbose_name_plural': '点赞数量'},
        ),
    ]
