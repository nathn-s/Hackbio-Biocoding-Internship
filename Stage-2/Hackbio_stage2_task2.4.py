import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
sift_df = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv", sep='\s+')
foldx_df = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv", sep='\s+')
"""
print(sift_df)
print(sift_df.dtypes)
print(foldx_df)
print(foldx_df.dtypes)
"""

# Create the specific Protein and Amico acid column
sift_df['specific_Protein_aa'] = sift_df['Protein'] + '_' + sift_df['Amino_Acid']
foldx_df['specific_Protein_aa'] = foldx_df['Protein'] + '_' + foldx_df['Amino_Acid']

# Merge the datasets
merged_df = pd.merge(sift_df, foldx_df, on='specific_Protein_aa', suffixes=('_sift', '_foldx'))
# print(merged_df)

# Identify deleterious mutations as SIFT Score < 0.05 and FoldX score > 2 kCal/mol
deleterious_mutations = merged_df[(merged_df['sift_Score'] < 0.05) & (merged_df['foldX_Score'] > 2)]
print(deleterious_mutations)

# Investigate the amino acid with the most functional and structural impact ---
# Extract the original amino acid
deleterious_mutations['Original_AA'] = deleterious_mutations['Amino_Acid_sift'].str[0]

# Find the most frequent original amino acid
most_impactful_aa = deleterious_mutations['Original_AA'].mode()[0]  # .mode() returns a Series, take the first element
print(f"\nThe amino acid with the most functional and structural impact is: {most_impactful_aa}")

# Generate a frequency table
aa_frequency = deleterious_mutations['Original_AA'].value_counts()
print("\nFrequency Table of Amino Acids with Deleterious Mutations:")
print(aa_frequency)

# Generate plots 
# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=aa_frequency.index, y=aa_frequency.values)
plt.title('Frequency of Original Amino Acids in Deleterious Mutations (Bar Plot)')
plt.xlabel('Amino Acid')
plt.ylabel('Frequency')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(aa_frequency, labels=aa_frequency.index, autopct='%1.1f%%', startangle=140)
plt.title('Frequency of Original Amino Acids in Deleterious Mutations (Pie Chart)')
plt.show()

# Description of the most impactful amino acid
print(f"\n{most_impactful_aa} is the amino acid with the highest impact on protein structure and function, based on the number of deleterious mutations it is involved in.")

# Properties of amino acids with more than 100 occurrences
print(f"\nAmino acids with more than 100 occurrences in deleterious mutations:\n {high_frequency_aa}")
high_frequency_aa = aa_frequency[aa_frequency > 100]
