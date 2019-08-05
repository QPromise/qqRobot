import  re
import math
def ratio(m, d):
    return round((m / d), 1)
def test_direction(members):
    invalid_alias = {'1.无效备注':[]}
    uncertain_pro = {'2.专硕不确定':[]}
    uncertain_ac = {'3.学硕不确定':[]}
    pro = 0 #专硕
    pro_910 = 0
    pro_940 = 0
    pro_911 = 0
    pro_930_341 = 0
    ac = 0 # 学硕
    ac_940 = 0
    ac_954 = 0
    ac_912 = 0
    other = 0
    for key, value in members.items():
        if 'cd' in value:
            goal = value['cd']
            if re.search('910',goal) or re.search('01',goal) or re.search('计',goal) and re.search('专',goal):
                pro_910 += 1
                pro += 1
            elif re.search('保密',goal) and re.search('学',goal) or re.search('940',goal) and re.search('学',goal) or re.search('网',goal) and re.search('学',goal):
                ac_940 += 1
                ac += 1
            elif re.search('940',goal) or re.search('保密',goal) or re.search('02',goal) or re.search('网',goal):
                pro_940 += 1
                pro += 1
            elif re.search('912', goal) or re.search('软',goal) and re.search('学',goal) or re.search('软',goal) and re.search('理',goal):
                ac_912 += 1
                ac += 1
            elif re.search('911', goal) or re.search('软',goal):
                pro_911 += 1
                pro += 1
                #alias.append(goal)
            elif re.search('954', goal) or re.search('计',goal) and re.search('学',goal) or re.search('计',goal) and re.search('应',goal)or re.search('计',goal) and re.search('科',goal):
                ac_954 += 1
                ac += 1
            elif re.search('专', goal) or re.search('技术',goal):
                pro += 1
                uncertain_pro['2.专硕不确定'].append(goal)
            elif re.search('学硕', goal):
                ac += 1
                uncertain_ac['3.学硕不确定'].append(goal)
            elif re.search('农', goal) and re.search('信',goal):
                pro_930_341 += 1
                pro += 1
            else:
                invalid_alias['1.无效备注'].append(goal)
                other += 1
    res = [ratio(pro_910,40),ratio(pro_911,38),ratio(pro_940,22),ratio(ac_912,12),ratio(ac_940,7),ratio(ac_954,27),ratio(pro,ac),pro+ac+other,pro+ac,ratio(pro_930_341,11)]
    print(invalid_alias,end= '\n\n')
    print(uncertain_pro)
    print(uncertain_ac)
    print('911,910,940,930+341:',pro_911,pro_910,pro_940,pro_930_341)
    print('专硕,学硕,其它:',pro,ac,other)
    return res