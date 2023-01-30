'''
별명 사용하기 2 (함수에도 별칭 사용하기)
'''

from converter import kilometer_to_miles as k_to_m

miles = k_to_m(150)
print('150kim = {}miles'.format(miles))