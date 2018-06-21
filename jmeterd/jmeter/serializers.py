from rest_framework import serializers

from jmeter.models import (
    Host,
    Task,
    TaskResult,
    Config,
    Machine,
    Files

)


class MachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Machine
        fields = ('name', 'port', 'ip', 'password', 'status', 'is_slave', 'task')

class TaskSerializer(serializers.ModelSerializer):
    """
    任务 model 序列化
    """
    machines = MachineSerializer(
        many=True, read_only=True)


    class Meta:
        model = Task
        fields = ('id', 'name', 'run_time', 'loops', 'num_threads',
                  'scheduler', 'duration', 'machines')


class TaskResultSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = TaskResult
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Host
        fields = '__all__'


class ConfigSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Config
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files
        fields = ('name', 'file_path', 'status')



