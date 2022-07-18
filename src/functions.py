def season_hemisphere(month,hemisphere):
    North_dict={'Dec':'winter','Jan':'winter','Feb':'winter','Mar':'spring','Apr':'spring','May':'spring','Jun':'summer',
           'Jul':'summer','Aug':'summer','Sep':'autumn','Oct':'autumn','Nov':'autumn'}
    South_dict={'Dec':'summer','Jan':'summer','Feb':'summer','Mar':'autumn','Apr':'autumn','May':'autumn','Jun':'winter',
           'Jul':'winter','Aug':'winter','Sep':'spring','Oct':'spring','Nov':'spring'}
    if hemisphere == 'North Hemisphere':
        return North_dict[month]
    elif hemisphere == 'South Hemisphere':
        return South_dict[month]
    else:
        return ''

#function country - hemisphere
def hemisphere(country):
    North=['ADMIRALTY ISLANDS',' TONGA','AMERICAN SAMOA','ARUBA', 'AZORES','BARBADOS','BAHAMAS', 'BERMUDA', 'BELIZE','BRITISH ISLES',
      'DOMINICAN REPUBLIC','COSTA RICA','CROATIA','CUBA','ENGLAND','CHINA','IRAQ','IRAN','ISRAEL','ITALY','JAPAN','COLUMBIA','CANADA','CENTRAL PACIFIC',
       'CARIBBEAN SEA', 'TURKS & CAICOS','ST. MAARTIN','ST. MARTIN', 'TRINIDAD & TOBAGO', 'TONGA','TAIWAN','VIETNAM','THAILAND','USA', 'SOUTH CHINA SEA', 'SOUTH KOREA','UNITED KINGDOM','UNITED ARAB EMIRATES (UAE)','UNITED ARAB EMIRATES','SRI LANKA', 'PUERTO RICO','PHILIPPINES','TURKEY','SPAIN','SINGAPORE','PALESTINIAN TERRITORIES','SOMALIA','SIERRA LEONE','PANAMA','SENEGAL', 'SAUDI ARABIA','SCOTLAND','RUSSIA','PORTUGAL','PALA','OKINAWA','NICARAGUA','NIGERIA','MICRONESIA','NEW BRITAIN','MID ATLANTIC OCEAN','MARSHALL ISLANDS', 'MALAYSIA','JAMAICA', 'INDIA', 'HONG KONG','HONDURAS','GUINEA','GUAM','GRENADA','EL SALVADOR', 'CAYMAN ISLANDS','GRAND CAYMAN','FEDERATED STATES OF MICRONESIA', 'MALTA', 'GREECE','FRANCE','MEXICO','NORWAY','BRITISH VIRGIN ISLANDS', 'BRITISH WEST INDIES',]
    South=['ARGENTINA','PAPUA NEW GUINEA', 'WESTERN SAMOA','URUGUAY','TANZANIA', 'SOLOMON ISLANDS','SAMOA','SEYCHELLES','ANDAMAN / NICOBAR ISLANDAS', 'AUSTRALIA', 'BRAZIL','BRITISH NEW GUINEA','CHILE','EGYPT ','EGYPT','CAPE VERDE','ECUADOR','FIJI','Fiji',
      'DIEGO GARCIA','NEW GUINEA','VANUATU','VENEZUELA','SOUTH AFRICA','NEW CALEDONIA','MOZAMBIQUE','NEW ZEALAND', 'KENYA','KIRIBATI','MADAGASCAR','MAURITIUS', 'MALDIVES','FRENCH POLYNESIA','INDONESIA',]
    if country in North:
        return 'North Hemisphere'
    elif country in South:
        return 'South Hemisphere'
    else:
        return ''