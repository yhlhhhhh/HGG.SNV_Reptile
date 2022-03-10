import requests
import json
import pandas as pd


def main(inputs, output):
    df = pd.read_csv(inputs)
    df1 = []
    for c in range(len(df)-1):
        e = df.loc[c]
        data = json.loads(requests.get(f'https://www.pggsnv.org/snvSvr/distribute?key={int(e.CHR)}:{int(e.BP)}-{e.A1}-{e.A2}').text)['data']['genotypesList']
        for i in data:
            del[i['aaf']]
            del[i['chrom']]
            del[i['pos']]
            del[i['id']]
            i['rsid'] = e.SNP
            geno = i['geno']
            genotypes = {}
            if geno is not None:
                for a in geno:
                    if isinstance(geno[a], int) and a != 'no':
                        genotypes[a.upper()] = geno[a]
            else:
                pass
            k = list(genotypes.keys())
            v = list(genotypes.values())
            for b in range(len(k)):
                if k[b].count(i['alt']) == 1:
                    i['alt/ref'] = v[b]
                elif k[b].count(i['alt']) == 2:
                    i['alt/alt'] = v[b]
                elif k[b].count(i['alt']) == 0:
                    i['ref/ref'] = v[b]
            del[i['geno']]
            df1.append(i)
    pd.DataFrame(df1).to_csv(output)