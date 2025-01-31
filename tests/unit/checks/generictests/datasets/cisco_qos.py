#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore



checkname = 'cisco_qos'


info = [[[u'225', u'84'],
         [u'1248', u'78'],
         [u'1250', u'78'],
         [u'1392', u'87'],
         [u'1394', u'87'],
         [u'1408', u'88'],
         [u'1410', u'88'],
         [u'2080', u'130'],
         [u'2082', u'130']],
        [[u'423488', u'cos-pol-VPN-INT1_C7'],
         [u'3596928', u'copp-policy'],
         [u'7955776', u'cos-pol-VPN-INT1_C14'],
         [u'7956256', u'cos-pol-VPN-INT1_C32'],
         [u'7956304', u'cos-pol-VPN-INT1_C35']],
        [[u'1593', u'class-default'],
         [u'1974129', u'copp-monitoring'],
         [u'2812097', u'copp-undesirable'],
         [u'3458881', u'copp-arp'],
         [u'3459137', u'copp-bgp'],
         [u'3943617', u'copp-critical-app'],
         [u'4164417', u'cos-map-c7_VPN-INT1'],
         [u'8625617', u'copp-reporting'],
         [u'11195249', u'cos-map-c14_VPN-INT1'],
         [u'12078609', u'copp-management'],
         [u'13357937', u'cos-map-c35_VPN-INT1'],
         [u'13423473', u'cos-map-c32_VPN-INT1']],
        [[u'225.225', u'3596928'],
         [u'225.2000883', u'15123939'],
         [u'225.2121537', u'2812097'],
         [u'225.2215201', u'12078609'],
         [u'225.4146434', u'11165954'],
         [u'225.4397474', u'1594'],
         [u'225.4553043', u'12809827'],
         [u'225.5003170', u'13597522'],
         [u'225.5759266', u'5626594'],
         [u'225.6427570', u'13295346'],
         [u'225.6501313', u'8625617'],
         [u'225.7030675', u'11344963'],
         [u'225.8444705', u'3458881'],
         [u'225.8444961', u'3459137'],
         [u'225.9294625', u'3943617'],
         [u'225.9318433', u'1593'],
         [u'225.9766803', u'11410499'],
         [u'225.10057635', u'11607539'],
         [u'225.13216354', u'11857778'],
         [u'225.13232179', u'708867'],
         [u'225.14174739', u'10575619'],
         [u'225.14445266', u'5460850'],
         [u'225.14851394', u'13217138'],
         [u'225.15220035', u'3335699'],
         [u'225.15400241', u'1974129'],
         [u'1248.1248', u'7955776'],
         [u'1248.1627154', u'1594'],
         [u'1248.1726081', u'11195249'],
         [u'1248.3668898', u'5349330'],
         [u'1248.8033249', u'1593'],
         [u'1248.8877715', u'1949187'],
         [u'1250.1250', u'7955776'],
         [u'1250.906402', u'5349330'],
         [u'1250.1431090', u'1594'],
         [u'1250.3857235', u'1949187'],
         [u'1250.8262625', u'1593'],
         [u'1250.10638977', u'11195249'],
         [u'1392.1392', u'7956256'],
         [u'1392.5957057', u'13423473'],
         [u'1392.9597921', u'1593'],
         [u'1392.10598034', u'1594'],
         [u'1392.15137315', u'5058243'],
         [u'1392.15632130', u'5343698'],
         [u'1394.1394', u'7956256'],
         [u'1394.5944547', u'5058243'],
         [u'1394.6088129', u'13423473'],
         [u'1394.8890434', u'5343698'],
         [u'1394.8951170', u'1594'],
         [u'1394.9622497', u'1593'],
         [u'1408.1408', u'423488'],
         [u'1408.612785', u'4164417'],
         [u'1408.857043', u'15039475'],
         [u'1408.9868257', u'1593'],
         [u'1408.10106402', u'959922'],
         [u'1408.12891234', u'1594'],
         [u'1410.1410', u'423488'],
         [u'1410.907697', u'4164417'],
         [u'1410.4419154', u'959922'],
         [u'1410.4589426', u'1594'],
         [u'1410.7349907', u'15039475'],
         [u'1410.10097633', u'1593'],
         [u'2080.2080', u'7956304'],
         [u'2080.4795219', u'6612771'],
         [u'2080.7470802', u'5343954'],
         [u'2080.12322642', u'1594'],
         [u'2080.13711281', u'1593'],
         [u'2080.14585393', u'13357937'],
         [u'2082.2082', u'7956304'],
         [u'2082.12655506', u'5343954'],
         [u'2082.13344034', u'1594'],
         [u'2082.13735857', u'1593'],
         [u'2082.13789027', u'6612771'],
         [u'2082.14716465', u'13357937']],
        [[u'225.2121537', u'191030'],
         [u'225.2215201', u'703772366'],
         [u'225.6501313', u'67356642'],
         [u'225.8444705', u'0'],
         [u'225.8444961', u'730158815'],
         [u'225.9294625', u'0'],
         [u'225.9318433', u'1330302675'],
         [u'225.15400241', u'3934444'],
         [u'1248.1726081', u'0'],
         [u'1250.10638977', u'468837662'],
         [u'1392.5957057', u'0'],
         [u'1394.6088129', u'462395629'],
         [u'1408.612785', u'0'],
         [u'1410.907697', u'496675588'],
         [u'2080.14585393', u'0'],
         [u'2082.14716465', u'462212382']],
        [[u'225.2121537', u'0'],
         [u'225.2215201', u'0'],
         [u'225.6501313', u'0'],
         [u'225.8444705', u'0'],
         [u'225.8444961', u'0'],
         [u'225.9294625', u'0'],
         [u'225.9318433', u'2096'],
         [u'225.15400241', u'89208'],
         [u'1248.1726081', u'0'],
         [u'1250.10638977', u'0'],
         [u'1392.5957057', u'0'],
         [u'1394.6088129', u'0'],
         [u'1408.612785', u'0'],
         [u'1410.907697', u'0'],
         [u'2080.14585393', u'0'],
         [u'2082.14716465', u'0']],
        [[u'7', u'TenGigabitEthernet4/1'],
         [u'8', u'TenGigabitEthernet4/2'],
         [u'9', u'TenGigabitEthernet4/3'],
         [u'10', u'TenGigabitEthernet4/4'],
         [u'11', u'GigabitEthernet5/1'],
         [u'12', u'GigabitEthernet5/2'],
         [u'13', u'GigabitEthernet7/1'],
         [u'14', u'GigabitEthernet7/2'],
         [u'15', u'GigabitEthernet7/3'],
         [u'16', u'GigabitEthernet7/4'],
         [u'17', u'GigabitEthernet7/5'],
         [u'18', u'GigabitEthernet7/6'],
         [u'19', u'GigabitEthernet7/7'],
         [u'20', u'GigabitEthernet7/8'],
         [u'21', u'GigabitEthernet7/9'],
         [u'22', u'GigabitEthernet7/10'],
         [u'23', u'GigabitEthernet7/11'],
         [u'24', u'GigabitEthernet7/12'],
         [u'25', u'GigabitEthernet7/13'],
         [u'26', u'GigabitEthernet7/14'],
         [u'27', u'GigabitEthernet7/15'],
         [u'28', u'GigabitEthernet7/16'],
         [u'29', u'GigabitEthernet7/17'],
         [u'30', u'GigabitEthernet7/18'],
         [u'31', u'GigabitEthernet7/19'],
         [u'32', u'GigabitEthernet7/20'],
         [u'33', u'GigabitEthernet7/21'],
         [u'34', u'GigabitEthernet7/22'],
         [u'35', u'GigabitEthernet7/23'],
         [u'36', u'GigabitEthernet7/24'],
         [u'37', u'GigabitEthernet7/25'],
         [u'38', u'GigabitEthernet7/26'],
         [u'39', u'GigabitEthernet7/27'],
         [u'40', u'GigabitEthernet7/28'],
         [u'41', u'GigabitEthernet7/29'],
         [u'42', u'GigabitEthernet7/30'],
         [u'43', u'GigabitEthernet7/31'],
         [u'44', u'GigabitEthernet7/32'],
         [u'45', u'GigabitEthernet7/33'],
         [u'46', u'GigabitEthernet7/34'],
         [u'47', u'GigabitEthernet7/35'],
         [u'48', u'GigabitEthernet7/36'],
         [u'49', u'GigabitEthernet7/37'],
         [u'50', u'GigabitEthernet7/38'],
         [u'51', u'GigabitEthernet7/39'],
         [u'52', u'GigabitEthernet7/40'],
         [u'53', u'GigabitEthernet7/41'],
         [u'54', u'GigabitEthernet7/42'],
         [u'55', u'GigabitEthernet7/43'],
         [u'56', u'GigabitEthernet7/44'],
         [u'57', u'GigabitEthernet7/45'],
         [u'58', u'GigabitEthernet7/46'],
         [u'59', u'GigabitEthernet7/47'],
         [u'60', u'GigabitEthernet7/48'],
         [u'61', u'Vlan1'],
         [u'62', u'EOBC0/0'],
         [u'63', u'Null0'],
         [u'65', u'unrouted VLAN 1'],
         [u'66', u'unrouted VLAN 1002'],
         [u'67', u'unrouted VLAN 1004'],
         [u'68', u'unrouted VLAN 1005'],
         [u'69', u'unrouted VLAN 1003'],
         [u'72', u'unrouted VLAN 714'],
         [u'74', u'unrouted VLAN 715'],
         [u'76', u'Port-channel1'],
         [u'77', u'unrouted VLAN 100'],
         [u'78', u'Vlan100'],
         [u'79', u'unrouted VLAN 101'],
         [u'80', u'unrouted VLAN 200'],
         [u'81', u'Vlan200'],
         [u'82', u'SPAN RP Interface'],
         [u'83', u'SPAN SP Interface'],
         [u'84', u'Control Plane Interface'],
         [u'86', u'unrouted VLAN 102'],
         [u'87', u'Vlan101'],
         [u'88', u'Vlan102'],
         [u'89', u'unrouted VLAN 201'],
         [u'92', u'unrouted VLAN 300'],
         [u'93', u'unrouted VLAN 306'],
         [u'94', u'unrouted VLAN 307'],
         [u'95', u'unrouted VLAN 315'],
         [u'97', u'unrouted VLAN 202'],
         [u'98', u'unrouted VLAN 203'],
         [u'99', u'unrouted VLAN 103'],
         [u'101', u'unrouted VLAN 514'],
         [u'102', u'Vlan514'],
         [u'103', u'unrouted VLAN 732'],
         [u'105', u'TenGigabitEthernet1/1'],
         [u'106', u'unrouted VLAN 414'],
         [u'107', u'unrouted VLAN 415'],
         [u'108', u'unrouted VLAN 418'],
         [u'109', u'unrouted VLAN 419'],
         [u'110', u'unrouted VLAN 420'],
         [u'111', u'unrouted VLAN 424'],
         [u'112', u'unrouted VLAN 425'],
         [u'113', u'unrouted VLAN 421'],
         [u'114', u'unrouted VLAN 422'],
         [u'115', u'unrouted VLAN 154'],
         [u'116', u'unrouted VLAN 503'],
         [u'117', u'unrouted VLAN 317'],
         [u'118', u'unrouted VLAN 617'],
         [u'119', u'Vlan154'],
         [u'120', u'unrouted VLAN 105'],
         [u'122', u'Vlan421'],
         [u'123', u'Vlan422'],
         [u'124', u'Vlan419'],
         [u'125', u'Vlan420'],
         [u'126', u'unrouted VLAN 316'],
         [u'127', u'Vlan316'],
         [u'128', u'Vlan317'],
         [u'129', u'unrouted VLAN 106'],
         [u'130', u'Vlan106'],
         [u'131', u'Vlan424'],
         [u'132', u'Vlan425'],
         [u'133', u'Vlan414'],
         [u'134', u'Vlan415'],
         [u'135', u'Vlan306'],
         [u'136', u'Vlan315'],
         [u'137', u'unrouted VLAN 204'],
         [u'138', u'Vlan203'],
         [u'139', u'Vlan204'],
         [u'140', u'unrouted VLAN 318'],
         [u'141', u'unrouted VLAN 426'],
         [u'142', u'unrouted VLAN 427'],
         [u'144', u'Vlan427'],
         [u'147', u'unrouted VLAN 606'],
         [u'148', u'GigabitEthernet8/1'],
         [u'149', u'GigabitEthernet8/2'],
         [u'150', u'GigabitEthernet8/3'],
         [u'151', u'GigabitEthernet8/4'],
         [u'152', u'GigabitEthernet8/5'],
         [u'153', u'GigabitEthernet8/6'],
         [u'154', u'GigabitEthernet8/7'],
         [u'155', u'GigabitEthernet8/8'],
         [u'156', u'GigabitEthernet8/9'],
         [u'157', u'GigabitEthernet8/10'],
         [u'158', u'GigabitEthernet8/11'],
         [u'159', u'GigabitEthernet8/12'],
         [u'160', u'GigabitEthernet8/13'],
         [u'161', u'GigabitEthernet8/14'],
         [u'162', u'GigabitEthernet8/15'],
         [u'163', u'GigabitEthernet8/16'],
         [u'164', u'GigabitEthernet8/17'],
         [u'165', u'GigabitEthernet8/18'],
         [u'166', u'GigabitEthernet8/19'],
         [u'167', u'GigabitEthernet8/20'],
         [u'168', u'GigabitEthernet8/21'],
         [u'169', u'GigabitEthernet8/22'],
         [u'170', u'GigabitEthernet8/23'],
         [u'171', u'GigabitEthernet8/24'],
         [u'172', u'GigabitEthernet8/25'],
         [u'173', u'GigabitEthernet8/26'],
         [u'174', u'GigabitEthernet8/27'],
         [u'175', u'GigabitEthernet8/28'],
         [u'176', u'GigabitEthernet8/29'],
         [u'177', u'GigabitEthernet8/30'],
         [u'178', u'GigabitEthernet8/31'],
         [u'179', u'GigabitEthernet8/32'],
         [u'180', u'GigabitEthernet8/33'],
         [u'181', u'GigabitEthernet8/34'],
         [u'182', u'GigabitEthernet8/35'],
         [u'183', u'GigabitEthernet8/36'],
         [u'184', u'GigabitEthernet8/37'],
         [u'185', u'GigabitEthernet8/38'],
         [u'186', u'GigabitEthernet8/39'],
         [u'187', u'GigabitEthernet8/40'],
         [u'188', u'GigabitEthernet8/41'],
         [u'189', u'GigabitEthernet8/42'],
         [u'190', u'GigabitEthernet8/43'],
         [u'191', u'GigabitEthernet8/44'],
         [u'192', u'GigabitEthernet8/45'],
         [u'193', u'GigabitEthernet8/46'],
         [u'194', u'GigabitEthernet8/47'],
         [u'195', u'GigabitEthernet8/48'],
         [u'197', u'Port-channel2'],
         [u'199', u'unrouted VLAN 321'],
         [u'200', u'unrouted VLAN 322'],
         [u'201', u'Vlan321'],
         [u'202', u'unrouted VLAN 432'],
         [u'203', u'Vlan432'],
         [u'204', u'unrouted VLAN 435'],
         [u'205', u'unrouted VLAN 436'],
         [u'208', u'Vlan436'],
         [u'209', u'GigabitEthernet3/1'],
         [u'210', u'GigabitEthernet3/2'],
         [u'211', u'GigabitEthernet3/3'],
         [u'212', u'GigabitEthernet3/4'],
         [u'213', u'GigabitEthernet3/5'],
         [u'214', u'GigabitEthernet3/6'],
         [u'215', u'GigabitEthernet3/7'],
         [u'216', u'GigabitEthernet3/8'],
         [u'217', u'GigabitEthernet3/9'],
         [u'218', u'GigabitEthernet3/10'],
         [u'219', u'GigabitEthernet3/11'],
         [u'220', u'GigabitEthernet3/12'],
         [u'221', u'GigabitEthernet3/13'],
         [u'222', u'GigabitEthernet3/14'],
         [u'223', u'GigabitEthernet3/15'],
         [u'224', u'GigabitEthernet3/16'],
         [u'225', u'Vlan322'],
         [u'226', u'unrouted VLAN 434'],
         [u'227', u'Vlan434'],
         [u'231', u'GigabitEthernet6/1'],
         [u'232', u'GigabitEthernet6/2'],
         [u'233', u'TenGigabitEthernet4/4.1053'],
         [u'234', u'unrouted VLAN 1053 for TenGigabitEthernet4/4.1053'],
         [u'235', u'TenGigabitEthernet4/4.1103'],
         [u'236', u'unrouted VLAN 1103 for TenGigabitEthernet4/4.1103'],
         [u'237', u'TenGigabitEthernet4/4.1105'],
         [u'238', u'unrouted VLAN 1105 for TenGigabitEthernet4/4.1105'],
         [u'239', u'Vlan1106'],
         [u'240', u'Vlan1054'],
         [u'241', u'Vlan1107'],
         [u'242', u'unrouted VLAN 1054'],
         [u'243', u'unrouted VLAN 1106'],
         [u'244', u'unrouted VLAN 1107'],
         [u'245', u'Vlan732'],
         [u'246', u'unrouted VLAN 205'],
         [u'247', u'Vlan205'],
         [u'248', u'unrouted VLAN 416'],
         [u'249', u'unrouted VLAN 324'],
         [u'250', u'Vlan324'],
         [u'251', u'Vlan416'],
         [u'252', u'unrouted VLAN 331'],
         [u'253', u'unrouted VLAN 332'],
         [u'254', u'Vlan331'],
         [u'255', u'Vlan332'],
         [u'256', u'unrouted VLAN 325'],
         [u'257', u'Vlan325'],
         [u'258', u'unrouted VLAN 162'],
         [u'259', u'Vlan162'],
         [u'260', u'unrouted VLAN 423'],
         [u'261', u'Vlan423'],
         [u'262', u'unrouted VLAN 616']],
        [[u'7', u'4294967295'],
         [u'8', u'4294967295'],
         [u'9', u'4294967295'],
         [u'10', u'4294967295'],
         [u'11', u'1000000000'],
         [u'12', u'1000000000'],
         [u'13', u'1000000000'],
         [u'14', u'1000000000'],
         [u'15', u'1000000000'],
         [u'16', u'1000000000'],
         [u'17', u'1000000000'],
         [u'18', u'1000000000'],
         [u'19', u'1000000000'],
         [u'20', u'1000000000'],
         [u'21', u'1000000000'],
         [u'22', u'1000000000'],
         [u'23', u'1000000000'],
         [u'24', u'1000000000'],
         [u'25', u'100000000'],
         [u'26', u'100000000'],
         [u'27', u'1000000000'],
         [u'28', u'100000000'],
         [u'29', u'1000000000'],
         [u'30', u'1000000000'],
         [u'31', u'100000000'],
         [u'32', u'100000000'],
         [u'33', u'1000000000'],
         [u'34', u'100000000'],
         [u'35', u'100000000'],
         [u'36', u'100000000'],
         [u'37', u'1000000000'],
         [u'38', u'1000000000'],
         [u'39', u'1000000000'],
         [u'40', u'1000000000'],
         [u'41', u'1000000000'],
         [u'42', u'1000000000'],
         [u'43', u'1000000000'],
         [u'44', u'1000000000'],
         [u'45', u'1000000000'],
         [u'46', u'1000000000'],
         [u'47', u'1000000000'],
         [u'48', u'1000000000'],
         [u'49', u'1000000000'],
         [u'50', u'1000000000'],
         [u'51', u'1000000000'],
         [u'52', u'1000000000'],
         [u'53', u'1000000000'],
         [u'54', u'100000000'],
         [u'55', u'100000000'],
         [u'56', u'1000000000'],
         [u'57', u'1000000000'],
         [u'58', u'1000000000'],
         [u'59', u'1000000000'],
         [u'60', u'1000000000'],
         [u'61', u'1000000000'],
         [u'62', u'100000000'],
         [u'63', u'4294967295'],
         [u'65', u'0'],
         [u'66', u'0'],
         [u'67', u'0'],
         [u'68', u'0'],
         [u'69', u'0'],
         [u'72', u'0'],
         [u'74', u'0'],
         [u'76', u'4294967295'],
         [u'77', u'0'],
         [u'78', u'1000000000'],
         [u'79', u'0'],
         [u'80', u'0'],
         [u'81', u'1000000000'],
         [u'82', u'4294967295'],
         [u'83', u'4294967295'],
         [u'84', u'4294967295'],
         [u'86', u'0'],
         [u'87', u'1000000000'],
         [u'88', u'1000000000'],
         [u'89', u'0'],
         [u'92', u'0'],
         [u'93', u'0'],
         [u'94', u'0'],
         [u'95', u'0'],
         [u'97', u'0'],
         [u'98', u'0'],
         [u'99', u'0'],
         [u'101', u'0'],
         [u'102', u'1000000000'],
         [u'103', u'0'],
         [u'105', u'4294967295'],
         [u'106', u'0'],
         [u'107', u'0'],
         [u'108', u'0'],
         [u'109', u'0'],
         [u'110', u'0'],
         [u'111', u'0'],
         [u'112', u'0'],
         [u'113', u'0'],
         [u'114', u'0'],
         [u'115', u'0'],
         [u'116', u'0'],
         [u'117', u'0'],
         [u'118', u'0'],
         [u'119', u'1000000000'],
         [u'120', u'0'],
         [u'122', u'1000000000'],
         [u'123', u'1000000000'],
         [u'124', u'1000000000'],
         [u'125', u'1000000000'],
         [u'126', u'0'],
         [u'127', u'1000000000'],
         [u'128', u'1000000000'],
         [u'129', u'0'],
         [u'130', u'1000000000'],
         [u'131', u'1000000000'],
         [u'132', u'1000000000'],
         [u'133', u'1000000000'],
         [u'134', u'1000000000'],
         [u'135', u'1000000000'],
         [u'136', u'1000000000'],
         [u'137', u'0'],
         [u'138', u'1000000000'],
         [u'139', u'1000000000'],
         [u'140', u'0'],
         [u'141', u'0'],
         [u'142', u'0'],
         [u'144', u'1000000000'],
         [u'147', u'0'],
         [u'148', u'1000000000'],
         [u'149', u'1000000000'],
         [u'150', u'1000000000'],
         [u'151', u'1000000000'],
         [u'152', u'1000000000'],
         [u'153', u'1000000000'],
         [u'154', u'100000000'],
         [u'155', u'100000000'],
         [u'156', u'100000000'],
         [u'157', u'100000000'],
         [u'158', u'100000000'],
         [u'159', u'100000000'],
         [u'160', u'100000000'],
         [u'161', u'100000000'],
         [u'162', u'100000000'],
         [u'163', u'100000000'],
         [u'164', u'1000000000'],
         [u'165', u'1000000000'],
         [u'166', u'100000000'],
         [u'167', u'1000000000'],
         [u'168', u'1000000000'],
         [u'169', u'1000000000'],
         [u'170', u'1000000000'],
         [u'171', u'1000000000'],
         [u'172', u'1000000000'],
         [u'173', u'1000000000'],
         [u'174', u'1000000000'],
         [u'175', u'1000000000'],
         [u'176', u'1000000000'],
         [u'177', u'1000000000'],
         [u'178', u'1000000000'],
         [u'179', u'1000000000'],
         [u'180', u'1000000000'],
         [u'181', u'1000000000'],
         [u'182', u'1000000000'],
         [u'183', u'1000000000'],
         [u'184', u'1000000000'],
         [u'185', u'1000000000'],
         [u'186', u'100000000'],
         [u'187', u'1000000000'],
         [u'188', u'1000000000'],
         [u'189', u'1000000000'],
         [u'190', u'1000000000'],
         [u'191', u'1000000000'],
         [u'192', u'1000000000'],
         [u'193', u'1000000000'],
         [u'194', u'1000000000'],
         [u'195', u'1000000000'],
         [u'197', u'2000000000'],
         [u'199', u'0'],
         [u'200', u'0'],
         [u'201', u'1000000000'],
         [u'202', u'0'],
         [u'203', u'1000000000'],
         [u'204', u'0'],
         [u'205', u'0'],
         [u'208', u'1000000000'],
         [u'209', u'1000000000'],
         [u'210', u'1000000000'],
         [u'211', u'1000000000'],
         [u'212', u'1000000000'],
         [u'213', u'1000000000'],
         [u'214', u'1000000000'],
         [u'215', u'1000000000'],
         [u'216', u'1000000000'],
         [u'217', u'1000000000'],
         [u'218', u'1000000000'],
         [u'219', u'1000000000'],
         [u'220', u'1000000000'],
         [u'221', u'1000000000'],
         [u'222', u'1000000000'],
         [u'223', u'1000000000'],
         [u'224', u'1000000000'],
         [u'225', u'1000000000'],
         [u'226', u'0'],
         [u'227', u'1000000000'],
         [u'231', u'1000000000'],
         [u'232', u'1000000000'],
         [u'233', u'4294967295'],
         [u'234', u'0'],
         [u'235', u'4294967295'],
         [u'236', u'0'],
         [u'237', u'4294967295'],
         [u'238', u'0'],
         [u'239', u'1000000000'],
         [u'240', u'1000000000'],
         [u'241', u'1000000000'],
         [u'242', u'0'],
         [u'243', u'0'],
         [u'244', u'0'],
         [u'245', u'1000000000'],
         [u'246', u'0'],
         [u'247', u'1000000000'],
         [u'248', u'0'],
         [u'249', u'0'],
         [u'250', u'1000000000'],
         [u'251', u'1000000000'],
         [u'252', u'0'],
         [u'253', u'0'],
         [u'254', u'1000000000'],
         [u'255', u'1000000000'],
         [u'256', u'0'],
         [u'257', u'1000000000'],
         [u'258', u'0'],
         [u'259', u'1000000000'],
         [u'260', u'0'],
         [u'261', u'1000000000'],
         [u'262', u'0']],
        [[u'225.225', u'0'],
         [u'225.2000883', u'9318433'],
         [u'225.2121537', u'225'],
         [u'225.2215201', u'225'],
         [u'225.4146434', u'6501313'],
         [u'225.4397474', u'9318433'],
         [u'225.4553043', u'9294625'],
         [u'225.5003170', u'8444705'],
         [u'225.5759266', u'2215201'],
         [u'225.6427570', u'9294625'],
         [u'225.6501313', u'225'],
         [u'225.7030675', u'8444705'],
         [u'225.8444705', u'225'],
         [u'225.8444961', u'225'],
         [u'225.9294625', u'225'],
         [u'225.9318433', u'225'],
         [u'225.9766803', u'8444961'],
         [u'225.10057635', u'2121537'],
         [u'225.13216354', u'2121537'],
         [u'225.13232179', u'2215201'],
         [u'225.14174739', u'15400241'],
         [u'225.14445266', u'15400241'],
         [u'225.14851394', u'8444961'],
         [u'225.15220035', u'6501313'],
         [u'225.15400241', u'225'],
         [u'1248.1248', u'0'],
         [u'1248.1627154', u'8033249'],
         [u'1248.1726081', u'1248'],
         [u'1248.3668898', u'1726081'],
         [u'1248.8033249', u'1248'],
         [u'1248.8877715', u'1726081'],
         [u'1250.1250', u'0'],
         [u'1250.906402', u'10638977'],
         [u'1250.1431090', u'8262625'],
         [u'1250.3857235', u'10638977'],
         [u'1250.8262625', u'1250'],
         [u'1250.10638977', u'1250'],
         [u'1392.1392', u'0'],
         [u'1392.5957057', u'1392'],
         [u'1392.9597921', u'1392'],
         [u'1392.10598034', u'9597921'],
         [u'1392.15137315', u'5957057'],
         [u'1392.15632130', u'5957057'],
         [u'1394.1394', u'0'],
         [u'1394.5944547', u'6088129'],
         [u'1394.6088129', u'1394'],
         [u'1394.8890434', u'6088129'],
         [u'1394.8951170', u'9622497'],
         [u'1394.9622497', u'1394'],
         [u'1408.1408', u'0'],
         [u'1408.612785', u'1408'],
         [u'1408.857043', u'612785'],
         [u'1408.9868257', u'1408'],
         [u'1408.10106402', u'612785'],
         [u'1408.12891234', u'9868257'],
         [u'1410.1410', u'0'],
         [u'1410.907697', u'1410'],
         [u'1410.4419154', u'907697'],
         [u'1410.4589426', u'10097633'],
         [u'1410.7349907', u'907697'],
         [u'1410.10097633', u'1410'],
         [u'2080.2080', u'0'],
         [u'2080.4795219', u'14585393'],
         [u'2080.7470802', u'14585393'],
         [u'2080.12322642', u'13711281'],
         [u'2080.13711281', u'2080'],
         [u'2080.14585393', u'2080'],
         [u'2082.2082', u'0'],
         [u'2082.12655506', u'14716465'],
         [u'2082.13344034', u'13735857'],
         [u'2082.13735857', u'2082'],
         [u'2082.13789027', u'14716465'],
         [u'2082.14716465', u'2082']],
        [],
        [],
        [[u'225.225', u'1'],
         [u'225.2000883', u'7'],
         [u'225.2121537', u'2'],
         [u'225.2215201', u'2'],
         [u'225.4146434', u'3'],
         [u'225.4397474', u'3'],
         [u'225.4553043', u'7'],
         [u'225.5003170', u'3'],
         [u'225.5759266', u'3'],
         [u'225.6427570', u'3'],
         [u'225.6501313', u'2'],
         [u'225.7030675', u'7'],
         [u'225.8444705', u'2'],
         [u'225.8444961', u'2'],
         [u'225.9294625', u'2'],
         [u'225.9318433', u'2'],
         [u'225.9766803', u'7'],
         [u'225.10057635', u'7'],
         [u'225.13216354', u'3'],
         [u'225.13232179', u'7'],
         [u'225.14174739', u'7'],
         [u'225.14445266', u'3'],
         [u'225.14851394', u'3'],
         [u'225.15220035', u'7'],
         [u'225.15400241', u'2'],
         [u'1248.1248', u'1'],
         [u'1248.1627154', u'3'],
         [u'1248.1726081', u'2'],
         [u'1248.3668898', u'3'],
         [u'1248.8033249', u'2'],
         [u'1248.8877715', u'7'],
         [u'1250.1250', u'1'],
         [u'1250.906402', u'3'],
         [u'1250.1431090', u'3'],
         [u'1250.3857235', u'7'],
         [u'1250.8262625', u'2'],
         [u'1250.10638977', u'2'],
         [u'1392.1392', u'1'],
         [u'1392.5957057', u'2'],
         [u'1392.9597921', u'2'],
         [u'1392.10598034', u'3'],
         [u'1392.15137315', u'7'],
         [u'1392.15632130', u'3'],
         [u'1394.1394', u'1'],
         [u'1394.5944547', u'7'],
         [u'1394.6088129', u'2'],
         [u'1394.8890434', u'3'],
         [u'1394.8951170', u'3'],
         [u'1394.9622497', u'2'],
         [u'1408.1408', u'1'],
         [u'1408.612785', u'2'],
         [u'1408.857043', u'7'],
         [u'1408.9868257', u'2'],
         [u'1408.10106402', u'3'],
         [u'1408.12891234', u'3'],
         [u'1410.1410', u'1'],
         [u'1410.907697', u'2'],
         [u'1410.4419154', u'3'],
         [u'1410.4589426', u'3'],
         [u'1410.7349907', u'7'],
         [u'1410.10097633', u'2'],
         [u'2080.2080', u'1'],
         [u'2080.4795219', u'7'],
         [u'2080.7470802', u'3'],
         [u'2080.12322642', u'3'],
         [u'2080.13711281', u'2'],
         [u'2080.14585393', u'2'],
         [u'2082.2082', u'1'],
         [u'2082.12655506', u'3'],
         [u'2082.13344034', u'3'],
         [u'2082.13735857', u'2'],
         [u'2082.13789027', u'7'],
         [u'2082.14716465', u'2']]]


