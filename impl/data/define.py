from numpy import nan

discrete = ['_STATE', 'FMONTH', 'IDATE', 'IMONTH', 'IDAY', 'IYEAR', 'CTELENUM', 'PVTRESD1', 'COLGHOUS', 'STATERES', 'CELLFON3', 'LADULT', 'CTELNUM1', 'CELLFON2', 'CADULT', 'PVTRESD2', 'CCLGHOUS', 'CSTATE', 'LANDLINE', 'GENHLTH', 'PHYSHLTH', 'MENTHLTH', 'POORHLTH', 'HLTHPLN1', 'PERSDOC2', 'MEDCOST', 'CHECKUP1', 'BPHIGH4', 'BPMEDS', 'BLOODCHO', 'CHOLCHK', 'TOLDHI2', 'CVDINFR4', 'CVDCRHD4', 'CVDSTRK3', 'ASTHMA3', 'ASTHNOW', 'CHCSCNCR', 'CHCOCNCR', 'CHCCOPD1', 'HAVARTH3', 'ADDEPEV2', 'CHCKIDNY', 'DIABETE3', 'SEX', 'MARITAL', 'EDUCA', 'RENTHOM1', 'NUMHHOL2', 'NUMPHON2', 'CPDEMO1', 'VETERAN3', 'EMPLOY1', 'INCOME2', 'INTERNET', 'PREGNANT', 'QLACTLM2', 'USEEQUIP', 'BLIND', 'DECIDE', 'DIFFWALK', 'DIFFDRES', 'DIFFALON', 'SMOKE100', 'SMOKDAY2', 'STOPSMK2', 'LASTSMK2', 'USENOW3', 'EXERANY2', 'EXRACT11', 'EXRACT21', 'LMTJOIN3', 'ARTHDIS2', 'ARTHSOCL', 'JOINPAIN', 'SEATBELT', 'FLUSHOT6', 'FLSHTMY2', 'IMFVPLAC', 'PNEUVAC3', 'HIVTST6', 'HIVTSTD3', 'WHRTST10', 'PDIABTST', 'PREDIAB1', 'INSULIN', 'EYEEXAM', 'DIABEYE', 'DIABEDU', 'CAREGIV1', 'CRGVREL1', 'CRGVLNG1', 'CRGVHRS1', 'CRGVPRB1', 'CRGVPERS', 'CRGVHOUS', 'CRGVMST2', 'CRGVEXPT', 'VIDFCLT2', 'VIREDIF3', 'VIPRFVS2', 'VINOCRE2', 'VIEYEXM2', 'VIINSUR2', 'VICTRCT4', 'VIGLUMA2', 'VIMACDG2', 'CIMEMLOS', 'CDHOUSE', 'CDASSIST', 'CDHELP', 'CDSOCIAL', 'CDDISCUS', 'WTCHSALT', 'DRADVISE', 'ASATTACK', 'ASYMPTOM', 'ASNOSLEP', 'ASTHMED3', 'ASINHALR', 'HAREHAB1', 'STREHAB1', 'CVDASPRN', 'ASPUNSAF', 'RLIVPAIN', 'RDUCHART', 'RDUCSTRK', 'ARTTODAY', 'ARTHWGT', 'ARTHEXER', 'ARTHEDU', 'TETANUS', 'HPVADVC2', 'HPVADSHT', 'SHINGLE2', 'HADMAM', 'HOWLONG', 'HADPAP2', 'LASTPAP2', 'HPVTEST', 'HPLSTTST', 'HADHYST2', 'PROFEXAM', 'LENGEXAM', 'BLDSTOOL', 'LSTBLDS3', 'HADSIGM3', 'HADSGCO1', 'LASTSIG3', 'PCPSAAD2', 'PCPSADI1', 'PCPSARE1', 'PSATEST1', 'PSATIME', 'PCPSARS1', 'PCPSADE1', 'PCDMDECN', 'SCNTMNY1', 'SCNTMEL1', 'SCNTPAID', 'SCNTLPAD', 'SXORIENT', 'TRNSGNDR', 'RCSGENDR', 'RCSRLTN2', 'CASTHDX2', 'CASTHNO2', 'EMTSUPRT', 'LSATISFY', 'MISTMNT', 'ADANXEV', 'QSTLANG', 'MSCODE', '_CHISPNC', '_CRACE1', '_CPRACE', '_DUALUSE', '_RFHLTH', '_HCVU651', '_RFHYPE5', '_CHOLCHK', '_RFCHOL', '_LTASTH1', '_CASTHM1', '_ASTHMS1', '_DRDXAR1', '_PRACE1', '_MRACE1', '_HISPANC', '_RACE', '_RACEG21', '_RACEGR3', '_RACE_G1', '_AGEG5YR', '_AGE65YR', '_AGE80', '_AGE_G', '_BMI5CAT', '_RFBMI5', '_CHLDCNT', '_EDUCAG', '_INCOMG', '_SMOKER3', '_RFSMOK3', 'DRNKANY5', '_RFBING5', '_RFDRHV5', '_MISFRTN', '_MISVEGN', '_FRTRESP', '_VEGRESP', '_FRTLT1', '_VEGLT1', '_FRT16', '_VEG23', '_FRUITEX', '_VEGETEX', '_TOTINDA', 'ACTIN11_', 'ACTIN21_', 'PAMISS1_', '_PACAT1', '_PAINDX1', '_PA150R2', '_PA300R2', '_PA30021', '_PASTRNG', '_PAREC1', '_PASTAE1', '_LMTACT1', '_LMTWRK1', '_LMTSCL1', '_RFSEAT2', '_RFSEAT3', '_FLSHOT6', '_PNEUMO2', '_AIDTST3', ]

