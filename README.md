# BioInformatics
Dominyko Jovaišos bioinformatikos projektai

Ataskaita

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

8
B1 0.0 0.05976879370000515 0.04554510240847443 0.061788584725763554 0.045715569918641154 0.07045585894067014 0.04604802323442663 0.09006273724141313

B2 0.05976879370000515 0.0 0.04250216524573858 0.08535853240975486 0.048025717023960496 0.03485762720561546 0.05283371864599968 0.049003299806151646

B3 0.04554510240847443 0.04250216524573858 0.0 0.07099946559116788 0.03966733359254377 0.051571657458253324 0.05317377508906526 0.07097774859343615

B4 0.061788584725763554 0.08535853240975486 0.07099946559116788 0.0 0.0687815485082864 0.09129867295885583 0.07110640614033724 0.1082387690832318

M1 0.045715569918641154 0.048025717023960496 0.03966733359254377 0.0687815485082864 0.0 0.0561270548343955 0.05571147098601104 0.07795207879248489

M2 0.07045585894067014 0.03485762720561546 0.051571657458253324 0.09129867295885583 0.0561270548343955 0.0 0.07432087419862739 0.035416263725871436

M3 0.04604802323442663 0.05283371864599968 0.05317377508906526 0.07110640614033724 0.05571147098601104 0.07432087419862739 0.0 0.08750624932510849

M4 0.09006273724141313 0.049003299806151646 0.07097774859343615 0.1082387690832318 0.07795207879248489 0.035416263725871436 0.08750624932510849 0.0

Naudota formulė: sqrt(sum(pow(xi - yi),2)), kai i = visų kodonų/dikodonų skaičius

Palyginimas.

Atsisžvelgiant į sugeneruotus medžius, galima pamatyti, kad bakterijų bei žinduolių kodonų ir dikodonų dažniai yra skirtingi, tačiau ne visiškai, nes į bakterijų klasterį patenka ir žinduoliai, o į žinduolių klasterį patenka ir bakterijos. 
