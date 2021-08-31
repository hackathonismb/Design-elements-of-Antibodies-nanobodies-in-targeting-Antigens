#!/bin/bash
input="/path/to/txt/file.txt"

# https://github.com/ncbi/icn3d/tree/master/icn3dnode
# https://github.com/ncbi/icn3d/blob/master/icn3dnode/epitope.js
# https://github.com/ncbi/icn3d/blob/master/icn3dnode/interaction2.js

j=0 # introduce a variable
while read line; do
    ((j++))
    name=`echo $line`
    pdb_name=`echo $name | awk -F ' ' '{print $1}'`
    pdb_chain=`echo $name | awk -F ' ' '{print $1,$2,$3}'` # heavy chain
    #pdb_chain=`echo $name | awk -F ' ' '{print $1,$2,$4}'` # light chain
    echo $name # input for the epitope.js command for identifying epitopes-paratopes information from a PDB
    echo $pdb_chain # input as heavy or light chain complexed with SARS-CoV-2 PDB
   
    # 1. Identifying  epitopes-paratopes infromation from a PDB 
    # usage synatax: node epitope.js [PDB ID] [master chain ID] [binding partner chain ID] > [output_epitope_paratope.txt]
   
    # 1. Identifying  epitopes-paratopes infromation from a PDB 
    # usage synatax: node epitope.js [PDB ID] [master chain ID] [binding partner chain ID] > [output_epitope_paratope.txt]
    # Example: node epitope.js 7CM4    A   H > 7CM4, 7CM4_A, 403, R, Spike glycoprotein, 7CM4_H, 56, D, IgG heavy chain
    node epitope.js $pdb_chain > $pdb_name"_"${j}"_epitopes_paratopes.txt"

    # 2. Matching of the mutant postion from mutant.txt and pdb_epitope_paratope.txt for comparing wild type and mutant type > [output_pdb_epitopes.txt]
    # usage syntax: python3 molecularSentry_match_mutant_position.py variants.txt pdb_epitopes_paratopes.txt
    # Example Matching of the third column of pdb_epitope_paratope.txt (here, 403) with  mutant.txt (one mutant perline, here, R403H,so on) containing residue number  say (403) and one letter mutant (H)
    
    python3 molecularsentry_match_mutant_position.py variants.txt $pdb_name"_"${j}"_epitopes_paratopes.txt" > $pdb_name"_"${j}"_matched_mutant_postion.txt"

    #For identifying the antibody-targeting region of SARS-Cov-2 spike protein (S1, 14–685 residues)
    
    python3 molsen_pdb_analysis.py $pdb_name"_"${j}"_epitopes_paratopes.txt" > $pdb_name"_"${j}"_pdb_info_matched_mutant_postion.txt"

    # 3. Identifying change in eiptopes-paratopes interactions for comparing wild type versus mutant type
    # 3. Identifying change in eiptopes-paratopes interactions for comparing wild type versus mutant type
    # usage syntaxt node interaction2.js [PDB ID] [Chain ID] [Residue number] [One letter mutant] > [output_epitopes_paratopes_interactions.txt]
    # Example:  node interaction2.js 7CM4    A   403 H > 7CM4, 7CM4_A, 403, R, H, -1, 0, -2, 0, 0, 0 (PDB ID, PDB_chain, amino acid postion, original amino acid, mutant amino acid, Change Hbond,Change Ionic, Change Contact, Change Halogen, Change Pi-Cation, Change Pi-Stacking, respectively)
    intract="/home/jupyter-sachendra/scratch/sachendra/$pdb_name"_"${j}_matched_mutant_postion.txt"
    k=0 # introduce a variable
    while read line; do
    	((k++))
    	name2=`echo $line`
    	echo $name2 # input for the interaction2.js command for identifying change in the interactions due to a mutation
        node interaction2.js $name2 >>$pdb_name"_"${j}"_epitopes_paratopes.txt"
        node interaction2.js $name2 >>$pdb_name"_"${j}"_epitopes_paratopes_interactions.txt"
    done < "$intract"	

    # the relative change in interaction based on the individual interaction and count for the same
    
    #python3 molsen_change_indv_interact_analysis.py $pdb_name"_"${j}"_epitopes_paratopes_interactions.txt" >> "summary_epitopes_paratopes_interactions_indv.txt"
    #python3 molsen_change_indv_interact_count_analysis.py $pdb_name"_"${j}"_epitopes_paratopes_interactions.txt" >> "count_epitopes_paratopes_interactions_indv.txt"

    # the relative change in interaction based on the sum of  interaction and count for the same
    
    python3 molsen_change_sum_interact_analysis.py $pdb_name"_"${j}"_epitopes_paratopes_interactions.txt" >> "summary_epitopes_paratopes_interactions_sum.txt"    
    python3 molsen_change_sum_interact_count_analysis.py $pdb_name"_"${j}"_epitopes_paratopes_interactions.txt" >> "count_epitopes_paratopes_interactions.txt"
    

done < "$input"