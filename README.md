# BioInformatics
Dominyko Jovaišos bioinformatikos projektai

1 laboratorinis darbas

Pateiktoje sekoje fasta formatu surastu visas start ir stop kodonų poras, tarp kurių nebutu stop kodono (ir tiesioginei sekai ir jos reverse komplementui). 
Kiekvienam stop kodonui parinkti toliausiai nuo jo esanti start kodoną (su salyga, kad tarp ju nera kito stop kodono)
Atfiltruokite visus fragmentus ("tai butu baltymų koduojancios sekos"), kurie trumpesni nei 100 fragmentų.
Parasykite funkcijas, kurios ivertintu kodonu ir dikodonu daznius (visi imanomi kodonai/dikodonai ir jų atitinkamas daznis  - gali buti nemazai nuliu, jei ju sekoje nerasite).
Palyginkite kodonu bei dikodonu daznius tarp visu seku (atstumu matrica - kokia formule naudosite/kaip apskaiciuosite - parasykite ataskaitoje).
Ivertinkite, ar bakteriniai ir zinduoliu virusai sudaro atskirus klasterius vertinant kodonu/dikodonu dažniu aspektu. Siuilau atstumu matrica issaugoti tokiu formatu:

Programa patenkina visus reikalavimus. Programoje yra komentarai su žingsniais ir užkomentuotu spausdinimu, su kuriuo galima pasižiūrėti, ką gauname kiekviename žingsnyje

Gauta kodonų matrica:

8
B1 0.0 0.061296287814035 0.04747134744120625 0.06348867968624305 0.04567215154019387 0.07353558180798585 0.049626282547950755 0.09517645806369882
B2 0.061296287814035 0.0 0.040950842821507294 0.09203698922563057 0.04798126186807434 0.03821093819540374 0.05205294104543895 0.05266621902959068
B3 0.04747134744120625 0.040950842821507294 0.0 0.07858868442949377 0.03620922396897884 0.052516817720597776 0.053319124431165626 0.07502626980528496
B4 0.06348867968624305 0.09203698922563057 0.07858868442949377 0.0 0.07648934738025527 0.10091924339428922 0.0773323801671055 0.11794609455221011
M1 0.04567215154019387 0.04798126186807434 0.03620922396897884 0.07648934738025527 0.0 0.0575373048364705 0.057571545958518634 0.08199361229483232
M2 0.07353558180798585 0.03821093819540374 0.052516817720597776 0.10091924339428922 0.0575373048364705 0.0 0.07655181534509274 0.03929628755947009
M3 0.049626282547950755 0.05205294104543895 0.053319124431165626 0.0773323801671055 0.057571545958518634 0.07655181534509274 0.0 0.09072853021057216
M4 0.09517645806369882 0.05266621902959068 0.07502626980528496 0.11794609455221011 0.08199361229483232 0.03929628755947009 0.09072853021057216 0.0

Gauta dikodonų matrica:
