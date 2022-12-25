import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coc.settings')
import django

django.setup()

import time

from coc import coc_sdk
from v1.models import ClanMembers, CapitalLog, CapitalCalculate, UserInfos
from coc import utils


def sync_clan_members():
    data = coc_sdk.get_clan_members()
    ClanMembers.objects.update(in_clan=0)
    if data:
        for user in data.get('items', []):
            ClanMembers.objects.update_or_create(defaults={'in_clan': 1, 'name': user['name']}, tag=user['tag'])


def sync_user_info():
    users = ClanMembers.objects.filter(in_clan=1).all()
    for user in users:
        tag = user.tag
        userinfo = coc_sdk.get_users_info(tag)
        if userinfo:
            UserInfos.objects.update_or_create(defaults={
                'capital_contributions': userinfo['clanCapitalContributions'],
                'role': userinfo['role'],
            }, user_id=user.id, date=utils.current_month_str())
            time.sleep(1)


def sync_attack_log():
    users = ClanMembers.objects.filter(in_clan=1).all()
    all_users_tag = [user.tag for user in users]
    tag_id_map = {user.tag: user.id for user in users}

    # get attack log
    data = coc_sdk.get_capitalraid_log()
    log = data.get('items', [])
    current_log = {}
    if log:
        current_log = log[0]

    if not current_log or current_log['state'] != 'ended':
        return

    members = current_log.get('members', [])
    date = current_log.get('startTime', '')[:8]

    for member in members:
        tag = member['tag']
        if tag in all_users_tag:
            CapitalLog.objects.update_or_create(defaults={
                'attacks': member['attacks'],
                'capital_resource_looted': member['capitalResourcesLooted'],
            },
                date=date,
                user_id=tag_id_map[tag],
            )


def check_who_not_attack():
    # get attack log
    data = coc_sdk.get_capitalraid_log()
    log = data.get('items', [])
    current_log = {}
    if log:
        current_log = log[0]

    attack_members = current_log.get('members', [])
    clan_members = ClanMembers.objects.filter(in_clan=1).all()
    print(attack_members)
    print(clan_members)


if __name__ == '__main__':
    sync_clan_members()
    # sync_user_info()
    # sync_attack_log()
    pass
