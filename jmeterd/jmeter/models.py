from django.db import models

# Create your models here.
__doc__ = """
存储文件地址
历史记录
任务信息
"""

class Machine(models.Model):
    """
    """
    name = models.CharField()
    port = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=22
    )
    intranet_ip = models.IPAddressField()
    external_ip = models.IPAddressField()
    password = models.CharField()
    secret_key = models.FileField()
    status = models.PositiveSmallIntegerField()
    gmt_create = models.DateTimeField(
        "创建时间",
        "",
        auto_now=True
    )
    gmt_modified = models.DateTimeField()

    class Meta:
        db_table = 'jmeter_machine'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')

class File(models.Model):
    """
    """
    file = models.FileField()


class AbstractTask(models.Model):

    jmx_file = models.ForeignKey(
        File,
        on_delete=models.CASCADE
    )
    data_file = models.ForeignKey(
        File,
        on_delete=models.CASCADE
    )

    name = models.CharField()
    run_time = models.DateTimeField()
    loops = models.SmallIntegerField()
    num_threads = models.PositiveIntegerField()


    source_machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        db_constraint=False
    )
    target_machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        db_constraint=False
    )

    class Meta:
        abstract = True
    
        
class Task(AbstractTask):
    """
    """
    status = models.PositiveSmallIntegerField()
    gmt_create = models.DateTimeField(
        "创建时间",
        "",
        auto_now=True
    )
    gmt_modified = models.DateTimeField()
    
    class Meta:
        db_table = 'jmeter_task'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')
        permissions = (("can_run_task", "执行性能测试任务"),)
    
    
class TaskResult(AbstractTask):
    """
    """

    # 成功或者失败
    status = models.PositiveSmallIntegerField()
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField()

    class Meta:
        db_table = 'jmeter_task_result'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')


class Host(models.Model):
    ip = models.IPAddressField()
    server = models.URLField()

    gmt_create = models.DateTimeField(
        "创建时间",
        "",
        auto_now=True
    )
    gmt_modified = models.DateTimeField()

    class Meta:
        db_table = 'jmeter_host'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')

class Config(models.Model):
    """
    配置
    """
    jmeter_report_path = models.FilePathField()
    jmeter_path = models.FilePathField()
    jtl_path = models.FilePathField()
    host = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        db_constraint=False
    )
    gmt_create = models.DateTimeField(
        "创建时间",
        "",
        auto_now=True
    )
    gmt_modified = models.DateTimeField()

    class Meta:
        db_table = 'jmeter_config'
        ordering = ['-gmt_modified']
        default_permissions = ('add', 'change')



    
    