continus = ['NUMADULT', 'NUMMEN', 'NUMWOMEN', 'HHADULT', 'DIABAGE2', 'CHILDREN', 'WEIGHT2', 'HEIGHT3', 'ALCDAY5', 'AVEDRNK2', 'DRNK3GE5', 'MAXDRNKS', 'FRUITJU1', 'FRUIT1', 'FVBEANS', 'FVGREEN', 'FVORANG', 'VEGETAB1', 'EXEROFT1', 'EXERHMM1', 'EXEROFT2', 'EXERHMM2', 'STRENGTH', 'BLDSUGAR', 'FEETCHK2', 'DOCTDIAB', 'CHKHEMO3', 'FEETCHK', 'LONGWTCH', 'ASTHMAGE', 'ASERVIST', 'ASDRVIST', 'ASRCHKUP', 'ASACTLIM', 'SCNTWRK1', 'SCNTLWK1', 'ADPLEASR', 'ADDOWN', 'ADSLEEP', 'ADENERGY', 'ADEAT1', 'ADFAIL', 'ADTHINK', 'ADMOVE', 'HTIN4', 'HTM4', 'WTKG3', '_BMI5', 'DROCDY3_', '_DRNKWEK', 'FTJUDA1_', 'FRUTDA1_', 'BEANDAY_', 'GRENDAY_', 'ORNGDAY_', 'VEGEDA1_', '_FRUTSUM', '_VEGESUM', 'METVL11_', 'METVL21_', 'MAXVO2_', 'FC60_', 'PADUR1_', 'PADUR2_', 'PAFREQ1_', 'PAFREQ2_', '_MINAC11', '_MINAC21', 'STRFREQ_', 'PAMIN11_', 'PAMIN21_', 'PA1MIN_', 'PAVIG11_', 'PAVIG21_', 'PA1VIGM_', ]

USEFUL_QUESTIONARE = [
    #'BPHIGH4',
    'TOLDHI2',
    'CVDSTRK3',
    'DIABETE3',
]

DELETE_FEATURE = [
    'HEIGHT3',
    'FRUITJU1',
    'FRUIT1',
    'FVBEANS',
    'FVGREEN',
    'FVORANG',
    'VEGETAB1',
    'EXEROFT1',
    'EXERHMM1',
    'EXEROFT2',
    'EXERHMM2',
    'STRENGTH',

    '_STATE',
    'FMONTH',
    'IDATE',
    'IMONTH',
    'IDAY',
    'IYEAR',
    'DISPCODE',
    'CTELENUM',
    'SEQNO',
    '_PSU',
    'PVTRESD1',
    'STATERES',
    'CELLFON3',
    'NUMADULT',
    'NUMMEN',
    'NUMWOMEN',
    'CTELNUM1',
    'CELLFON2',
    'CADULT',
    'PVTRESD2',
    'CSTATE',
    'LANDLINE',
    'HHADULT',
    'FLSHTMY2',
    'HIVTSTD3',
    '_CHISPNC',
    '_DUALUSE',
    'QSTLANG',
    '_DUALCOR',
    '_STRWT',
    'EXRACT11',
    'EXRACT21',
    '_STSTR',
    '_RAWRAKE',
    '_WT2RAKE',
    '_LLCPWT',
    #'HTM4',  # not sure
    #'_EDUCAG',  # not sure
    #'_PACAT1',  # not sure
    #'_HCVU651',
    #'_CHOLCHK',
    #'_LTASTH1',
    #'_CASTHM1',
    #'_PRACE1',
    #'_MRACE1',
    #'_HISPANC',
    #'_RACE',
    #'_RACEG21',
    #'_RACEGR3',
    #'_RACE_G1',
    #'_AGEG5YR',  # for age feature, only reserve _AGE80
    #'_AGE65YR',
    #'_AGE_G',
    #'HTIN4',
    #'_BMI5',  # for bmi feature, only reserve _BMI5CAT
    #'_RFBMI5',
    #'_CHLDCNT',
    #'_INCOMG',  # not sure
    #'_RFSMOK3',
    #'DRNKANY5',
    #'DROCDY3_',
    #'_DRNKWEK',
    #'_RFBING5',
    #'_MISFRTN',
    #'_MISVEGN',
    #'FTJUDA1_',
    #'FRUTDA1_',
    #'BEANDAY_',
    #'GRENDAY_',
    #'ORNGDAY_',
    #'VEGEDA1_',
    #'_FRTRESP',
    #'_VEGRESP',
    #'_FRUTSUM',
    #'_VEGESUM',
    #'_FRT16',
    #'_VEG23',
    #'_FRUITEX',
    #'_VEGETEX',
    #'_TOTINDA',
    #'METVL11_',
    #'METVL21_',
    #'MAXVO2_',
    #'FC60_',
    #'ACTIN11_',
    #'ACTIN21_',
    #'PADUR1_',
    #'PADUR2_',
    #'PAFREQ1_',
    #'PAFREQ2_',
    #'_MINAC11',
    #'_MINAC21',
    #'STRFREQ_',
    #'PAMISS1_',
    #'PAMIN11_',
    #'PAMIN21_',
    #'PA1MIN_',
    #'PAVIG11_',
    #'PAVIG21_',
    #'PA1VIGM_',
    #'_PAINDX1',
    #'_PA300R2',
    #'_PA30021',
    #'_PA150R2',
    #'_PASTRNG',
    #'_PASTAE1',
    #'_RFSEAT2',
    #'_RFSEAT3',
    #'_FLSHOT6',
    #'_PNEUMO2',
    #'_AIDTST3',
]

