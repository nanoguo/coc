from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class ModelsMixin:
    @classmethod
    def create(cls, columns):
        host_obj = cls()
        for k, v in columns.items():
            setattr(host_obj, k, v)
        return host_obj

    class Meta:
        abstract = True


class ClanMembers(BaseModel):
    tag = models.CharField(max_length=15, db_index=True, unique=True)
    name = models.CharField(max_length=63)
    in_clan = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'clan_members'

    def serialize(self):
        return {
            'id': self.id,
            'tag': self.tag,
            'name': self.name,
            'in_clan': self.in_clan,
            'created_time': self.created_time,
            'updated_time': self.updated_time,
        }


class UserInfos(BaseModel):
    """ 只记录总数，按月更新当前记录 """
    user = models.ForeignKey(ClanMembers, on_delete=models.CASCADE)
    role = models.CharField('角色', max_length=10)
    capital_contributions = models.IntegerField('当前总贡献', default=0)
    date = models.CharField('年月', max_length=6)

    class Meta:
        db_table = 'users_info'

    def serialize(self):
        return {
            # 'id': self.id,
            'tag': self.user.tag,
            'name': self.user.name,
            'role': self.role,
            'capital_contributions': self.capital_contributions,
            'date': self.date,
            'created_time': self.created_time,
            'updated_time': self.updated_time,
        }


class CapitalLog(BaseModel):
    """ 每周写一条记录 """
    user = models.ForeignKey(ClanMembers, on_delete=models.CASCADE)
    attacks = models.SmallIntegerField(default=0)
    capital_resource_looted = models.IntegerField('每周进攻获取', default=0)
    date = models.CharField('年月', max_length=6)

    class Meta:
        db_table = 'capital_attack_logs'

    def serialize(self):
        return {
            'tag': self.user.tag,
            'name': self.user.name,
            'capital_resource_looted': self.capital_resource_looted,
            'date': self.date,
            'created_time': self.created_time,
            'updated_time': self.updated_time,
        }


class CapitalCalculate(BaseModel):
    """ 计算历史每月差值 """
    user = models.ForeignKey(ClanMembers, on_delete=models.CASCADE)
    delta = models.IntegerField('当月实际贡献', default=0)
    date = models.CharField('年月', max_length=6)

    class Meta:
        db_table = 'capital_calculate'
