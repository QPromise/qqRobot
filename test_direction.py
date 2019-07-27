import  re
import math
def ratio(m, d):
    return round((m / d) * 10, 1)
def test_direction(members):
    alias = []
    pro = 0 #专硕
    pro_910 = 0
    pro_940 = 0
    pro_911 = 0
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
            elif re.search('保密',goal) and re.search('学',goal) or re.search('940',goal) and re.search('学',goal):
                ac_940 += 1
                ac += 1
            elif re.search('940',goal) or re.search('保密',goal) or re.search('02',goal):
                pro_940 += 1
                pro += 1
            elif re.search('912', goal) or re.search('软',goal) and re.search('学',goal) or re.search('软',goal) and re.search('理',goal):
                ac_912 += 1
                ac += 1
            elif re.search('911', goal) or re.search('软',goal):
                pro_911 += 1
                pro += 1
                alias.append(goal)
            elif re.search('954', goal) or re.search('计',goal) and re.search('学',goal) or re.search('计',goal) and re.search('应',goal):
                ac_954 += 1
                ac += 1
            elif re.search('专', goal) or re.search('技术',goal) or re.search('计科',goal):
                pro += 1
            else:
                other += 1
    res = [ratio(pro_910,pro),ratio(pro_911,pro),ratio(pro_940,pro),ratio(ac_912,ac),ratio(ac_940,ac),ratio(ac_954,ac),ratio(pro,ac),pro+ac+other]
    print(pro+ac+other)
    return res