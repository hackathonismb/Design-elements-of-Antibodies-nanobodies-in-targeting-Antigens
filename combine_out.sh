#!/bin/bash
input="/path/to/txt/file.txt"
​
# Epitope.js input file is the text file containing the PDB information [PDB ID] [master chain ID] [binding partner chain ID]
while IFS= read -r line
do
        1. node epitope.js [PDB ID] [master chain ID] [binding partner chain ID] > [output_epitope_paratope.txt]
      # Example: node epitope.js 7CM4    A   H > 7CM4, 7CM4_A, 403, R, Spike glycoprotein, 7CM4_H, 56, D, IgG heavy chain
      # Light chain input is  1, 2, and 4 column
        2. Matching of the mutant postion from mutant.txt and output-epitope_paratope.txt > [output_PDBID_ChainID_ResidueNumber_OneLetterMutant.txt]
        # Example Matching of the third column of output-epitope_paratope.txt (here, 403) with  mutant.txt (one mutant perline, here, R403H,so on) containing residue number  say (403) and one letter mutant (H)
        # This step .txt file may avoided by giving ResidueNumber_OneLetterMutant to the third step
        3. node interaction.js [PDB ID] [Chain ID] [Residue number] [One letter mutant] > [change_energy_interaction.txt]
        # Example:  node interaction.js 7CM4    A   403 H > node interaction.js 7CM4    A   403 H free energy (kcal/mol): 68.0997 Change Hbond: -1 Change Ionic: -1 Change Contact: -5 Change Halegen: 0 Change Pi-Cation: -1 Change Pi-Stacking: 2]
​
​
​
done;
