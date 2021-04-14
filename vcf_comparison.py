##Celine

"""
Compare two files to keep all different GENE_ID betwenn all genome and sequenced genome
"""

path_origin = "./C57BL_6NJ.mgp.v5.snps.dbSNP142.PASS.vcf"
path_search = "./GL261-CNV.PASS.snpEff.vcf"
path_out = "./comparison.txt"

def comparison_vcf(path_origin, path_search, path_out):
    data = open(str(path_origin),'r')
    file_origin = data.readlines()
    data.close()

    data2 = open(str(path_search), 'r')
    file_comparison = data2.readlines()
    data2.close()

    out = open(str(path_out),'w')

    n = 0
    list_interest = []
    for line in file_origin :
        line = line.replace("\n", "")
        line_to_read = line.split("\t")
        if n > 0 :
            list_interest.append(line_to_read[1])
        n+=1

    t = 0
    for line in file_comparison :
        if "##" not in line:
            line = line.replace("\n", "")
            line_to_read = line.split("\t")

            if line_to_read[1] not in list_interest:
                out.write(str(line_to_read) + "\n")
        else :
            continue

comparison_vcf(path_origin, path_search, path_out)
