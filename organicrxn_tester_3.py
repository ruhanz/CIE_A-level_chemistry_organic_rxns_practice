# import pandas as pd
# import numpy as np
#
# arr = np.array([
#     ['cracking','alkane','','alkane','','heat, Al2O3 catalyst'],
#     ['free radical substitution', 'alkane','Cl2, Br2','Xoalkane','','ultraviolet light'],
#     ['elimination','Xoalkane','NaOH(aq)','alkene','H2O, NaX','ethanol, heat'],
#     ['dehydration','alcohol','','alkene','H2O','heat, catalyst e.g. Al2O3 OR conc. acid e.g. H2SO4, H3PO4'],
#     ['electrophilic addition','alkene','H2(g)','alkane','','heat, Pt/Ni catalyst'],
#     ['electrophilic addition','alkene','steam','alcohol','','H3PO4 catalyst'],
#     ['electrophilic addition','alkene','HX(g)','Xoalkane','','room temp'],
#     ['electrophilic addition','alkene','X2','Xoalkane','',''],
#     ['nucleophilic addition','aldehyde/ketone','HCN','hydroxynitrile','','heat, KCN catalyst'],
#     ['nucleophilic substitution','Xoalkane','NH3','amine','HX','reagent in ethanol, heat, under pressure'],
#     ['nucleophilic substitution','Xoalkane','NaOH(aq)','alcohol','NaX','heat'],
#     ['nucleophilic substitution','Xoalkane','AgNO3(aq)','alcohol','AgX(s)','reagent in ethanol'],
#     ['nucleophilic substitution','Xoalkane','KCN','nitrile','KX','reagent in ethanol, heat'],
#     ['substitution','alcohol','HX(g)','Xoalkane','H2O',''],
#     ['substitution','alcohol','KCl','Xoalkane','H2O','conc. H2SO4 OR conc. H3PO4'],
#     ['substitution','alcohol','PCl3','Xoalkane','H3PO3','heat'],
#     ['substitution','alcohol','PCl5','Xoalkane','HCl(g),POCl3',''],
#     ['substitution','alcohol','SOCl2','Xoalkane','HCl, SO2',''],
#     ['hydrolysis',''
#     []
# ])
column_names = {
    0:'type: ',
    1: 'organic reagent: ',
    2: 'inorganic reagent: ',
    3: 'organic product: ',
    4: 'inorganic product: ',
    5: 'conditions: '
}
#
# df = pd.DataFrame(arr,[i for i in range(len(arr))],[column_names[j] for j in range(6)])
# pd.set_option('display.max_colwidth', None)  # Disable truncation
# pd.set_option('display.expand_frame_repr', False)  # Prevent line breaks between columns
# print(df)
# def test(shown: list[int]):
#     for col in shown:
#         print(f'{column_names[col]}: {arr}')
#
# def menu():
#     print('0: type of rxn\n'
#           '1: organic reagent\n'
#           '2: inorganic reagent\n'
#           '3: organic product\n'
#           '4: inorganic product\n'
#           '5: conditions\n'
#           'Example input: 1,2,5')
#     print('Select cols to show:\n')
#     shown = list(map(int,input().split(',')))
# arr = []
# def def_new_rxn():
#     global arr
#     rxn_type = input('type: ')
#     org_reag = input('org reag: ')
#     inorg_reag = input('inorg reag: ')
#     org_prod = input('org prod: ')
#     inorg_prod = input('inorg prod: ')
#     cond = input('cond: ')
#     new_rxn = [rxn_type,org_reag,inorg_reag,org_prod,inorg_prod,cond]
#
#     rule = input()
#     if rule == '':
#         arr.append(new_rxn.copy())
#         def_new_rxn()
#     elif rule == 'r':
#         def_new_rxn()
#     else:
#         arr.append(new_rxn.copy())
#         arr.sort()
#         print(f'arr = [')
#         for i in arr:
#             print(f'\t {i},')
#         print(']')
#
# def_new_rxn()
# arr2 = [
# 	 ['AE', 'alkene', 'H2(g)', 'alkane', '', 'Pt/Ni catalyst, heat'],
# 	 ['AE', 'alkene', 'H2O(g)', 'alcohol', '', 'H3PO4 catalyst'],
# 	 ['AE', 'alkene', 'HX(g)', 'Xoalkane', '', 'room temp'],
# 	 ['AE', 'alkene', 'X2', 'Xoalkane', '', ''],
# 	 ['AN', 'aldehyde', 'HCN', 'hydroxynitrile', '', 'KCN catalyst, heat'],
# 	 ['S', 'alcohol', 'HX(g)', 'Xoalkane', 'H2O', ''],
# 	 ['SN', 'Xoalkane', 'AgNO3(aq)', 'alcohol', 'AgX(s)', 'ethanol'],
# 	 ['SN', 'Xoalkane', 'KCN', 'nitrile', 'KX', 'ethanol, heat'],
# 	 ['SN', 'Xoalkane', 'NH3', 'amine', 'HX', 'ethanol, heat, under pressure'],
# 	 ['SN', 'Xoalkane', 'NaOH(aq)', 'alcohol', 'NaX', 'heat'],
# 	 ['cracking', 'alkane', '', 'alkane', '', 'Al2O3 catalyst, heat'],
# 	 ['dehydration', 'alcohol', '', 'alkene', 'H2O', 'Al2O3 catalyst, heat'],
# 	 ['elimination', 'Xoalkane', 'NaOH(aq)', 'alkene', 'NaX, H2O', 'ethanol, heat'],
# 	 ['free-radical substitution', 'alkane', 'Cl2', 'Xoalkane', '', 'ultraviolet light'],
# ]
# arr = arr+arr2
# arr.sort()
# print(f'arr = [')
# for i in arr:
#     print(f'\t {i},')
# print(']')

