# Memory Address

| **Description** | **Address** |
| -----------: | -----------: |
| Enemy HP | CFE6-CFE7 |<!-- 连续地址指将两个位置的数据拼成四位数进行读取。-->
| Enemy Level | CFF3 |
| Enemy Max HP | CFF4-CFF5 |
| Enemy Attack | CFF6-CFF7 |
| Enemy Defense | CFF8-CFF9 |
| Enemy internal ID | CFE5 |<!-- 此处的internal ID 指的是https://tcrf.net/Pok%C3%A9mon_Red_and_Blue/Internal_Index_Number 里面的Hex internal number, 在 https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Red_and_Blue/Notes#Picture_numbers 中也可以找到eg.6C指向EKANS-->
| Enemy type 1 | CFEA |
| Enemy type 2 | CFEB |<!-- 目前仍在寻找不同元素系对应的编码，已找到克制关系。若宝可梦只有一种元素，则会在type1 与 type2 中储存相同的编码。不确定仅有一种元素和两种元素皆有导致的其他影响。-->
| Enemy's Move 1 | CFED |
| Enemy's Move 2 | CFEE |
| Enemy's Move 3 | CFEF |
| Enemy's Move 4 | CFF0 |
| Enemy's Move ID | CFCC |<!-- Move 指技能，目前已有对照表。前四个指存储技能，最后一个指当前使用技能。对照表相同。-->
| Enemy's Status | CFE9 |<!-- 对应的bits和状态已有关系。--><!-- Pokemon in battle 会显示目前出战的宝可梦的数据，剩余六个宝可梦是在等待席的六个宝可梦。 -->
| **Pokemon In Battle** |
| ID | D014 |
| Current HP | D015-D016 |
| Status | D018 |
| Type 1 | D019 |
| Type 2 | D01A |
| Move 1 | D01C |
| Move 2 | D01D |
| Move 3 | D01E |
| Move 4 | D01F |<!-- 这里的Move1会出现储存多个数字的情况，可能是字节显示问题。-->
| Max HP | D023-D024 |
| Attack | D025-DO26 |
| Defense | D027-D028 |
| Level | D022 |
| PP Move 1 | D02D |
| PP Move 2 | D02E |
| PP Move 3 | D02F |
| PP Move 4 | D030 |<!-- PP 指可用点数，若点数归0，技能不能使用。-->
| **Player's Pokemon 1** |
| Level | D18C |
| Current HP | D16C-D16D |
| Attack | D18F-D190 |
| Defense | D191-D192 |
| Max HP | D18D-D18E |
| Name Index | D164 |
| Experience | D179-D17B |
| **Player's Pokemon 2** |
| Level | D1B8 |
| Current HP | D198-D199 |
| Attack | D1BB-D1BC |
| Defense | D1BD-D1BE |
| Max HP | D1B9-D1BA |
| Name Index | D165 |
| Experience | D1A5-D1A7 |
| **Player's Pokemon 3** |
| Level | D1E4 |
| Current HP | D1C4-D1C5 |
| Attack | D1E7-D1E8 |
| Defense | D1E9-D1EA |
| Max HP | D1E5-D1E6 |
| Name Index | D166 |
| Experience | D1D1-D1D3 |
| **Player's Pokemon 4** |
| Level | D210 |
| Current HP | D1F0-D1F1 |
| Attack | D213-D214 |
| Defense | D191-D192 |
| Max HP | D211-D212 |
| Name Index | D167 |
| Experience | D1FD-D1FF |
| **Player's Pokemon 5** |
| Level | D23C |
| Current HP | D21C-D21D |
| Attack | D23F-D240 |
| Defense | D241-D242 |
| Max HP | D23D-D23E |
| Name Index | D168 |
| Experience | D229-D22B |
| **Player's Pokemon 6** |
| Level | D268 |
| Current HP | D248-D249 |
| Attack | D26B-D26C |
| Defense | D26D-D26E |
| Max HP | D269-D26A |
| Name Index | D169 |
| Experience | D255-D257 |
| **Item 1** |
| Index | 0xD31E |
| Quantity | 0xD31F |
| **Item 2** |
| Index | 0xD320 |
| Quantity | 0xD321 |
| **Item 3** |
| Index | 0xD322 |
| Quantity | 0xD323 |
| **Item 4** |
| Index | 0xD324 |
| Quantity | 0xD325 |
| **Item 5** |
| Index | 0xD326 |
| Quantity | 0xD327 |
| **Item 6** |
| Index | 0xD328 |
| Quantity | 0xD329 |
| **Item 7** |
| Index | 0xD32A |
| Quantity | 0xD32B |
| **Item 8** |
| Index | 0xD32C |
| Quantity | 0xD32D |
| **Item 9** |
| Index | 0xD32E |
| Quantity | 0xD32F |
| **Item 10** |
| Index | 0xD330 |
| Quantity | 0xD331 |
| **Item 11** |
| Index | 0xD332 |
| Quantity | 0xD333 |
| **Item 12** |
| Index | 0xD334 |
| Quantity | 0xD335 |
| **Item 13** |
| Index | 0xD336 |
| Quantity | 0xD337 |
| **Item 14** |
| Index | 0xD338 |
| Quantity | 0xD339 |
| **Item 15** |
| Index | 0xD33A |
| Quantity | 0xD33B |
| **Item 16** |
| Index | 0xD33C |
| Quantity | 0xD33D |
| **Item 17** |
| Index | 0xD33E |
| Quantity | 0xD33F |
| **Item 18** |
| Index | 0xD340 |
| Quantity | 0xD341 |
| **Item 19** |
| Index | 0xD342 |
| Quantity | 0xD343 |
| **Item 20** |
| Index | 0xD344 |
| Quantity | 0xD345 |
