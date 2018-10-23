#! /usr/bin/pythonw
# coding: utf-8

"""
aleatory_mixtape_v.1
"""

import random, textwrap
from random import randint
import webbrowser

text = ["LOVE098", "LOVE089", "SV128", "HDBD012", "PFL197", "N-037", "JAG316CD", "MUSLIMLIM003DI", "DTD 021DI", "HOS468", "HOS425", "MRP099LP", "SF105LP", "HAFTW008", "HAFTW015", "PRB018", "SFT0376", "DAIS103", "IDEAL134", "IDEAL076", "MRP093LP", "TRR224CD", "KRANK176LP", "ABDT055LP", "VOD91RE", "SV144", "RTRADDA725", "PTYT086LP", "ELP020", "CREP53", "0731383667800", "WARPLP43", "WAP345", "DEATH026", "DEATH013LP", "DEATH012", "PR015", "DEATH006", "RS51CD", "TTT022", "TTT064", "RPC 6", "CST003LP", "HDB098", "SV150", "SV120", "SV087", "LECKEY001", "RAVE002", "USCD55", "KFR2038", "LIES057", "LIES078", "KFR2016", "FV39", "DO-GC01", "DOJS005", "MTR056DNL", "SF031", "SF084DI", "PAL 039DI", "BFFP132I", "EMEGO128", "HOS-601", "HOS-496", "N-033", "N-043", "HOS-450EU", "EMEGO091", "DAIS028", "ARTYARDCD004", "711574835713PMI", "SDGBJ1303DI", "PF07602", "TJDCD326", "TBL1007", "MRP097LP", "MRP083LP", "HOS341", "HN133", "HN206", "TRR312LP", "LOVE079", "LOVE107", "LOVE092", "HDBCD002", "MB3922DB", "SUK 3021", "GOO022LP", "TRUE1236", "WAP375", "RS62", "655035034317", "655035006246", "BC KD", "SE002", "EMEGO189", "CY997", "CY989", "DAIS065LP", "SB1112", "HIT025WMG", "NA5120", "AKUCD1009-10", "AKUDI1007", "ATFA031CD", "HJRCD3", "HJRCD58", "HJRLP62", "STRUT148D", "ARTYARDCD008", "AAIMP228", "702397800620", "WARPCDD25", "FAITBACK01CD", "TNC1", "ELP006", "LACR001", "LACR005", "LACR013", "ABD008DI", "LITA097", "CREVV1087", "HJRLP111", "SUNN25", "BLP005", "LOVE099", "RBN073D", "ONLY3CD", "TO72", "TYPE046", "TYPE009", "BBQDA96", "RH RSS 25", "IMPREC368DI", "ALE001", "SV 09", "W-2383", "SND2SE", "DDD07T", "KRANK177LP", "TYPE074", "ND-25", "LACR008", "LOVE100", "HJP49", "SP185", "ED. RZ1015-16", "BB039", "BRATRALP1005", "P021", "HJRLP107", "634457458567", "FR6", "HDBC001", "ARTYARDLP014", "LSSN020", "METH022X", "STS279D", "H033", "H018-V", "MGART904", "ST07", "ST43", "WAP105", "TRR226CD", "ZIQ290", "JTR06", "SBR3016LP", "HAFTW016", "GI-204LP", "BLACKEST004", "PV007DI", "SF077DI", "KFR2025", "KFR2004", "NHNHCD1005", "DTD 026DI", "HN250", "SS-003", "SS047LP", "NNT007", "RH 115 CD", "LOVE069", "0889397884024", "TYPE063", "STRUT051CD", "STRUT129D", "HOS232", "5055300330895", "R-N 099", "SKA007", "SKA002", "DA006", "GR-006B", "UNITEDJNANA366", "W-0037", "HDB001", "WATER139", "IBFFP180BX", "BMD-1", "WARPCDD66", "SOMADA057", "DUSTDL054", "SHELTER 099", "REL004", "PAN30", "4797007", "SFW40534", "ESP1003D", "ESP1003LP", "TTW77", "SDGBJ1304DI", "CST126CD", "KRANK071", "ALIENCD66", "KRANK213", "MRP023LP", "SUK 3015", "SUK 3020", "NNT005", "NNT006", "NNT008", "MUSLIMLIM018DI", "NNT009", "FABRIC200D", "MEDI069", "PFL152", "634457442627", "SS-027", "ATFA011DIG", "AMMP 791C", "SS-01", "CREP07", "MODE 68", "SF019LP", "SF078DI", "TRS08", "BLUME005", "BLUME006", "MM105", "HJP066", "HJRCD21", "HOS403", "HH666-220", "HOS302", "HOS321-322-323", "HOS319", "VICTO CD 089", "EMEGO124", "RS1003D", "HES013", "RAVE014", "IDEAL160", "PAN87", "HDB116D", "PAN73", "HALC004", "HALCSCREW", "ZENDNLS438", "DED004", "TLOITC001", "TRANS368", "BMD-2", "RS-03", "RS-04", "RS-01", "RS-07", "BMD-3", "BC-08", "BC-01", "BC-03", "BC-04", "HOS581", "PRESH003DA", "PRESH001D", "HERWL002", "HER015", "GCA006", "GCA008", "TFR001", "HATE002", "HATE005", "HATE001", "LOVE096", "LOVE101", "HOS-489", "K7319DTM", "HJP062", "CST081", "KRANK064", "KRANK161LP", "WARPCDD252", "HDB090D", "TEKLIFE001DL", "TEKLIFE006DL", "DM300", "DM069", "DM129 2016", "SP104", "DM262", "DM138", "DM056", "GL002", "LACR015", "SP2104", "SP1204", "DNC1206D", "DNC1205D", "LCTRAX004", "STRUT114CD", "HOS407", "HOS-477", "HOS406", "DIAG043", "REL1", "SND1SE", "SND7", "5055300374622", "DNC1203CD", "HDB091D", "RUG977D2", "S&C001", "RAMP066", "THRILL115LP", "DVBGPM274", "DVBGPM294", "DVGIL 017", "SATURN101477", "SATURN 521", "SATURN92074", "SATURN 406", "SATURN208", "SATURN 529", "8013252888267", "6749300", "KAT 00440", "N006", "NUM5077DIG1", "NUM75LP", "NUM5072DIG1,", "NUM207DIG1", "NUM207.4DIG1", "GRVTS003", "3610155332573", "8013252886355", "DTD 053DI", "ISTUMM32", "HOS79", "HOS106", "HOS401", "ELP037", "LOVE094", "WAP381D", "WARPCDD92", "WAP63CDD", "WAP60CDD", "HDB013", "NONPLUS043", "HDB100D", "WARPCDD38", "WARPDD364-1", "WARPCDD234", "WAP64CDD", "WAP256CDD", "FALL06", "OZITDAND9991D", "HYH-091-2", "HH666-236", "IDEAL149", "NFP-08", "TRR268LP", "20620901CD", "TRR225CD", "20620601CD", "SV109", "BING114", "IMPREC 174DI", "ABD019DI", "TYPE113", "ABD040DI", "SV086", "ESP1006D", "DTD-37", "SBR3008CD", "DTD 023DI", "DTD-47", "DTD 040DI", "DTD-36", "DTD 033DI", "DTD 031DI", "DTD 032DI", "DTD 017DI", "DTD 041DI", "ICE013", "CST098CD", "VIPERDL128", "VIPERDL097", "VIPERDL095", "MRP067LP", "MRP060LP", "HEL 92092", "H09", "HEL93031", "PDZD", "PB08D", "LFDL002", "LFDL003", "WE 031 / AT", "WE 018 / GOT", "WE 024 / AM234", "WE 020 / GOT", "WE 035 / HN106", "HN101", "HN241", "HN208", "HN132", "CEJ10", "HN207", "AMAZON003", "AMAZON013", "AMAZON009", "AMAZON001", "AMAZON021", "ABD011DI", "IDEAL136", "TCD11", "BLACKTRUFFLE011CD", "VDSQ10", "EMEGO166", "EMEGO119", "LOAD126", "LOAD086", "LOAD031", "LOAD022", "LOAD062", "LOAD113", "LOAD082", "LOAD039", "LOAD081", "LOAD064", "LOAD078", "0309", "0305", "0303", "KFR2023", "KFR2021", "KFR2015", "KFR2028", "KFR2003", "KFR2036", "KFR2042", "KFR2027", "KFR10290", "W13DL4", "WCD007", "WC047D", "WC030D", "WC046D", "WCD057", "NG065", "PD351", "PRCD-4049", "PRCD-4070", "PRCD4063", "PRCD-1513", "PRCD-1510", "PRCD4003", "SATURN519", "SATURN19842", "HALC013", "ALT26", "HOS606", "LIES092", "LIES095", "LIES090", "DSRLP025", "GR128", "HJP77", "DO-ADM071", "PSCD99", "WIG140D", "SN11", "WIG89D", "WIG343D", "RUG421D", "WIG59D", "RUG462D", "WIGCD074", "RERUG010D", "REWIG84D", "REWIG83D", "REWIG82D", "HOLY1240", "DC674", "HYP007", "HDB110D", "HDB075", "HDBCD008", "DOR04", "SUK 3018", "SUK 3014", "SUK 3017", "RE022", "WARPDD287C", "MFM019", "MFM035", "BCBR", "ISTUMM44", "NSK1I", "HOS221", "HOS284", "HOS394", "HOS470", "HOS427", "HOS318", "HOS372", "2D01", "HOS260", "HOS336", "HOS341", "HOS263", "HOS337", "HOS-64", "HOS320", "2D18", "PTYT06", "PTYT034-12", "N-028", "FV43", "FV57", "E#21E", "FLUOR001", "TES 158LP", "PLAN-S 20TES.154", "FDR619", "FV83LP", "FV27LP", "FV701", "FV69CD", "FV75CD", "MFM030", "WAP394DD", "WAP425D", "WAP406DA", "EMEGO152", "P!?014", "P026", "KERN004LP", "UTTU001", "UTTU_025", "K009", "ZIQ364", "ZIQ366", "5055300383013", "FTS5LP", "WINO002", "HDBLP002", "AMB3922LP", "HDB080", "YT098DS", "FTDIGI002", "NHS336DD", "METH015", "SNKR014", "PAN82", "RAVE011", "IDEAL133", "HVALUR2CD", "N-041", "N-039", "N-045-2", "N-031", "N-030", "N-044-2", "APATHYXXX", "HDBCD037DS", "NHS002", "DECISIONS12", "SHAM002DI", "AFCD012", "BTDL83", "OR001", "634457442610", "XLDS675EP", "AST027", "ST026", "FUCKPUNK002", "PMAWS003", "GCA007", "TEC084D", "LOVE102", "634457458963", "VOD121.1RE", "ARCHIVE 020DI", "VOD121.5RE", "PAN74", "CJFD20", "E218", "E62", "E209", "E228", "E220", "E219", "E224", "WTN52", "ANM029", "HALC010", "EXIT077", "FUR101", "PAN59", "E197", "E171", "BKV015", "BKV012", "E200", "ASH113", "ASH49", "SV049", "TOE-CD-805", "LOVE033", "PR000", "PAN64", "LOVE103", "LOVE071", "TRIANGLE21", "WAP315DV", "COY006", "FOCUS1666666", "ILTECH010", "ILTECH007", "NAIL007", "AVN0025", "AVN031", "AVN022", "TYPE111", "DDS025", "655035002118", "655035037417", "RAVEDIT", "RAVE017", "RAVE024", "WMA / HIT022", "NSFM001", "NSFM002", "MAN101", "MAN 104", "MAN076", "RTRADDA880", "RTRADDS859", "MEDI096", "MEDI099", "IMRV013", "IMRV015", "BOKA044D", "HATE003", "TRI029LP", "LOVE024", "20620703CD", "TYPE064", "LSINV203LP", "SBR057LP", "SBR071CD", "SBR327LP", "MEOW186", "PP012", "VIS002", "HJP056", "HJP055", "655035008219", "655035007243", "BLEED003", "ANM009", "ANM006", "SS001", "PAN26", "HOS345", "HOS-448", "HOS-411CD", "HOS134", "ESP4058D", "ESP5011D", "RS67", "IMPREC203DI", "VON0172LP", "LOVE109", "KAT 256", "ARCHIVEFOURTYEIGHT", "ARCHIVE017DI", "BLACKESTDL008", "BLACKESTDL017", "DNLP2R", "AM-0", "AM-2", "TBD036", "CST137LP", "OTCR12010", "OTCR12003", "SRV411", "JNR275-8DIG1", "SOMA028", "SUC12", "SA038", "CREP51", "ALE007", "HABIBI007", "AALP084", "UNROCKLP007", "DOSER032", "AKUCD1004", "ADN001", "AKU1001", "OSTLP003", "ASS003", "MRBLP150", "BH31", "CLPM_R003", "CREP42", "SS-041", "JBLP001", "HJP57", "CREP35", "CREP33", "SF106LP", "SF074DI", "HJRCD48", "SOMA022", "SUNN31LP", "GZH084DP D", "1442TP7DL", "1444TP7DL", "MUS170", "MUS118", "MUS154", "ML-020", "FUCKPUNK009", "IDEAL167", "ZIQ356", "ZIQ368", "ZIQ384", "SNKRXDSK001", "SNKR008", "SNKR015", "UTTU_007", "UTTU_008", "VER083", "S&C006", "HDBLP024", "HDB082", "WIGLP094", "STH2183A", "HJRLP201", "HJRLP75", "HJRLP74", "HJP083", "PRB017", "HOS-486", "ZHARK0024", "ZHARK028", "ZHARK0030", "FANTOM 001", "VF271", "K7308", "K7S350D", "SR423", "180GLP02", "SCTR007", "SCTR042", "LITA146LP", "DEATH015LP", "DEATH024", "N49LP", "OMLP10", "PAN52", "XLDA834", "LISTUMM374", "4050538407617", "PAN66", "PAN53CD", "EMEGO202", "TRI046lP-C1", "3299039990322", "WARPDD9RX", "MUSLIMLIM030DI", "ARCHIVE025DI", "ARCHIVE002DI", "ARCHIVE027DI", "ARCHIVEFORTYTWO", "LOVE080", "HDB069", "HOS360", "TYPE105", "HOS424B", "KEM001", "SRV115", "EAD3119A", "PAN35", "HOS354", "HOS-592", "RAVE007", "RAVE022", "RAVE012", "RAVE025-COL", "HOS-498", "BK12X1204", "SP-56", "REAP001", "MSCUM001", "APCO-018", "APCO006", "HOS-435", "HOS-591CD", "HOS391", "HOS-493BLACK", "EDLX048LP", "EDLX053", "DNUM01", "HJP52", "FABRIC109D", "WARPLP247", "WARPDD297B", "KALKCD59", "TYPE080", "VHSX012", "LOVE086", "LOVE1005TESPRESSINGS", "EDRM427", "GM030", "EWR 0403/4", "BNSD018", "EF107", "HN 129", "HN143", "HN195", "TRO-275", "HN 204", "HN 066", "FJORD 006", "PRAXIS56", "102DSR/CFC-CD2", "DSR-X13", "SS067/68", "NW004", "FADELP002", "BD270", "HALC005", "HALC006", "HALC003", "BZH003", "GRVTS007", "OTRLP010", "GRVTS009", "GRVTS011", "DRUGCDR8", "USLP58", "SJRLP418", "HJRCD42", "DB164", "DB165", "AA 072", "AALP086", "AACD 068", "AACD 066", "AA064", "AACD087/AALP087", "BRG005", "MOTEER SAMPLER002", "BRG009", "SIGE 056", "THRILL434LP", "THRILL417LP", "SYR09", "GOO017CD", "GOO14CD", "TG141-5", "TG211-5", "TG184-6", "TG185-6", "TG218-6", "LM029D", "TRI037LP", "TRI022DIG1", "TRI022LP", "TRI008CD", "TRIANGLE34", "TRI040LP", "ONUDL0005", "ONUDL0011", "ONUDL1012", "ONULP18", "ONUDL136", "SWINGTING013", "MEDI097", "MEDI095", "SWINGTING011", "SWINGTING005", "MIX067", "LIES050", "LIES054", "LOL003", "ESTY005", "000000004", "STRUT098CDX", "STRUT195D", "STRUT056CD", "AA 073", "WCD070", "THRILL-256"]
while len(text) > 10:
    text.remove(random.choice(text))
print "\noutput:\n\n" + \
    textwrap.fill(" :: ".join(text), 40) + random.choice(["  /"]) + "\n"

urls = ['http://boomkat.com']

for url in urls:
    webbrowser.open_new_tab(url)