arr = [
    ['AE', 'alkene', 'H2(g)', 'alkane', '', 'Pt/Ni catalyst, heat'],
    ['AE', 'alkene', 'H2O(g)', 'alcohol', '', 'H3PO4 catalyst'],
    ['AE', 'alkene', 'HX(g)', 'Xoalkane', '', 'room temp'],
    ['AE', 'alkene', 'X2', 'Xoalkane', '', ''],
    ['AN', 'aldehyde', 'HCN', 'hydroxynitrile', '', 'KCN catalyst, heat'],
    ['AN', 'ketone', 'HCN', 'hydroxynitrile', '', 'KCN catalyst, heat'],
    ['S', 'alcohol', 'HX(g)', 'Xoalkane', 'H2O', ''],
    ['S', 'alcohol', 'KCl', 'Xoalkane', 'H2O', 'conc. H2SO4'],
    ['S', 'alcohol', 'KCl', 'Xoalkane', 'H2O', 'conc. H3PO4'],
    ['S', 'alcohol', 'PCl3', 'Xoalkane', 'H3PO3', 'heat'],
    ['S', 'alcohol', 'PCl5', 'Xoalkane', 'HCl, POCl3', ''],
    ['S', 'alcohol', 'SOCl2', 'Xoalkane', 'HCl, SO2', ''],
    ['SN', 'Xoalkane', 'AgNO3(aq)', 'alcohol', 'AgX(s)', 'ethanol'],
    ['SN', 'Xoalkane', 'KCN', 'nitrile', 'KX', 'ethanol, heat q.r'],
    ['SN', 'Xoalkane', 'NH3', 'amine', 'NH4X', 'ethanol, heat, under pressure'],
    ['SN', 'Xoalkane', 'NaOH(aq)', 'alcohol', 'NaX', 'heat'],
    ['condensation', 'alcohol', 'carboxylic acid', 'ester', 'H2O', 'conc. H2SO4 catalyst, heat a.r'],
    ['cracking', 'alkane', '', 'alkane', 'alkene', 'Al2O3 catalyst, heat'],
    ['cracking', 'alkane', '', 'alkene', 'alkane', 'Al2O3 catalyst, heat'],
    ['dehydration', 'alcohol', '', 'alkene', 'H2O', 'Al2O3 catalyst, heat'],
    ['dehydration', 'alcohol', '', 'alkene', 'H2O', 'conc. H2SO4, heat'],
    ['dehydration', 'alcohol', '', 'alkene', 'H2O', 'conc. H3PO4, heat'],
    ['elimination', 'Xoalkane', 'NaOH(aq)', 'alkene', 'NaX, H2O', 'ethanol, heat a.r'],
    ['free-radical substitution', 'alkane', 'X2', 'Xoalkane', '', 'ultraviolet light'],
    ['hydrolysis', 'ester', 'H2O', 'carboxylic acid', 'alcohol', 'dilute acid, heat'],
    ['hydrolysis', 'ester', 'alkali', 'carboxylate salt', 'alcohol', 'dilute alkali, heat'],
    ['hydrolysis', 'nitrile', 'H2O', 'carboxylic acid', 'ammonium salt', 'dilute acid, heat'],
    ['hydrolysis', 'nitrile', 'alkali', 'carboxylate salt', 'NH3', 'dilute alkali, heat'],
]
unsure_arr = []

import random

try:
    cols_print = list(map(int, input('enter cols to show, separated by "," OR "rand": ').split(',')))
    cols_input = [x for x in range(0, 6) if x not in cols_print]
    rand = False
    rand_cols = 0
except ValueError:
    cols_print = []
    cols_input = []
    rand = True
    rand_cols = int(input('enter number of cols to show: '))


def test():
    def new_rxn():
        global arr, unsure_arr, cols_print, cols_input, rand, rand_cols
        cur_rxn = random.choice(arr)
        if rand:
            cols_print = random.sample(range(0, 6), rand_cols)
            cols_input = [x for x in range(0, 6) if x not in cols_print]
        for col in cols_print:
            print(f'{column_names[col]}{cur_rxn[col]}')
        input()

        for col in cols_input:
            print(f'{column_names[col]}{cur_rxn[col]}')
        order = input()
        arr.remove(cur_rxn)
        if order == 'n':
            unsure_arr.append(cur_rxn)
        if len(arr)>0:
            new_rxn()
        elif len(unsure_arr) >0 :
            print('You were unsure with these rxns. ')
            arr = unsure_arr.copy()
            unsure_arr.clear()
            new_rxn()
        else:
            input('congrats')
    new_rxn()
test()
