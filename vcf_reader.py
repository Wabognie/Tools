"""
Reading and extracting information of vcf file and writting all lines in '.txt' file
informations : name of chromosome, position of gene, frequence of gene, name of gene
"""

### Modification of paths
input_path = ""
output_path = ""

def read_write(path, output_path):
    ### Openning input path -> vcf file with all informations
    ### becarefull no headers, reading line by line not panda using
    data = open(str(path),"r")
    file = data.readlines()
    data.close()

    ### Openning output path -> txt file with "," to separator
    ### Writting header of output file
    out_path = open(str(output_path),"w")
    out_path.write("chromosome_name,position_place,frequence,name_gene" + "\n")

    for line in file :
        if not line.startswith('#') : ##to avoid the first line with description of file (all description's line strated by "##")
            line = line.replace("\n", "")
            line_to_read = line.split("\t")
            chromosome_name = line_to_read[0]
            position_place = line_to_read[1]
            name_gene = ""
            for values in line_to_read :
                if "ENSMUSG" in values : ##to locate the good column containing gene name without "MODERATE", "HIGH", "LOWER", "MODIFIER" marker
                    values = str(values).split("|")
                    indexe_search = ""
                    for indexes in values :
                        if "ENSMUSG" in indexes : ##to locate the index before ENSMUSG column -> corresponding to name gene
                            indexe_search = indexes
                    name = values[values.index(str(indexe_search))-1]
                    name_gene = name

            pourcentage = line_to_read[-1]
            pourcentage_i = str(pourcentage).split(":")
            frequence = pourcentage_i[2]
            ## Write information in output file
            out_path.write(str(chromosome_name)+","+str(position_place)+","+str(frequence)+","+str(name_gene)+"\n")
        else :
            continue
read_write(input_path, output_path)
