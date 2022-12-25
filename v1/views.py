import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from v1.models import ClanMembers, UserInfos, CapitalCalculate, CapitalLog

from coc import utils


class ClanUserInfos(APIView):
    """获取部落成员信息 """

    @staticmethod
    def get(request):
        clans_user_infos = ClanMembers.objects.filter(in_clan=1)

        return Response({
            'data': [user.serialize() for user in clans_user_infos],
            'total': len(clans_user_infos)
        })


class TopContributions(APIView):
    """ 获取当前总量排名 """

    @staticmethod
    def get(request):
        dt = datetime.datetime.now().strftime('%Y%m')
        user_infos = UserInfos.objects.filter(user__in_clan=1, date=dt).order_by('-capital_contributions')
        # todo redis

        return Response({
            'data': [user.serialize() for user in user_infos],
            'total': len(user_infos)
        })


class TopWeeklyAttack(APIView):
    """ 获取攻击记录 """
    @staticmethod
    def get(request):
        dt = '20221118'
        logs = CapitalLog.objects.filter(user__in_clan=1).order_by('-capital_resource_looted')

        return Response({
            'data': [log.serialize() for log in logs],
            'total': len(logs)
        })


class MonthContributions(APIView):
    """ 获取上月贡献排名 """

    @staticmethod
    def get(request):
        dt = utils.last_month_str()
        infos = CapitalCalculate.objects.filter(user__in_clan=1, date=dt).order_by('-delta')
        print(infos)

        return Response({"data": "ok"})
