import numpy as np
from Bio import SeqIO
from array import *
import math


def find_frequencies_difference(frequencies1, frequencies2):
    count = 0.0
    for e in range(len(frequencies1)):
        count += math.pow((frequencies1[e] - frequencies2[e]), 2)
    return math.sqrt(count)


def generate_matrix(frequencies):
    matrix = [[0.0 for _ in range(8)] for _ in range(8)]
    for n in range(0, 7):
        for m in range(n + 1, 8):
            matrix[n][m] = find_frequencies_difference(frequencies[n], frequencies[m])
            matrix[m][n] = matrix[n][m]
    return matrix


def find_dicodon_frequency(sequence, dicodon):
    count = 0
    for seq in sequence:
        if seq == dicodon:
            count += 1
    return count / len(sequence)


def get_all_dicodons():
    all_letters = "ARNDCEQGHILKMFPSTWYV"
    dicodons = []
    for start_codon in all_letters:
        for end_codon in all_letters:
            dicodons.append(start_codon + end_codon)
    # print(dicodons)
    return dicodons


def find_dicodon_frequencies(sequence):
    from Bio.Seq import Seq
    string = ""
    for element in sequence:
        string += element
    dna = Seq(string)
    translated_dna = dna.translate()
    # print(translated_dna)
    a = 0
    dicodon_sequence = []
    while a < len(translated_dna) - 1:
        if translated_dna[a] != '*' and translated_dna[a + 1] != '*':
            dicodon_sequence.append(translated_dna[a] + translated_dna[a + 1])
        a += 1
    # print(dicodon_sequence)
    all_dicodons = get_all_dicodons()
    dicodon_frequencies = []
    for dicodon in all_dicodons:
        dicodon_frequencies.append(find_dicodon_frequency(dicodon_sequence, dicodon))
    return dicodon_frequencies


def find_all_frequencies(filtered_sequences):
    all_codons = get_all_codons()
    combined_sequences = "".join(filtered_sequences)
    split_sequence = [combined_sequences[x:x + 3] for x in range(0, len(combined_sequences), 3)]
    codon_frequencies = []
    for codon in all_codons:
        codon_frequencies.append(find_codon_frequency(codon, split_sequence))
    return codon_frequencies


def find_codon_frequency(codon, sequence):
    count = 0
    for seq in sequence:
        if seq == codon:
            count += 1
    return count / len(sequence)


def get_all_codons():
    return ["ATT", "ATC", "ATA", "CTT", "CTC", "CTA", "CTG", "TTA", "TTG", "GTT", "GTC", "GTA", "GTG", "TTT", "TTC",
            "ATG", "TGT", "TGC", "GCT", "GCC", "GCA", "GCG", "GGT", "GGC", "GGA", "GGG", "CCT", "CCC", "CCA", "CCG",
            "ACT", "ACC", "ACA", "ACG", "TCT", "TCC", "TCA", "TCG", "AGT", "AGC", "TAT", "TAC", "TGG", "CAA", "CAG",
            "AAT", "AAC", "CAT", "CAC", "GAA", "GAG", "GAT", "GAC", "AAA", "AAG", "CGT", "CGC", "CGA", "CGG", "AGA",
            "AGG ,TAA", "TAG", "TGA"]


def filter_sequences(sequence_list):
    return [sequence for sequence in sequence_list if len(sequence) >= 100]


def all_longest_sequences(sequence_list):
    longest_sequence_list = [longest_sequence(sequence_list, "TAG"), longest_sequence(sequence_list, "TAA"),
                             longest_sequence(sequence_list, "TGA")]
    return longest_sequence_list


def longest_sequence(sequence_list, end_codon):
    max_length = 0
    longest_seq = ""
    for sequence in sequence_list:
        if len(sequence) > max_length and str(sequence).endswith(end_codon):
            max_length = len(sequence)
            longest_seq = sequence
    return longest_seq


def find_all_pairs(seq_record):
    length = 3
    sequence_list = [seq_record.seq[j:j + length] for j in range(len(seq_record.seq) - 2)]
    reversed_sequence_list = [seq_record.seq.reverse_complement()[j:j + length] for j in range(len(seq_record.seq) - 2)]
    combined_sequence_list = sequence_list + reversed_sequence_list
    # print(combined_sequence_list)
    k = 0
    codon_pairs_list = []
    while k < len(combined_sequence_list):
        if combined_sequence_list[k] == 'ATG':
            start_pos = k
            j = k
            while j < len(combined_sequence_list):
                if combined_sequence_list[j] == 'TAA' or combined_sequence_list[j] == 'TAG'\
                        or combined_sequence_list[j] == 'TGA':
                    end_pos = j
                    codon_pairs_list.append(''.join(str(e) for e in combined_sequence_list[start_pos:end_pos + 1]))
                    k = j
                    break
                j += 1
        k += 1
    return codon_pairs_list
    # print("seq: " + str(sequence))
    # print("rev seq: " + str(reversed_sequence))
    # sequence


def read_file(file_name):
    for seq_record in SeqIO.parse("data/" + file_name, "fasta"):
        sequence = seq_record
    # print(file_name + " " + sequence.seq)
    return sequence


def explore(filename):
    sequence = read_file(filename)

    # pirma uzduotis
    codon_pairs_list = find_all_pairs(sequence)
    # print(codon_pairs_list)

    # 2 uzduotis
    all_longest_seq = all_longest_sequences(codon_pairs_list)
    # print(all_longest_seq)

    # 3 uzduotis
    filtered_sequences = filter_sequences(codon_pairs_list)
    # print(filtered_sequences)

    # 4 uzduotis
    codon_frequencies = find_all_frequencies(filtered_sequences)
    # print(codon_frequencies)
    dicodon_frequencies = find_dicodon_frequencies(filtered_sequences)
    # print(dicodon_frequencies)
    return codon_frequencies, dicodon_frequencies


if __name__ == '__main__':
    codons, dicodons = get_all_codons(), get_all_dicodons()
    all_dicodon_frequencies = []
    all_codon_frequencies = []

    for i in range(1, 5):
        codons, dicodons = explore("bacterial" + str(i) + ".fasta")
        all_codon_frequencies.append(codons)
        all_dicodon_frequencies.append(dicodons)
    # print(all_codon_frequencies[0][1])
    for i in range(1, 5):
        codonss, dicodonss = explore("mamalian" + str(i) + ".fasta")
        all_codon_frequencies.append(codonss)
        all_dicodon_frequencies.append(dicodonss)
    codon_matrix = generate_matrix(all_codon_frequencies)
    print("b1 b2 b3 b4 m1 m2 m3 m4")
    for value in codon_matrix:
        print(value)
    dicodon_matrix = generate_matrix(all_dicodon_frequencies)
    print("b1 b2 b3 b4 m1 m2 m3 m4")
    for value in dicodon_matrix:
        print(value)



