import pandas as pd

# load the GWAS file
file_path = "gwas_t2d.tsv"
df = pd.read_csv(file_path, sep="\t")

# select useful columns
cols = ["SNPS", "MAPPED_GENE", "DISEASE/TRAIT", "P-VALUE", 
        "OR or BETA", "95% CI (TEXT)", "STUDY ACCESSION", "PUBMEDID"]
df = df[cols]

# drop rows with missing SNP or Gene
df = df.dropna(subset=["SNPS", "MAPPED_GENE"])

# split multiple mapped genes into separate rows
df = df.assign(MAPPED_GENE=df["MAPPED_GENE"].str.split(","))
df = df.explode("MAPPED_GENE")
df["MAPPED_GENE"] = df["MAPPED_GENE"].str.strip()

#save cleaned file
df.to_csv("gwas_t2d_clean.csv", index=False)

print("Cleaned dataset saved as gwas_t2d_clean.csv")

