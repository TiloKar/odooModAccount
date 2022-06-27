# -*- coding: utf-8 -*-

{
  'name': 'bbi_mod_account',
  'author': "Hanning Liu, Tilo Karczewski",
  'version': '0.10',
  'category': 'Accounting',
  'description': """
     - Anpassung des account_move forms für Übernahme des Wareningangsbuchs

    """,
  'depends': [
    'account',
    'purchase',
  ],
  'data': [
    'views/account_view_move_form_bbi.xml',
  ],
}
