# Stage 2
_**Internship Topics Covered: Dataframe and Visualization in Biological practice **_

## Task List
### Task code 2.4 - Biochemistry & Oncology
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
