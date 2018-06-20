from django.db import models

# Create your models here.
__doc__ = """
存储文件地址
历史记录
任务信息

注意，对 Model 的操作写在 Manage 中，不要把复杂操作写到 views 中
"""


class Host(models.Model):
    ip = models.GenericIPAddressField(
        'IP地址',
        null=False,
        blank=False,
        default='127.0.0.1'

    )
    server = models.URLField(
        '域名',
        null=False,
        blank=False,
        default=""
    )

    gmt_create = models.DateTimeField(
        "创建时间",
        null=False,
        auto_now_add=True
    )
    gmt_modified = models.DateTimeField(
        '修改时间',
        null=False,
        auto_now=True,
    )

    class Meta:
        db_table = 'jmeter_host'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')


class Machine(models.Model):
    """
    """
    name = models.CharField(
        "机器名",
        max_length=20,
        null=False,
        blank=False,
        default=""
    )
    port = models.PositiveIntegerField(
        '机器端口',
        blank=False,
        null=False,
        default=22
    )
    ip = models.GenericIPAddressField(
        'IP地址',
        blank=False,
        null=False,
        default="127.0.0.1"
    )
    password = models.CharField(
        'password',
        max_length=50,
        blank=False,
        null=False,
        default=""

    )

    # secret_key = models.FileField(
    #     '秘钥文件',
    #     null=False,
    #     blank=True
    # )

    status = models.BooleanField(
        '状态, 离线/在线',
        blank=False,
        null=False,
        default=0

    )

    is_slave = models.BooleanField(
        '是否是从机器, 只允许一个主机器',
        blank=False,
        null=False,
        default=False
    )

    # host = models.ForeignKey(
    #     Host,
    #     on_delete=models.CASCADE,
    #     db_constraint=False,
    #     null=False,
    #     blank=False
    # )

    gmt_create = models.DateTimeField(
        "创建时间",
        null=False,
        auto_now_add=True,
    )
    gmt_modified = models.DateTimeField(
        '修改时间',
        null=False,
        auto_now=True
    )

    class Meta:
        db_table = 'jmeter_machine'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')

class Files(models.Model):
    """
    """
    name = models.CharField(
        "文件名",
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        default=""
    )
    
    # 状态，0 未知，  1不存在， 2存在
    status = models.BooleanField(
        blank=False,
        null=False,
        default=True
    )

    file_path = models.FilePathField(
        '文件',
        null=False,
        blank=False,
    )


class AbstractTask(models.Model):

    name = models.CharField(
        '任务名',
        max_length=20,
        blank=False,
        null=False,
        default=""
    )
    run_time = models.DateTimeField(
        '执行时间',
        null=False,
        blank=False
    )
    loops = models.SmallIntegerField(
        '循环次数',
        null=False,
        blank=False,
        default=1
    )
    num_threads = models.PositiveIntegerField(
        '线程数',
        null=False,
        blank=False,
        default=1
    )

    scheduler = models.BooleanField(
        '调度器',
        null=False,
        blank=False,
        default=False
    )

    duration = models.PositiveIntegerField(
        '持续时间',
        null=False,
        blank=False,
        default=0
    )

    machines = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        db_constraint=False,
        null=False,
        blank=False,
        verbose_name='压力源机器'
    )


    class Meta:
        abstract = True
    
        
class Task(AbstractTask):
    """
    """
    status = models.BooleanField(
        '任务状态',
        null=False,
        blank=True,
        default=True,
    )

    jmx_file = models.ForeignKey(
        Files,
        related_name='task_jmx_file',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=0
    )

    data_file = models.ForeignKey(
        Files,
        related_name='task_data_file',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )
    
    task_start_time = models.DateTimeField(
        '任务开始时间',
        null=False,
        blank=False
    )
    task_end_time = models.DateTimeField(
        '任务结束时间',
        null=False,
        blank=False
    )

    gmt_create = models.DateTimeField(
        "创建时间",
        null=False,
        auto_now_add=True,
    )
    gmt_modified = models.DateTimeField(
        '修改时间',
        null=False,
        auto_now=True,
    )
    
    class Meta:
        db_table = 'jmeter_task'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')
        permissions = (("can_run_task", "执行性能测试任务"),)
    
    
class TaskResult(AbstractTask):
    """
    """
    jmx_file = models.ForeignKey(
        Files,
        related_name='result_jmx_file',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=0
    )

    data_file = models.ForeignKey(
        Files,
        related_name='result_data_file',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )


    # 成功或者失败
    status = models.BooleanField(
        '状态',
        null=False,
        blank=False
    )
    gmt_create = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    gmt_modified = models.DateTimeField(
        null=False,
        auto_now=True
    )

    class Meta:
        db_table = 'jmeter_task_result'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')


class Config(models.Model):
    """
    配置
    """
    jmeter_report_path = models.FilePathField(
        '报告存放路径',
        null=False,
        blank=False,
        default=""
    )
    jmeter_path = models.FilePathField(
        'JMeter存放路径',
        null=False,
        blank=False,
        default=""
    )
    jtl_path = models.FilePathField(
        'Jtl文件存放路径',
        null=False,
        blank=False,
        default=""
    )

    gmt_create = models.DateTimeField(
        "创建时间",
        null=False,
        auto_now_add=True
    )
    gmt_modified = models.DateTimeField(
        '修改时间',
        null=False,
        auto_now=True
    )

    class Meta:
        db_table = 'jmeter_config'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')



    
    



