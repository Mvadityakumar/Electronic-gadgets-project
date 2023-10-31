print('List of Eletronics mentioned below:\n'
      '1. Laptops\n'
      '2. Head Phones\n'
      '3. Smart watches\n')


types=int(input('Please enter your option:'))
print()
if (types==1):
      print('These are the top rated popular laptop brands on our store:\n'

    '(1)ASUS\t\t\t\t\t\t\t\t\t'                   '(2)DELL\t\t\t\t\t\t\t\t\t'           '(3)APPLE\t\t\t\t\t\t\t\t\t'            '(4)HP\t\t\t\t\t\t\t\t\t'                '(5)LENOVO\t\t\t\t\t\t\t\t\t\n'
      '1.1)ASUS  VIVOBOOK\t\t\t\t\t\t'            '2.1)INSPIRON\t\t\t\t\t\t\t'          '3.1)MACBOOK\t\t\t\t\t\t\t\t\t'         '4.1)PAVILION\t\t\t\t\t\t\t'             '5.1)IDELPAD\t\t\t\t\t\t\t\n'
            '1.2)ASUS FLIP SERIES\t\t\t\t\t'      '2.2)VOSTRO\t\t\t\t\t\t\t\t'          '3.2)MACBOOK AIR\t\t\t\t\t\t\t\t'       '4.2)VICTUS\t\t\t\t\t\t\t\t'             '5.2)SILMPAD\t\t\t\t\t\t\t\n'
            '1.3)ASUS ROG GAMING\t\t\t\t\t\t'     '2.3)XPS\t\t\t\t\t\t\t\t\t'           '3.3)MACBOOK PRO\t\t\t\t\t\t\t\t'       '4.3)ELITE BOOK\t\t\t\t\t\t\t'           '5.3)YOGA\t\t\t\t\t\t\t\n'
            '1.4)ASUS TUF\t\t\t\t\t\t\t'          '2.4)ALIEN WARE\t\t\t\t\t\t\t'            '\t\t\t\t\t\t\t\t\t\t\t'            '4.4)CHROME BOOK\t\t\t\t\t\t\t'          '5.4)THINKPAD\t\t\t\t\t\t\t\n'
            '\t\t\t\t\t\t\t\t\t\t'                    '2.5)G SERIES\t\t\t\t\t\t\t'            '\t\t\t\t\t\t\t\t\t\t\t'          '\t\t\t\t\t\t\t\t\t\t'                   '\t\t\t\t\t\t\t\t\t\t\n')
      print()
      brand=int(input(('Please select the brand:')))
      if brand==1:
          print('asus\t\t\t\t\t\t\t\t\t'                 'price\n'
                '1.1)ASUS VIVOBOOK\t\t\t\t\t\t'          '55000/-\n'
                '1.2)ASUS FLIP SERIES\t\t\t\t\t'         '79000/-\n'
                '1.3)ASUS ROG GAMING\t\t\t\t\t\t'        '88000/-\n'
                '1.4)ASUS TUF\t\t\t\t\t\t\t'             '82000/-\n')
          print('Please check the price details of your required series')
      elif brand==2:
          print('dell\t\t\t\t\t\t\t\t\t'                 'price\n'
                '2.1)INSPIRON\t\t\t\t\t\t\t'          '45000/-\n'
                '2.2)VOSTRO\t\t\t\t\t\t\t\t'         '49000/-\n'
                '2.3)XPS\t\t\t\t\t\t\t\t\t'        '68000/-\n'
                '2.4)ALIEN WARE\t\t\t\t\t\t\t'             '82000/-\n'
                '2.5)G SERIES\t\t\t\t\t\t\t'             '62000/-\n'
                )
          print('Please check the price details of your required series')
      elif brand==3:
          print('APPLE\t\t\t\t\t\t\t\t\t'                 'price\n'
                '3.1)MACBOOK\t\t\t\t\t\t\t\t'          '145000/-\n'
                '3.2)MACBOOK AIR\t\t\t\t\t\t\t'         '132000/-\n'
                '3.3)MACBOOK PRO\t\t\t\t\t\t\t'        '188000/-\n')
          print('Please check the price details of your required series')
      elif brand==4:
          print('HP\t\t\t\t\t\t\t\t\t'                 'price\n'
                '4.1)PAVILION\t\t\t\t\t\t'          '59000/-\n'
                '4.2)VICTUS\t\t\t\t\t\t\t'         '58000/-\n'
                '4.3)ELITE BOOK\t\t\t\t\t\t'        '64000/-\n'
                '4.4)CHROME BOOK\t\t\t\t\t\t'             '44000/-\n')
          print('Please check the price details of your required series')
      elif brand==5:
          print('LENOVO\t\t\t\t\t\t\t\t\t'                 'price\n'
                '5.1)IDELPAD\t\t\t\t\t\t\t\t'          '59000/-\n'
                '5.2)SLIMPAD\t\t\t\t\t\t\t\t'         '68000/-\n'
                '5.3)YOGA\t\t\t\t\t\t\t\t'        '74000/-\n'
                '5.4)THINKPAD\t\t\t\t\t\t\t'             '132000/-\n')
          print('Please check the price details of your required series')
      else:
          print('enter vaild option')