ONEHOT = { # credit to Pian Wan
    '_STATE': [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
               32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 66, 72],
    'HLTHPLN1': [1, 2, 7, 9],
    'PERSDOC2': [1, 2, 3, 7, 9],
    'MEDCOST': [1, 2, 7, 9],
    'CHECKUP1': [1, 2, 3, 4, 7, 8, 9],
    'BPHIGH4': [1, 2, 3, 4, 7, 9],
    'BPMEDS': [1, 2, 7, 9],
    'BLOODCHO': [1, 2, 7, 9],
    'CHOLCHK': [1, 2, 3, 4, 7, 9],
    'TOLDHI2': [1, 2, 7, 9],
    'CVDINFR4': [1, 2, 7, 9],
    'CVDCRHD4': [1, 2, 7, 9],
    'CVDSTRK3': [1, 2, 7, 9],
    'ASTHMA3': [1, 2, 7, 9],
    'ASTHNOW': [1, 2, 7, 9],
    'CHCSCNCR': [1, 2, 7, 9],
    'CHCOCNCR': [1, 2, 7, 9],
    'CHCCOPD1': [1, 2, 7, 9],
    'HAVARTH3': [1, 2, 7, 9],
    'ADDEPEV2': [1, 2, 7, 9],
    'CHCKIDNY': [1, 2, 7, 9],
    'DIABETE3': [1, 2, 3, 4, 7, 9],
    'SEX': [1, 2],
    'MARITAL': [1, 2, 3, 4, 5, 6, 9],
    'EDUCA': [1, 2, 3, 4, 5, 6, 9],
    'RENTHOM1': [1, 2, 3, 7, 9],
    'NUMHHOL2': [1, 2, 3, 7, 9],
    'VETERAN3': [1, 2, 7, 9],
    'EMPLOY1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'INCOME2': [1, 2, 3, 4, 5, 6, 7, 8, 77, 99],
    'INTERNET': [1, 2, 7, 9],
    'PREGNANT': [1, 2, 7, 9],
    'QLACTLM2': [1, 2, 7, 9],
    'USEEQUIP': [1, 2, 7, 9],
    'BLIND': [1, 2, 7, 9],
    'DECIDE': [1, 2, 7, 9],
    'DIFFWALK': [1, 2, 7, 9],
    'DIFFDRES': [1, 2, 7, 9],
    'DIFFALON': [1, 2, 7, 9],
    'SMOKE100': [1, 2, 7, 9],
    'SMOKDAY2': [1, 2, 3, 7, 9],
    'STOPSMK2': [1, 2, 7, 9],
    'USENOW3': [1, 2, 3, 7, 9],
    'EXERANY2': [1, 2, 7, 9],
    'EXRACT11': list(range(1, 99)),
    'EXRACT21': list(range(1, 100)),
    'LMTJOIN3': [1, 2, 7, 9],
    'ARTHDIS2': [1, 2, 7, 9],
    'ARTHSOCL': [1, 2, 3, 7, 9],
    'FLUSHOT6': [1, 2, 7, 9],
    'PNEUVAC3': [1, 2, 7, 9],
    'HIVTST6': [1, 2, 7, 9],
    'WHRTST10': [1, 2, 3, 4, 5, 6, 7, 8, 9, 77, 99],
    'PDIABTST': [1, 2, 7, 9],
    'PREDIAB1': [1, 2, 3, 7, 9],
    'INSULIN': [1, 2, 9],
    'DIABEYE': [1, 2, 7, 9],
    'DIABEDU': [1, 2, 7, 9],
    'CAREGIV1': [1, 2, 7, 8, 9],
    'CRGVREL1': list(range(1, 16)) + [77, 99],
    'CRGVLNG1': [1, 2, 3, 4, 5, 7, 9],
    'CRGVHRS1': [1, 2, 3, 4, 7, 9],
    'CRGVPRB1': list(range(1, 14)) + [77, 99],
    'CRGVPERS': [1, 2, 7, 9],
    'CRGVHOUS': [1, 2, 7, 9],
    'CRGVMST2': [1, 2, 3, 4, 5, 6, 7, 9],
    'CRGVEXPT': [1, 2, 7, 9],
    'CDDISCUS': [1, 2, 7, 9],
    'WTCHSALT': [1, 2, 7, 9],
    'DRADVISE': [1, 2, 7, 9],
    'ASATTACK': [1, 2, 7],
    'STREHAB1': [1, 2, 7, 9],
    'CVDASPRN': [1, 2, 7, 9],
    'ASPUNSAF': [1, 2, 3, 7, 9],
    'RLIVPAIN': [1, 2, 7, 9],
    'RDUCHART': [1, 2, 7, 9],
    'RDUCSTRK': [1, 2, 7, 9],
    'ARTHWGT': [1, 2, 7, 9],
    'ARTHEXER': [1, 2, 7, 9],
    'ARTHEDU': [1, 2, 7, 9],
    'HPVADVC2': [1, 2, 3, 7, 9],
    'SHINGLE2': [1, 2, 7, 9],
    'HADMAM': [1, 2, 7, 9],
    'HADPAP2': [1, 2, 7, 9],
    'HPVTEST': [1, 2, 7, 9],
    'HADHYST2': [1, 2, 7, 9],
    'PROFEXAM': [1, 2, 7, 9],
    'BLDSTOOL': [1, 2, 7, 9],
    'HADSIGM3': [1, 2, 7, 9],
    'HADSGCO1': [1, 2, 7, 9],
    'PCPSAAD2': [1, 2, 7, 9],
    'PCPSADI1': [1, 2, 7, 9],
    'PCPSARE1': [1, 2, 7, 9],
    'PSATEST1': [1, 2, 7, 9],
    'PCPSARS1': [1, 2, 3, 4, 5, 7, 9],
    'PCPSADE1': [1, 2, 3, 4, 9],
    'SXORIENT': [1, 2, 3, 4, 7, 9],
    'TRNSGNDR': [1, 2, 3, 4, 7, 9],
    'RCSGENDR': [1, 2, 9],
    'RCSRLTN2': [1, 2, 3, 4, 5, 6, 7, 9],
    'CASTHDX2': [1, 2, 7, 9],
    'CASTHNO2': [1, 2, 7, 9],
    'MISTMNT': [1, 2, 7, 9],
    'ADANXEV': [1, 2, 7, 9],
    'MSCODE': [1, 2, 3, 5],
    'CHISPNC': [1, 2, 9],
    'CRACE1': [1, 2, 3, 4, 5, 6, 7, 77, 99],
    'CPRACE': [1, 2, 3, 4, 5, 6, 7, 77, 99],
    '_RACE': [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

TREAT_NAN = {
    'MSCODE': {
        nan: 5
    },
    'GENHLTH': {
        7: 2,
        9: 2,
        nan: 2
    },
    'MENTHLTH': {
        88: 0,
        77: 0,
        99: 0,
        nan: 0
    },
    'PHYSHLTH': {
        88: 0,
        77: 0,
        99: 0,
        nan: 0
    },
    'POORHLTH': {
        88: 0,
        77: 0,
        99: 0,
        nan: 0
    },
    'HLTHPLN1': {
        7: 1,
        9: 1,
    },
    'PERSDOC2': {
        7: 1,
        9: 1,
    },
    'MEDCOST': {
        7: 2,
        9: 2,
        nan: 2
    },
    'CHECKUP1': {
        7: 5,
        8: 5,
        9: 5,
        nan: 5
    },
    'BPHIGH4': {
        2: 3,
        4: 2,
        7: 3,
        9: 3,
        nan: 3
    },
    'BPMEDS': {
        7: 2,
        9: 2,
        nan: 2
    },
    'BLOODCHO': {
        7: 2,
        9: 2,
    },
    'CHOLCHK': {
        7: 6,
        9: 6,
        nan: 6
    },
    'TOLDHI2': {
        7: 2,
        9: 2,
        nan: 2
    },
    'CVDINFR4': {
        7: 2,
        9: 2,
    },
    'CVDCRHD4': {
        7: 2,
        9: 2,
        nan: 2
    },
    'CVDSTRK3': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'DIABETE3': {
        7: 3,
        9: 3,
        nan: 3
    },
    'ASTHMA3': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'ASTHNOW': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'CHCSCNCR': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'CHCOCNCR': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'CHCCOPD1': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'HAVARTH3': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'ADDEPEV2': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'CHCKIDNY': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'DIABAGE2': {
        98: 0,
        99: 0,
        nan: 0,
    },
    'MARITAL': {
        9: 7
    },
    'EDUCA': {
        9: 6
    },
    'RENTHOM1': {
        7: 1,
        9: 1
    },
    'NUMHHOL2': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'VETERAN3': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'CHILDREN': {
        88: 0,
        99: 0,
        nan: 0,
    },
    'INCOME2': {
        77: 6,
        99: 6,
        nan: 6,
    },
    'CPDEMO1': {
        7: 1,
        9: 1,
        nan: 1,
    },
    'INTERNET': {
        7: 1,
        9: 1,
        nan: 1,
    },
    'WEIGHT2': {
        '>700': 'avg',
        nan: 'avg'
    },
    'HEIGHT3': {
        '>999': 'avg',
        nan: 'avg'
    },
    'PREGNANT': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'QLACTLM2': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'USEEQUIP': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'BLIND': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'DECIDE': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'DIFFWALK': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'DIFFDRES': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'DIFFALON': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'SMOKE100': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'SMOKDAY2': {
        3: 3,
        7: 2,
        9: 2,
        nan: 2,
    },
    'STOPSMK2': {
        7: 3,
        9: 3,
        nan: 3,
    },
    'LASTSMK2': {
        77: 9,
        99: 9,
        nan: 9,
    },
    'USENOW3': {
        7: 3,
        9: 3,
        nan: 3,
    },
    'ALCDAY5': {
        '<200': 'ALCDAY5<',
        '>200': 'ALCDAY5>',
        888: 0,
        777: 'avg',
        999: 'avg',
        nan: 'avg',
    },
    'AVEDRNK2': {
        77: 0,
        99: 0,
        nan: 0,
    },
    'DRNK3GE5': {
        77: 0,
        88: 0,
        99: 0,
        nan: 0,
    },
    'MAXDRNKS': {
        77: 0,
        99: 0,
        nan: 0,
    },
    'FRUITJU1': {
        777: 555,
        999: 555,
        nan: 555,
    },
    'FRUIT1': {
        777: 555,
        999: 555,
        nan: 555,
    },
    'FVBEANS': {
        777: 555,
        999: 555,
        nan: 555,
    },
    'FVGREEN': {
        777: 555,
        999: 555,
        nan: 555,
    },
    'FVORANG': {
        777: 555,
        999: 555,
        nan: 555,
    },
    'VEGETAB1': {
        777: 555,
        999: 555,
        nan: 555,
    },
    'EXERANY2': {
        7: 1,
        9: 1,
        nan: 1,
    },
    'EXRACT11': {
        99: 77,
        nan: 77,
    },
    'EXEROFT1': {
        999: 777,
        nan: 777,
    },
    'EXERHMM1': {
        999: 777,
        nan: 777,
    },
    'EXRACT21': {
        99: 77,
        nan: 77,
    },
    'EXEROFT2': {
        999: 777,
        nan: 777,
    },
    'STRENGTH': {
        999: 777,
        nan: 777,
    },
    'LMTJOIN3': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'EXERHMM2': {
        999: 777,
        nan: 777,
    },
    'ARTHDIS2': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'ARTHSOCL': {
        7: 3,
        9: 3,
        nan: 3,
    },
    'JOINPAIN': {
        77: 0,
        99: 0,
        nan: 0,
    },
    'SEATBELT': {
        7: 0,
        8: 0,
        9: 0,
        nan: 0,
    },
    'FLUSHOT6': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'IMFVPLAC': {
        77: 12,
        99: 12,
        nan: 'avg',
    },
    'PNEUVAC3': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'HIVTST6': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'WHRTST10': {
        99: 77,
        nan: 99,
    },
    'PDIABTST': {
        7: 2,
        9: 2,
        nan: 2,
    },
    'PREDIAB1': {
        7: 3,
        9: 3,
        nan: 3,
    },
    'INSULIN': {
        9: 2,
        nan: 2,
    },
    'SXORIENT': {
        7: 1,
        9: 1,
        nan: 1
    },
    'TRNSGNDR': {
        7: 4,
        9: 4,
        nan: 4
    },
    '_RFHLTH': {
        9: 1,  # Dont know, GENHLTH = 7 or 9 or Missing -> Good or Better Health
        nan: 1,
    },
    '_RFHYPE5': {
        9: 1,  # Dont know, GENHLTH = 7 or 9 or Missing -> No
        nan: 1,
    },
    '_CHOLCHK': {
        9: 3,  # Dont know -> Have never had cholesterol checked
    },
    '_RFCHOL': {  # all to no
        9: 1,  # Dont know， BLOODCHO=1 and TOLDHI2 = 7 or 9 or Missing
        nan: 1,  # BLOODCHO = 2 or 7 or 9 or Missing
    },
    '_MICHD': {
        nan: 2,  # Dont know -> no
    },
    '_LTASTH1': {
        9: 1,  # Dont know -> no
    },
    '_CASTHM1': {
        9: 1,  # ASTHMA3 = 7 or 9 or Missing or ASTHNOW = 7 or 9 or Missing -> no
    },
    '_ASTHMS1': {
        9: 3,  # ASTHMA3 = 7 or 9 or Missing or ASTHNOW = 7 or 9 or Missing -> never
        nan: 3,
    },
    '_DRDXAR1': {
        nan: 2  # HAVARTH3 = 7 or 9 or Missing -> no
    },
    '_PRACE1': {
        77: 8,  # Dont know
        99: 8,  # refused
    },
    '_MRACE1': {
        77: 8,  # Dont know
        99: 8,  # refused
    },
    '_HISPANC': {
        9: 2,  # Dont know
    },
    '_RACEG21': {
        9: 1,  # Dont know
    },
    '_RACEGR3': {
        9: 1,  # Dont know
    },
    '_RACE_G1': {
        nan: 1,  # Dont know
    },
    '_AGEG5YR': {
        14: 'avg',  # Dont know
    },
    '_AGE65YR': {
        3: 1,  # Dont know
    },
    'HTIN4': {  # remove, save HTM4
        nan: 'avg',  # Dont know
    },
    'HTM4': {
        # Height in meters [2 implied decimal places]
        nan: 'avg',  # Dont know, -> average
    },
    'WTKG3': {
        # Weight in kilograms [2 implied decimal places]
        99999: 'avg',  # Dont know, WEIGHT2 = 7777 or 9999 or Missing or not in accepted values -> average
        nan: 'avg'
    },
    '_BMI5': {
        # WTKG3/(HTM4*HTM4) (Has 2 implied decimal places)
        9999: 'avg',  # Dont know
        nan: 'avg',  # Dont know, WTKG3 = 777 or 999 or HTM4 = 777 or 999
    },
    '_BMI5CAT': {
        nan: 3,  # Dont know, _BMI5 = 9999 -> normal weight
    },
    '_RFBMI5': {
        9: 2,  # _BMI5 = 9999
    },
    '_CHLDCNT': {
        9: 1,  # Dont know -> no
    },
    '_EDUCAG': {
        9: 1,  # Dont know -> not graduate
    },
    '_INCOMG': {
        9: 1,  # Dont know -> less than 15000
    },
    '_SMOKER3': {
        9: 4,  # Dont know -> never smoked
        nan: 4,
    },
    '_RFSMOK3': {
        9: 1,  # Dont know -> no
    },
    'DRNKANY5': {  # all to no
        7: 2,
        9: 2,  # Dont know
    },
    'DROCDY3_': {
        900: 0,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_RFBING5': {
        9: 1,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_DRNKWEK': {
        99900: 0,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_RFDRHV5': {
        9: 1,  # Don’t know/Not Sure Or Refused/Missing -> no
        nan: 1,
    },
    'FTJUDA1_': {
        nan: 0,  # Dont know -> no
    },
    'FRUTDA1_': {
        nan: 0,  # Dont know -> no
    },
    'BEANDAY_': {
        nan: 0,  # Dont know -> no
    },
    'GRENDAY_': {
        nan: 0,  # Dont know -> no
    },
    'ORNGDAY_': {
        nan: 0,  # Dont know -> no
    },
    'VEGEDA1_': {
        nan: 0,  # Dont know -> no
    },
    '_FRUTSUM': {
        nan: 0,  # Dont know -> no
    },
    '_VEGESUM': {
        nan: 0,  # Dont know -> no
    },
    '_FRTLT1': {
        9: 1,  # Don’t know/Not Sure Or Refused/Missing -> no
        nan: 2,
    },
    '_VEGLT1': {
        9: 1,  # Don’t know/Not Sure Or Refused/Missing -> no
        nan: 2
    },
    '_TOTINDA': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    'METVL11_': {
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2) -> no
    },
    'METVL21_': {
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2) -> no
    },
    'MAXVO2_': {
        '>5.01': 'avg',  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    'FC60_': {
        '>85.90': 'avg',  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    'ACTIN11_': {
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2) -> no
    },
    'ACTIN21_': {
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2) -> no
    },
    'PADUR1_': {
        nan: 'avg',  # Dont know, or do not do sport (EXERANY2 = 2) -> no
    },
    'PADUR2_': {
        nan: 'avg',  # Dont know, or do not do sport (EXERANY2 = 2) -> no
    },
    'PAFREQ1_': {  # all to no
        '>99000': 'avg',
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2)
    },
    'PAFREQ2_': {  # all to no
        '>99000': 'avg',
        nan: 0,
    },
    '_MINAC11': {  # need a second check
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2)
    },
    '_MINAC21': {  # need a second check
        nan: 0,  # Dont know, or do not do sport (EXERANY2 = 2)
    },
    'STRFREQ_': {  # need a second check
        99000: 'avg',  # Dont know
        nan: 0,  # did not report doing any strengthening activity
        # STRENGTH = 777, 888, 999, nan
    },
    'PAMISS1_': {
        9: 0,  # Don’t know/Not Sure Or Refused/Missing
    },
    'PAMIN11_': {  # need a second check
        nan: 0,  # No value for ACTIN11_
    },
    'PAMIN21_': {  # need a second check
        nan: 0,  # No value for ACTIN21_
    },
    'PA1MIN_': {  # need a second check
        '>600': 600,
        nan: 0,  # No value for ACTIN11_ and ACTIN21_
    },
    'PAVIG11_': {  # need a second check
        nan: 0,  # no value for ACTIN11_
    },
    'PAVIG21_': {  # need a second check
        nan: 0,  # no value for ACTIN21_
    },
    'PA1VIGM_': {  # need a second check
        nan: 0  # no value for both PAVIG11_ and PAVIG21_
    },
    '_PACAT1': {
        9: 4,  # Don’t know/Not Sure Or Refused/Missing -> inactive
    },
    '_PAINDX1': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing -> did not meet
    },
    '_PA150R2': {
        9: 3,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_PA300R2': {
        9: 3,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_PA30021': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_PAREC1': {
        9: 4,  # Don’t know/Not Sure Or Refused/Missing -> no
        nan: 2,
    },
    '_PASTRNG': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_PASTAE1': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_LMTACT1': {  # all to no
        9: 3,  # Dont know
        nan: 3  # HAVARTH3=7, 9 or missing
    },
    '_LMTWRK1': {
        9: 3,  # Dont know
        nan: 3  # HAVARTH3=7, 9 or missing
    },
    '_LMTSCL1': {
        9: 4,  # Dont know
        nan: 4  # HAVARTH3=7, 9 or missing
    },
    '_RFSEAT2': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing -> no
    },
    '_RFSEAT3': {
        9: 2,  # Don’t know/Not Sure Or Refused/Missing
    },
    '_FLSHOT6': {  # all to no
        9: 2,  # Dont know
        nan: 2  # AGE <= 64
    },
    '_PNEUMO2': {  # all to no
        9: 2,  # Dont know
        nan: 2  # AGE <= 64
    },
    '_AIDTST3': {  # all to no
        9: 2,  # Dont know
        nan: 2  # HIVTST6 = missing
    },
}