discovery = {'': [(u'Control Plane Interface: class-default', {}),
                  (u'Control Plane Interface: copp-arp', {}),
                  (u'Control Plane Interface: copp-bgp', {}),
                  (u'Control Plane Interface: copp-critical-app', {}),
                  (u'Control Plane Interface: copp-management', {}),
                  (u'Control Plane Interface: copp-monitoring', {}),
                  (u'Control Plane Interface: copp-reporting', {}),
                  (u'Control Plane Interface: copp-undesirable', {}),
                  (u'Vlan100: class-default', {}),
                  (u'Vlan100: class-default', {}),
                  (u'Vlan100: cos-map-c14_VPN-INT1', {}),
                  (u'Vlan100: cos-map-c14_VPN-INT1', {}),
                  (u'Vlan101: class-default', {}),
                  (u'Vlan101: class-default', {}),
                  (u'Vlan101: cos-map-c32_VPN-INT1', {}),
                  (u'Vlan101: cos-map-c32_VPN-INT1', {}),
                  (u'Vlan102: class-default', {}),
                  (u'Vlan102: class-default', {}),
                  (u'Vlan102: cos-map-c7_VPN-INT1', {}),
                  (u'Vlan102: cos-map-c7_VPN-INT1', {}),
                  (u'Vlan106: class-default', {}),
                  (u'Vlan106: class-default', {}),
                  (u'Vlan106: cos-map-c35_VPN-INT1', {}),
                  (u'Vlan106: cos-map-c35_VPN-INT1', {})]}


