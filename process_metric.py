
# /datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs/100_2025-may_cdx_cs_a-e5_h_ccam-2203_q-agcd/annRain.csv

run_dict = {
ACCESS-CM2 (r2i1p1f1) / CCAMoc-v2112
ACCESS-CM2 (r4i1p1f1) / BARPA-R
ACCESS-CM2 (r4i1p1f1) / CCAM-v2203-SN
ACCESS-ESM1-5 (r6i1p1f1) / BARPA-R
ACCESS-ESM1-5 (r6i1p1f1) / CCAM-v2105
ACCESS-ESM1-5 (r6i1p1f1) / CCAM-v2203-SN
ACCESS-ESM1-5 (r6i1p1f1) / NARCliM2-0-WRF412R3
ACCESS-ESM1-5 (r6i1p1f1) / NARCliM2-0-WRF412R5
ACCESS-ESM1-5 (r20i1p1f1) / CCAMoc-v2112
ACCESS-ESM1-5 (r40i1p1f1) / CCAMoc-v2112
CESM2 (r11i1p1f1) / BARPA-R
CESM2 (r11i1p1f1) / CCAM-v2203-SN
CMCC-ESM2 (r1i1p1f1) / BARPA-R
CMCC-ESM2 (r1i1p1f1) / CCAM-v2105
CMCC-ESM2 (r1i1p1f1) / CCAM-v2203-SN
CNRM-CM6-1-HR (r1i1p1f2) / CCAMoc-v2112
CNRM-CM6-1-HR (r1i1p1f2) / CCAM-v2112
CNRM-ESM2-1 (r1i1p1f2) / CCAM-v2203-SN
EC-Earth3 (r1i1p1f1) / BARPA-R
EC-Earth3 (r1i1p1f1) / CCAM-v2105
EC-Earth3 (r1i1p1f1) / CCAM-v2203-SN
EC-Earth3-Veg (r1i1p1f1) / NARCliM2-0-WRF412R3
EC-Earth3-Veg (r1i1p1f1) / NARCliM2-0-WRF412R5
FGOALS-g3 (r4i1p1f1) / CCAM-v2105
GFDL-ESM4 (r1i1p1f1) / CCAM-v2105
GISS-E2-1-G (r2i1p1f2) / CCAM-v2105
MPI-ESM1-2-HR (r1i1p1f1) / BARPA-R
MPI-ESM1-2-LR (r9i1p1f1) / CCAM-v2105
MPI-ESM1-2-HR (r1i1p1f1) / NARCliM2-0-WRF412R3
MPI-ESM1-2-HR (r1i1p1f1) / NARCliM2-0-WRF412R5
MRI-ESM2-0 (r1i1p1f1) / CCAM-v2105
NorESM2-MM (r1i1p1f1) / BARPA-R
NorESM2-MM (r1i1p1f1) / CCAMoc-v2112
NorESM2-MM (r1i1p1f1) / CCAM-v2112
NorESM2-MM (r1i1p1f1) / CCAM-v2203-SN
NorESM2-MM (r1i1p1f1) / NARCliM2-0-WRF412R3
NorESM2-MM (r1i1p1f1) / NARCliM2-0-WRF412R5
UKESM1-0-LL (r1i1p1f2) / NARCliM2-0-WRF412R3
UKESM1-0-LL (r1i1p1f2) / NARCliM2-0-WRF412R5
}



# Store data is gcm_run


gcm_dict = {}

gcm_dict['bom'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'ea-3': 'EC-Earth3',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
}

gcm_dict['cs'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'ce2': 'CESM2',
    'cm-e2': 'CMCC-ESM2',
    'cn-c61': 'CNRM-CM6-1-HR',
    'ea-3': 'EC-Earth3',
    'nor-mm': 'NorESM2-MM',
}

gcm_dict['nsw'] = {
    'a-e5': 'ACCESS-ESM1-5',
    'ea-3v': 'EC-Earth3-Veg',
    'mpi-2h': 'MPI-ESM1-2-HR', 
    'nor-mm': 'NorESM2-MM',
    'uk-0ll': 'UKESM1-0-LL' 
} 

gcm_dict['uq-ccamo-2112'] = {
    'a-cm2': 'ACCESS-CM2',
    'a-e5': 'ACCESS-ESM1-5',
    'cn-c61': 'CNRM-CM6-1-HR',
    'nor-mm': 'NorESM2-MM',
}

gcm_dict['uq-ccam-2112'] = {
    'cn-c61': 'CNRM-CM6-1-HR',
    'nor-mm': 'NorESM2-MM',
}

gcm_dict['uq-ccam-2105] = {
    'a-e5': 'ACCESS-ESM1-5',
    'cm-e2': 'CMCC-ESM2',
    'ea-3': 'EC-Earth3',
    'fg-3': 'FGOALS-g3',
    'gf-e4': 'GFDL-ESM4',
    'gi-e2g': 'GISS-E2-1-G',
    'mpi-2l': 'MPI-ESM1-2-LR',
    'mri-e0': 'MRI-ESM2-0', 
}


rcm_dict = {
    'bar': 'BARPA-R',
    'ccam-2203': 'CCAM-v2203-SN',
    'nar-r3': 'NARCliM2-0-WRF412R3',
    'nar-r5': 'NARCliM2-0-WRF412R5',
    'ccamo-2112': 'CCAMoc-v2112',
    'ccam-2105-r6': 'CCAM-v2105_r6i1p1f1',
    'ccamo-2112-r4': 'CCAMoc-v2112_r40i1p1f1',
    'ccamo-2112-r2': 'CCAMoc-v2112_r20i1p1f1',
    'ccam-2112': 'CCAM-v2112',
}

experiment_dict = {
    'h': 'historical',
    's126': 'ssp126',
    's370': 'ssp370',
    
}

bias_dict = {
    'm-agcd': 'v1-r1-ACS-MRNBC-AGCDv1-1960-2022',
    'q-agcd': 'v1-r1-ACS-QME-AGCDv1-1960-2022',
    'm-barra': 'v1-r1-ACS-MRNBC-BARRAR2-1980-2022' 
    'q-barra': 'v1-r1-ACS-QME-BARRAR2-1980-2022',
}


output files:
- BOM
- CSIRO
- NSW Government
- UQ (CCAMoc-v2112)
- UQ (CCAM-v2112)
- UQ (CCAM-v210)


'2_2025-may_cdx_bom_a-cm2_h_bar_q-barra'.split('_')

index, data, project, institution, gcm, exp, rcm, bias = '2_2025-may_cdx_bom_a-cm2_h_bar_q-barra'.split('_')

institution_parts = institution.split('_')

if len(institution_parts) == 2:
    inst, run = institution_parts
else:
    run = run_dict[(gcm, rcm)]
