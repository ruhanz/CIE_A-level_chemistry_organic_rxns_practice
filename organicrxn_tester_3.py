import random
import pandas as pd
import numpy as np
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
    1: 'mechanism',
    2: 'organic reagent: ',
    3: 'inorganic reagent: ',
    4: 'organic product: ',
    5: 'inorganic product: ',
    6: 'conditions: '
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

arr1 = [
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

arr2 = [
    ['SE','SE','benzene', 'Cl2/Br2','Xobenzene','HX','cat AlX3',],
    ['SE','SE','methylbenzene', 'Cl2/Br2','2/4-Xomethylbenzene','HX','cat AlX3',],
    ['nitration','SE','benzene','HNO3','nitrobenzene','H2O','conc HNO3, conc H2SO4, temp 25C~60C'],
    ['nitration','SE','methylbenzene','HNO3','2/4-nitromethylbenzene','H2O','conc HNO3, conc H2SO4, temp 25C~60C'],
    ['Friedel-Crafts alkylation','SE','benzene','CH3Cl','methylbenzene','HCl','cat AlCl3, heat'],
    ['Friedel-Crafts acylation','SE','benzene','ethanoyl chloride','phenylethanone','HCl','cat AlCl3, heat'],
    ['complete oxidation','','methylbenzene','','benzoic acid','H2O','hot alkaline KMnO4; followed by dilute acid'],
    ['hydrogenation','AE','benzene','H2','cyclohexane','','cat Pt/Ni, heat'],
    ['esterification','AE','alcohol','acyl chloride','ester','HCl',''],
    ['diazotisation','','phenylamine','acid, HNO2/NaNO2','diazonium salt (e.g. benzenediazonium chloride)','H2O', 'dilute acid, temp <10C'],
    ['thermal decomposition','','diazonium salt','H2O','phenol','N2, H+','warming'],
    ['acid-base','','phenol','NaOH(aq)','sodium phenoxide','H2O',''],
    ['','','phenol','Na(s)','sodium phenoxide','H2(g)',''],
    ['','','phenol','diazonium salt','azo compound (4-hydroxyphenylazobenzene)','H+','in NaOH(aq)'],
    ['nitration','','phenol','HNO3(aq)','2/4-nitrophenol','H2O','dilute HNO3(aq), room temp'],
    ['bromination','','phenol','Br2(aq)','2,4,6-tribromophenol','HBr',''],
    ['S','','carboxylic acid','PCl3','acyl chloride','H3PO3','heat'],
    ['S','','carboxylic acid','PCl5','acyl chloride','POCl3, HCl',''],
    ['S','','carboxylic acid','SOCl2','acyl chloride','SO2, HCl',''],
    ['oxidation','','methanoic acid','','','CO2, H2O',"Fehling's reagent; Tollen's reagent; acidified KMnO4; acidified K2C2O7"],
    ['oxidation','','ethanedioic acid','','','CO2, H2O','warm acidified KMnO4'],
    ['hydrolysis','AE','acyl chloride','H2O','carboxylic acid','HCl','room temp'],
    ['esterification','AE','phenol','acyl chloride','ester','HCl','room temp'],
    ['condensation','AE','acyl chloride','ammonia','amide','HCl','room temp'],
    ['condensation','AE','acyl chloride','amine','amide','HCl','room temp'],
    ['SN','SN', 'Xoalkane', 'NH3', 'primary amine', 'HX', 'ethanol, heat, under pressure'],
    ['SN','SN', 'Xoalkane', 'primary amine', 'secondary amine', 'HX', 'ethanol, heat, under pressure/in a sealed tube'],
    ['reduction','','amide','','amine','H2O','LiAlH4'],
    ['reduction','','nitrile','','amine','','LiAlH4 OR H2/Ni'],
    ['reduction','','nitrobenzene','','phenylamine','H2O','hot Sn, conc HCl; followed by NaOH(aq)'],
    ['bromination','','phenylamine','Br2(aq)','2,4,6-tribromophenylamine','HBr','room temp'],
    ['hydrolysis','','amide','H2O','carboxylic acid','amine','aq acid'],
    ['hydrolysis','','amide','alkali','carboxylate salt','amine','aq alkali'],
    ['condensation polymerisation','','dicarboxylic acid','diol','polyester','H2O',''],
    ['condensation polymerisation','','dioyl chloride','diol','polyester','H2O',''],
    ['condensation polymerisation','','hydroxycarboxylic acid','','polyester','H2O',''],
    ['condensation polymerisation','','dicarboxylic acid','diamine','polyamide','H2O',''],
    ['condensation polymerisation','','dioyl chloride','diamine','polyamide','H2O',''],
    ['condensation polymerisation','','aminocarboxylic acid','','polyamide','H2O',''],
    ['condensation polymerisation','','amino acid','','polyamide','H2O',''],

]




unsure_arr = []
arr=None
max_col=0
rand = None
rand_cols = None
cols_input =None
cols_print = None

df = pd.DataFrame(arr2, columns=column_names.values())
cols=list(column_names.values())



def change_level():
    global max_col, arr
    lvl=int(input('Select from the following numbers:\n0: AS\n1: A2 \n2: both\n'))
    if lvl == 0:
        arr=arr1
        max_col=6
    elif lvl == 1:
        arr =arr2
        max_col=7

def test():
    global rand, rand_cols, cols_input, cols_print
    try:
        print('column_names:')
        for i in range(max_col):
            print(i, column_names[i])
        cols_print = list(map(int, input('enter cols to show, separated by "," OR "rand": ').split(',')))
        cols_input = [x for x in range(0, max_col) if x not in cols_print]
        rand = False
        rand_cols = 0
    except ValueError:
        cols_print = []
        cols_input = []
        rand = True
        rand_cols = int(input('enter number of cols to show: '))

    def new_rxn():
        global arr, unsure_arr, cols_print, cols_input
        cur_rxn = random.choice(arr)
        if rand:
            cols_print = random.sample(range(0, max_col), rand_cols)
            cols_input = [x for x in range(0, max_col) if x not in cols_print]
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

def mindmap():
    # if input('select from the following\n1: reagent to product\n2: product to reagent') == '1':
    #     choice = 2,3
    # else:
    #     choice = 4,5
    choice = 2,3
    substance='acyl chloride'
    print(df[(df[cols[choice[0]]]==substance)|(df[cols[choice[1]]]==substance)])
# pd.set_option('display.max_columns', None)
# print(df.sort_values(by=cols[0], ascending=True))
# print(df)
change_level()
test()