elif types==2:
    print('These are the top rated popular headset brands on our store:\n'

          '(1)BOAT\t\t\t\t\t\t\t\t\t'                   '(2)JBL\t\t\t\t\t\t\t\t\t'           '(3)BOULT\t\t\t\t\t\t\t\t\t\n'
          '1.1)BOAT ROCKERZ 4\t\t\t\t\t\t'            '2.1)JBL 5BT\t\t\t\t\t\t\t\t'          '3.1)BOULT AUDIO BASS\t\t\t\t\t\t\t\t\t\n'
          '1.2)BOAT ROCKERZ 5\t\t\t\t\t\t'      '2.2)JBL 7NCBLK\t\t\t\t\t\t\t'          '3.2)BOULT AUDIO PRO\t\t\t\t\t\t\t\t\n'
          '1.3)BOAT ROCKERZ 6\t\t\t\t\t\t'     '2.3)JBL 7NC\t\t\t\t\t\t\t\t'           '3.3)BOULT AIRBASS\t\t\t\t\t\t\t\t\n'
          )
    print()
    brand = int(input(('Please select the brand:')))
    if brand == 1:
        print('BOAT\t\t\t\t\t\t\t\t\t'                 'price\n'
              '1.1)BOAT ROCKERZ 4\t\t\t\t\t\t'          '1999/-\n'
              '1.2)BOAT ROCKERZ 5\t\t\t\t\t\t'         '2999/-\n'
              '1.3)BOAT ROCKERZ 6\t\t\t\t\t\t'        '3999/-\n'
              )
        print('Please check the price details of your required series')
    elif brand == 2:
        print('JBL\t\t\t\t\t\t\t\t\t'                 'price\n'
              '1.1)JBL 5BT 4\t\t\t\t\t\t'          '2500/-\n'
              '1.2)JBL 7NCBLK 5\t\t\t\t\t'         '3200/-\n'
              '1.3)JBL 7NC 6\t\t\t\t\t\t'        '4500/-\n'
              )
        print('Please check the price details of your required series')
    elif brand == 3:
        print('BOULT\t\t\t\t\t\t\t\t\t\t'                 'price\n'
              '3.1)BOULT AUDIO BASS\t\t\t\t\t\t'          '2999/-\n'
              '3.2)BOULT AUDIO PRO\t\t\t\t\t\t\t'         '3999/-\n'
              '3.3)BOULT AIRBASS\t\t\t\t\t\t\t'        '4499/-\n')
        print('Please check the price details of your required series')
    else:
        print('enter vaild option')


elif types==3:
    print('These are the top rated popular smart watch brands on our store:\n'

          '(1)NOISE\t\t\t\t\t\t\t\t\t'                   '(2)FIRE-BOLTT\t\t\t\t\t\t\t\t\t'           '(3)JABRA\t\t\t\t\t\t\t\t\t\n'
          '1.1)EVOLVE\t\t\t\t\t\t\t\t\t'            '2.1)DAZZLE PLUS\t\t\t\t\t\t\t\t\t'          '3.1)BINGO F0S\t\t\t\t\t\t\t\t\t\n'
          '1.2)ICON BUZZ\t\t\t\t\t\t\t\t'      '2.2)EPIC PLUS\t\t\t\t\t\t\t\t\t'          '3.2)BINGO F1S\t\t\t\t\t\t\t\t\n'
          '1.3)COLORFIT PULSE\t\t\t\t\t\t\t'     '2.3)ROCKET\t\t\t\t\t\t\t\t\t\t'           '3.3)BINGO F6S\t\t\t\t\t\t\t\t\n'
          )
    print()
    brand = int(input(('Please select the brand:')))
    if brand == 1:
        print('NOISE\t\t\t\t\t\t\t\t\t'                 'price\n'
              '1.1)EVOLVE\t\t\t\t\t\t\t\t'          '999/-\n'
              '1.2)ICON BUZZ\t\t\t\t\t\t\t'         '1999/-\n'
              '1.3)COLORFIT PULSE\t\t\t\t\t\t'        '2499/-\n'
              )
        print('Please check the price details of your required series')
    elif brand == 2:
        print('FIRE-BOLTT\t\t\t\t\t\t\t\t\t'                 'price\n'
              '2.1)DAZZLE PLUS\t\t\t\t\t\t\t\t'          '1999/-\n'
              '2.2)EPIC PLUS\t\t\t\t\t\t\t\t'         '2999/-\n'
              '2.3)ROCKET\t\t\t\t\t\t\t\t\t'        '3499/-\n'
              )
        print('Please check the price details of your required series')
    elif brand == 3:
        print('JABRA\t\t\t\t\t\t\t\t\t\t'                 'price\n'
              '3.1)BINGO F0S\t\t\t\t\t\t\t\t'          '2999/-\n'
              '3.2)BINGO F1S\t\t\t\t\t\t\t\t'         '4999/-\n'
              '3.3)BINGO F6S\t\t\t\t\t\t\t\t'        '5999/-\n')
        print('Please check the price details of your required series')
    else:
        print('enter vaild option')
else:
    print('enter vaild option')