checks = {'': [(u'Control Plane Interface: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-arp',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-bgp',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-critical-app',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-management',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-monitoring',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-reporting',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Control Plane Interface: copp-undesirable',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: copp-policy, Int-Bandwidth: 4.29 GBit/s',
                  [('post', 0.0, None, None, 0.0, 536870911.875),
                   ('drop', 0.0, None, None, 0.0, 536870911.875)])]),
               (u'Vlan100: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C14, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan100: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C14, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan100: cos-map-c14_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C14, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan100: cos-map-c14_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C14, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan101: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C32, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan101: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C32, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan101: cos-map-c32_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C32, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan101: cos-map-c32_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C32, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan102: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C7, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan102: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C7, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan102: cos-map-c7_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C7, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan102: cos-map-c7_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C7, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan106: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C35, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan106: class-default',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C35, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan106: cos-map-c35_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C35, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])]),
               (u'Vlan106: cos-map-c35_VPN-INT1',
                {},
                [(0,
                  u'post: 0 Bit/s, drop: 0 Bit/s, Policy-Name: cos-pol-VPN-INT1_C35, Int-Bandwidth: 1 GBit/s',
                  [('post', 0.0, None, None, 0.0, 125000000.0),
                   ('drop', 0.0, None, None, 0.0, 125000000.0)])])]}
