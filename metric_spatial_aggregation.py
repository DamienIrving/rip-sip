'''Command line program for spatial aggregation of metric files.'''

import glob
import argparse

import cmdline_provenance as cmdprov

import definitions

##output files:
#- BOM
#- CSIRO
#- NSW Government
#- UQ (CCAMoc-v2112)
#- UQ (CCAM-v2112)
#- UQ (CCAM-v210)


def main(args):
    '''Run the program.'''

    /datasets/work/af-ag2050-climate/reference/ag2050_extension_metrics_outputs/100_2025-may_cdx_cs_a-e5_h_ccam-2203_q-agcd/annRain.csv

    '2_2025-may_cdx_bom_a-cm2_h_bar_q-barra'.split('_')

    index, data, project, institution, gcm, exp, rcm, bias = '2_2025-may_cdx_bom_a-cm2_h_bar_q-barra'.split('_')

    institution_parts = institution.split('_')

    if len(institution_parts) == 2:
        inst, run = institution_parts
    else:
        run = run_dict[(gcm, rcm)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    metrics = list(definitions.METRIC_ATTRS.keys())
    institutions = list(definitions.GCM_NAMES.keys())
    parser.add_argument('metric', type=str, choices=metrics, help='input variable')
    parser.add_argument('institution', type=str, choices=institutions, help='institution to process')
    parser.add_argument('region', type=str, choices=('aus-wheatbelt',), help='region for spatial aggregation')
    parser.add_argument('outfile', type=str, help='output file')
    args = parser.parse_args()
    main(args)