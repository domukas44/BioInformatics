import matplotlib.pyplot as plt
from bioinfokit.analys import fastq
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from bioinfokit import analys

formats = dict({
    'Sanger Phred+33': (33, 73),
    'Solexa Solexa+64': (59, 104),
    'Illumina 1.3+ Phred+64': (64, 104),
    'Illumina 1.5+ Phred+64': (67, 105),
    'Illumina 1.8+ Phred+33': (33, 74)
})


def a_part():

    print(analys.format.fq_qual_var(file='data/reads_for_analysis.fastq'))


def b_part():
    plt.bar(x, y)
    plt.xlabel('C/G nukletidų dalis read’o sekoje (%)')
    plt.ylabel('read’ų skaičius')
    plt.show()


def c_part():
    # pikai
    print(x[y[:40].index(max(y[:40]))])
    print(x[40:60][y[40:60].index(max(y[40:60]))])
    print(x[60:][y[60:].index(max(y[60:]))])

    peak_1_ids = []
    peak_1_sequences = []
    peak_2_ids = []
    peak_2_sequences = []
    peak_3_ids = []
    peak_3_sequences = []
    peak_1_positions = [j for j, k in enumerate(cg) if k == 34][:5]
    peak_2_positions = [j for j, k in enumerate(cg) if k ==54][:5]
    peak_3_positions = [j for j, k in enumerate(cg) if k == 70][:5]
    for position in peak_1_positions:
        peak_1_ids.append(ids[position])
        peak_1_sequences.append(sequences[position])
    for position in peak_2_positions:
        peak_2_ids.append(ids[position])
        peak_2_sequences.append(sequences[position])
    for position in peak_3_positions:
        peak_3_ids.append(ids[position])
        peak_3_sequences.append(sequences[position])
    print(peak_1_sequences)
    print(peak_2_sequences)
    print(peak_3_sequences)

    ids_column = []
    bacteria_column = []
    for seq_id in peak_1_ids:
        ids_column.append(seq_id)
    for seq_id in peak_2_ids:
        ids_column.append(seq_id)
    for seq_id in peak_3_ids:
        ids_column.append(seq_id)


if __name__ == '__main__':
    iterator = fastq.fastq_reader(file='data/reads_for_analysis.fastq')

    quality_score_concat = ""
    cg = []
    ids = []
    sequences = []
    x = []
    y = []

    for bacteria in iterator:
        header, sequence, plus, quality_score = bacteria
        quality_score_concat = quality_score_concat + quality_score
        cg.append(round((sequence.count('C') + sequence.count('G')) / len(sequence) * 100, 0))
        ids.append(header)
        sequences.append(sequence)

    filtered_characters = set(quality_score_concat)

    for i in range(0, 100):
        x.append(i)
    for element in x:
        y.append(cg.count(element))

    a_part()
    b_part()
    c_part()
