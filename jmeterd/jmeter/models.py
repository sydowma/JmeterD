from django.db import models

# Create your models here.
__doc__ = """
存储文件地址
历史记录
任务信息
"""

class Task(models.Model):
    """
    """
    jmx_file = models.FileField()
    name = models.CharField()
    run_time = models.DateTimeField()
    loops = models.SmallIntegerField()
    num_threads = models.PositiveIntegerField()

    gmt_create = models.DateTimeField(
        "创建时间",
        "",
        auto_now=True
    )
    host_ip = models.IPAddressField()
    host = models.IPAddressField()
    gmt_modified = models.DateTimeField()
    

class TaskResult(models.Model):
    """
    """

    status = models.PositiveSmallIntegerField()
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField()
    

class Config(models.Model):
    """
    配置
    """
    jmeter_report_path = models.FilePathField()
    jmeter_path = models.FilePathField()
    jtl_path = models.FilePathField()

class Machine(models.Model):
    """
    """
    intranet_ip = models.IPAddressField()
    external_ip = models.IPAddressField()
    password = models.CharField()

    
    