FEATURE_CATEGORIES = {  # credit to Siyuan Cheng
    'TOLDHI2': 'Discrete_NoSeq',
    'CVDSTRK3': 'Discrete_NoSeq',
    'DIABETE3': 'Discrete_NoSeq',
    '_RFHLTH': 'Discrete_Seq',
    '_HCVU651': 'Discrete_NoSeq',
    '_RFHYPE5': 'Discrete_NoSeq',
    '_CHOLCHK': 'Discrete_NoSeq',
    '_RFCHOL': 'Discrete_NoSeq',
    '_LTASTH1': 'Discrete_NoSeq',
    '_CASTHM1': 'Discrete_NoSeq',
    '_ASTHMS1': 'Discrete_NoSeq',
    '_DRDXAR1': 'Discrete_NoSeq',
    '_PRACE1': 'Discrete_NoSeq',
    '_MRACE1': 'Discrete_NoSeq',
    '_HISPANC': 'Discrete_NoSeq',
    '_RACE': 'Discrete_NoSeq',
    '_RACEG21': 'Discrete_NoSeq',
    '_RACEGR3': 'Discrete_NoSeq',
    '_RACE_G1': 'Discrete_NoSeq',
    '_AGEG5YR': 'Discrete_Seq',
    '_AGE65YR': 'Discrete_NoSeq',
    '_AGE80': 'Discrete_Seq',
    '_AGE_G': 'Discrete_Seq',
    'HTIN4': 'Continues',
    'HTM4': 'Continues',
    'WTKG3': 'Continues',
    '_BMI5': 'Continues',
    '_BMI5CAT': 'Discrete_Seq',
    '_RFBMI5': 'Discrete_NoSeq',
    '_CHLDCNT': 'Discrete_Seq',
    '_EDUCAG': 'Discrete_NoSeq',
    '_INCOMG': 'Discrete_Seq',
    '_SMOKER3': 'Discrete_Seq',
    '_RFSMOK3': 'Discrete_NoSeq',
    'DRNKANY5': 'Discrete_NoSeq',
    'DROCDY3_': 'Continues',
    '_RFBING5': 'Discrete_NoSeq',
    '_DRNKWEK': 'Continues',
    '_RFDRHV5': 'Discrete_NoSeq',
    'FTJUDA1_': 'Continues',
    'FRUTDA1_': 'Continues',
    'BEANDAY_': 'Continues',
    'GRENDAY_': 'Continues',
    'ORNGDAY_': 'Continues',
    'VEGEDA1_': 'Continues',
    '_MISFRTN': 'Discrete_Seq',
    '_MISVEGN': 'Discrete_Seq',
    '_FRTRESP': 'Discrete_NoSeq',
    '_VEGRESP': 'Discrete_NoSeq',
    '_FRUTSUM': 'Continues',
    '_VEGESUM': 'Continues',
    '_FRTLT1': 'Discrete_NoSeq',
    '_VEGLT1': 'Discrete_NoSeq',
    '_FRT16': 'Discrete_NoSeq',
    '_VEG23': 'Discrete_NoSeq',
    '_FRUITEX': 'Discrete_NoSeq',
    '_VEGETEX': 'Discrete_NoSeq',
    '_TOTINDA': 'Discrete_NoSeq',
    'METVL11_': 'Continues',
    'METVL21_': 'Continues',
    'MAXVO2_': 'Continues',
    'FC60_': 'Continues',
    'ACTIN11_': 'Discrete_Seq',
    'ACTIN21_': 'Discrete_Seq',
    'PADUR1_': 'Continues',
    'PADUR2_': 'Continues',
    'PAFREQ1_': 'Continues',
    'PAFREQ2_': 'Continues',
    '_MINAC11': 'Continues',
    '_MINAC21': 'Continues',
    'STRFREQ_': 'Continues',
    'PAMISS1_': 'Discrete_NoSeq',
    'PAMIN11_': 'Continues',
    'PAMIN21_': 'Continues',
    'PA1MIN_': 'Continues',
    'PAVIG11_': 'Continues',
    'PAVIG21_': 'Continues',
    'PA1VIGM_': 'Continues',
    '_PACAT1': 'Discrete_Seq',
    '_PAINDX1': 'Discrete_NoSeq',
    '_PA150R2': 'Discrete_Seq',
    '_PA300R2': 'Discrete_Seq',
    '_PA30021': 'Discrete_NoSeq',
    '_PASTRNG': 'Discrete_NoSeq',
    '_PAREC1': 'Discrete_NoSeq',
    '_PASTAE1': 'Discrete_NoSeq',
    '_LMTACT1': 'Discrete_NoSeq',
    '_LMTWRK1': 'Discrete_NoSeq',
    '_LMTSCL1': 'Discrete_Seq',
    '_RFSEAT2': 'Discrete_NoSeq',
    '_RFSEAT3': 'Discrete_NoSeq',
    '_FLSHOT6': 'Discrete_NoSeq',
    '_PNEUMO2': 'Discrete_NoSeq',
    '_AIDTST3': 'Discrete_NoSeq'
}

