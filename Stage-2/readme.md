# Stage 2
_**Internship Topics Covered: Dataframe and Visualization in Biological practice **_

## Task code 2.4 - Biochemistry & Oncology
**Reference** Dateset from [Phenotype inference in an Escherichia coli strain panel](https://elifesciences.org/articles/31035)
eLife 2017;6:e31035; doi: [10.7554/eLife.31035](https://doi.org/10.7554/eLife.31035)
Which're uploaded through HackBio:
- [SIFT Dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv)
- [FoldX Dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv)

**Objective:** Identify mutations that are deleterious to both protein structure and function, and determine which amino acids are most frequently replaced in these detrimental mutations.

**Procedure:**

1.  **Data Preparation:**
    *   Load the SIFT and FoldX datasets. These datasets contain scores indicating the functional and structural effects of mutations, respectively.
    *   Create a unique identifier for each mutation in both datasets.  This identifier, `specific_Protein_aa`, is formed by concatenating the `Protein` and `Amino_acid` columns (e.g., `A5A607_E63D`).
    *   Merge the SIFT and FoldX datasets using the `specific_Protein_aa` column as a common key.

2.  **Deleterious Mutation Filtering:**
    *   Apply the following criteria to identify deleterious mutations:
        *   SIFT score < 0.05 (functionally deleterious)
        *   FoldX score > 2 kCal/mol (structurally destabilizing)
    *   Create a subset of the merged dataframe containing only these deleterious mutations.

3.  **Original Amino Acid Analysis:**
    *   Focus on the *original* amino acid that is being *replaced* in each deleterious mutation.  Extract this from the amino acid substitution notation (e.g., the 'E' in 'E63D').
    *   Calculate the frequency of each original amino acid among the deleterious mutations.  This gives us a measure of how often each amino acid is involved in mutations that disrupt both structure and function.
    *   Identify the most frequently occurring original amino acid.

4.  **Visualization and Reporting:**
    *   Generate a frequency table summarizing the counts of each original amino acid.
    *   Create a bar plot and a pie chart to visually represent the frequency distribution of these amino acids.

5.  **Interpretation:**
    *   Briefly describe the chemical and structural properties of the most frequently mutated amino acid.  Explain why this amino acid might be particularly prone to mutations that have negative impacts.
    *   Examine the amino acids with more than 100 occurrences in the deleterious mutation set. Discuss their structural and functional roles, providing insights into their sensitivity to mutations.

6. **Amino acid substitution nomenclature:**
    * Get familiar with amino acid substitution nomenclature.
  
### **Results**

G is the amino acid with the highest impact on protein structure and function, based on the number of deleterious mutations it is involved in.

![image](https://github.com/user-attachments/assets/0e766a4c-5246-48c5-8990-217a981f1874)
![image](https://github.com/user-attachments/assets/26e36044-5a88-4d71-b748-ffb22ff3acc9)


### Table: Amino acids with more than 100 occurrences in deleterious mutations

| Amino Acid | Count | Properties                                                                                                                                                                                                                            |
| :---------: | :---: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      G      | 1307  | Glycine. Smallest amino acid; provides flexibility; often found in turns and loops. Its small size allows for unique backbone conformations.                                                                                   |
|      L      |  739  | Leucine. Aliphatic, hydrophobic; often found in protein core, contributing to hydrophobic interactions and protein stability.                                                                                              |
|      A      |  640  | Alanine. Nonpolar, hydrophobic; small and versatile, found in both buried and exposed regions.                                                                                                                          |
|      P      |  470  | Proline. Rigid, cyclic structure; introduces kinks/turns; frequently in loops and turns, important for defining protein structure.                                                                                     |
|      V      |  380  | Valine. Nonpolar, hydrophobic; similar to alanine but larger; typically found in the protein interior, contributing to the hydrophobic core.                                                                                    |
|      R      |  227  | Arginine. Basic, positively charged; often surface-exposed; involved in salt bridges and interactions with negatively charged molecules.                                                                                        |
|      I      |  212  | Isoleucine. Hydrophobic; similar to leucine and valine; contributes to protein stability by being buried in the hydrophobic core.                                                                                               |
|      Y      |  172  | Tyrosine. Aromatic, polar; can participate in hydrogen bonds and stacking interactions; can be phosphorylated, playing a role in signaling.                                                                                     |
|      D      |  171  | Aspartic Acid. Negatively charged; often surface-exposed; involved in salt bridges and coordination of metal ions.   |
|      F      |  169  | Phenylalanine. Aromatic, hydrophobic; contributes to hydrophobic core and can participate in stacking interactions.                                                                                                            |
|      S      |  158  | Serine. Polar, uncharged; participates in hydrogen bonds; can be phosphorylated, important for cell signaling.                                                                                                             |
|      T      |  126  | Threonine. Polar, uncharged; participates in hydrogen bonds; can be phosphorylated, important for cell signaling.  Similar to Serine.                                                                                            |
|      W      |  108  | Tryptophan. Aromatic, bulky, hydrophobic; contributes to hydrophobic core and can participate in stacking interactions; often involved in protein-ligand interactions due to its aromaticity.                                    |
