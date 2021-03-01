# Big-Data-Analytics-e-Machine-Learning

## Introduzione:

Il seguente repository contiene una personalizzazione dell'implementazione PyTorch di Residual Masking Network[link](https://github.com/phamquiluan/ResidualMaskingNetwork) per il riconoscimento di espressioni facciali.
È possibile addestrare il modello utilizzando la Residual Masking Network o altre architetture, utilizzando il dataset fer2013. È possibile testare sul modello addestrato lo stesso fer2013, oppure un dataset di frame ricavati da video. È possibile inoltre decidere se applicare una k-fold cross validation e se far stampare, in fase di test, una matrice di confusione normalizzata o meno.

## Requisiti:

1. *Python 3.6+ (è stato usato in particolare python 3.6.9*
2. *PyTorch 1.3+*
3. *Torchvision 0.4.0+*

È neccesario installare i seguenti pacchetti:
1. torch
2. torchvision
3. tqdm

## 1. Training:
 
Per avviare il training, assicurarsi di sistemare i file .csv train, val, e test corrispondenti al dataset fer2013[link](https://drive.google.com/drive/folders/18ovcnZBsPvwXXFVAqczACe9zciO_1q6J) nella cartella saved/data/fer2013/fold_1/. Se si vuole applicare una k-fold cross validation, creare i .csv relativi ai k modi di assegnare i k gruppi in cui il dataset vuole essere diviso (possono essere utilizzati degli script brevemente descritti ala sezione .3) e sistemarli nelle cartelle /saved/data/fer2013/fold_k/ 

## 2. Test:



## 3. Altre funzionalità:

Il repository contiene inoltre nella cartella utils/scv_manager/ degli script che permettono la suddivisone del dataset in set di test, train, e validation applicando una sampling stratification, per generare k-fold che rispettino la distribuzione originale delle classi.
Infine nella cartella utils/preprocess and label/ sono presenti degli script che consentono di estrarre volti da frame video e di labellarli, per creare un set di immagini personalizzato.