VARIABLE_GROUP = {
    1: ['_RFHLTH'],

    4: ['_RFHYPE5'],

    5: ['_CHOLCHK', '_RFCHOL',],

    6: ['_MICHD', '_LTASTH1', '_CASTHM1', '_ASTHMS1', '_DRDXAR1'],

    7: ['_PRACE1', '_MRACE1', '_HISPANC', '_RACE', '_RACEG21',
        '_RACEGR3', '_RACE_G1', '_AGEG5YR', 'HTIN4', '_BMI5',
        '_RFBMI5', 'HTM4', 'WTKG3', '_BMI5CAT', '_CHLDCNT'],

    8: ['_SMOKER3', '_RFSMOK3', ],

    9: ['DRNKANY5', 'DROCDY3_', '_RFBING5', '_DRNKWEK', '_RFDRHV5'],

    10: ['_EDUCAG', '_INCOMG', 'FTJUDA1_', 'FRUTDA1_', 'BEANDAY_',
         'GRENDAY_', 'ORNGDAY_', 'VEGEDA1_', '_FRUTSUM', '_VEGESUM',
         '_FRTLT1', '_VEGLT1'],

    11: ['_TOTINDA', 'METVL11_', 'METVL21_', 'MAXVO2_', 'FC60_', 'ACTIN11_',
         'ACTIN21_', 'PADUR1_', 'PADUR2_', 'PAFREQ1_', 'PAFREQ2_', '_MINAC11',
         '_MINAC21', 'STRFREQ_', 'PAMISS1_', 'PAMIN11_', 'PAMIN21_', 'PA1MIN_',
         'PAVIG11_', 'PAVIG21_', 'PA1VIGM_', '_PACAT1', '_PAINDX1', '_PA150R2',
         '_PA300R2', '_PA30021', '_PAREC1', '_PASTRNG', '_PASTAE1'],

    12: ['_LMTACT1', '_LMTWRK1', '_LMTSCL1'],

    13: ['_RFSEAT2', '_RFSEAT3'],

    14: ['_FLSHOT6', '_PNEUMO2'],

    15: ['_AIDTST3'],
}