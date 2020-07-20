# Generated by Django 2.0.6 on 2018-06-21 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeter_report_path', models.FilePathField(default='', verbose_name='报告存放路径')),
                ('jmeter_path', models.FilePathField(default='', verbose_name='JMeter存放路径')),
                ('jtl_path', models.FilePathField(default='', verbose_name='Jtl文件存放路径')),
                ('gmt_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('gmt_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'jmeter_config',
                'ordering': ['-gmt_modified'],
                'default_permissions': ('add', 'change'),
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True, verbose_name='文件名')),
                ('status', models.BooleanField(default=True)),
                ('file_path', models.FilePathField(verbose_name='文件')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP地址')),
                ('server', models.URLField(default='', verbose_name='域名')),
                ('gmt_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('gmt_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'jmeter_host',
                'ordering': ['-gmt_modified'],
                'default_permissions': ('add', 'change'),
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='机器名')),
                ('port', models.PositiveIntegerField(default=22, verbose_name='机器端口')),
                ('ip', models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP地址')),
                ('password', models.CharField(default='', max_length=50, verbose_name='password')),
                ('status', models.BooleanField(default=0, verbose_name='状态, 离线/在线')),
                ('is_subordinate', models.BooleanField(default=False, verbose_name='是否是从机器, 只允许一个主机器')),
                ('gmt_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('gmt_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'jmeter_machine',
                'ordering': ['-gmt_modified'],
                'default_permissions': ('add', 'change'),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='任务名')),
                ('run_time', models.DateTimeField(verbose_name='执行时间')),
                ('loops', models.SmallIntegerField(default=1, verbose_name='循环次数')),
                ('num_threads', models.PositiveIntegerField(default=1, verbose_name='线程数')),
                ('scheduler', models.BooleanField(default=False, verbose_name='调度器')),
                ('duration', models.PositiveIntegerField(default=0, verbose_name='持续时间')),
                ('status', models.BooleanField(default=True, verbose_name='任务状态')),
                ('jmx_file', models.FilePathField(default='')),
                ('task_start_time', models.DateTimeField(default='1970-01-01T00:00', verbose_name='任务开始时间')),
                ('task_end_time', models.DateTimeField(default='1970-01-01T00:00', verbose_name='任务结束时间')),
                ('gmt_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('gmt_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'jmeter_task',
                'ordering': ['-gmt_modified'],
                'permissions': (('can_run_task', '执行性能测试任务'),),
                'default_permissions': ('add', 'change'),
            },
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='任务名')),
                ('run_time', models.DateTimeField(verbose_name='执行时间')),
                ('loops', models.SmallIntegerField(default=1, verbose_name='循环次数')),
                ('num_threads', models.PositiveIntegerField(default=1, verbose_name='线程数')),
                ('scheduler', models.BooleanField(default=False, verbose_name='调度器')),
                ('duration', models.PositiveIntegerField(default=0, verbose_name='持续时间')),
                ('jmx_file', models.FilePathField(default='')),
                ('data_files_id', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField(verbose_name='状态')),
                ('machines_id', models.CharField(default='', max_length=100)),
                ('gmt_create', models.DateTimeField(auto_now_add=True)),
                ('gmt_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'jmeter_task_result',
                'ordering': ['-gmt_modified'],
                'default_permissions': ('add', 'change'),
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='task',
            field=models.ForeignKey(db_constraint=False, default='', on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='jmeter.Task', verbose_name='任务'),
        ),
        migrations.AddField(
            model_name='files',
            name='task_data_file',
            field=models.ForeignKey(db_constraint=False, default='', on_delete=django.db.models.deletion.CASCADE, related_name='task_data_file', to='jmeter.Task'),
        ),
    ]
