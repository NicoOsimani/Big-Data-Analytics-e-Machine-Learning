# Big-Data-Analytics-e-Machine-Learning

## Introduzione:

Il seguente repository contiene una personalizzazione dell'implementazione PyTorch di [Residual Masking Network](https://github.com/phamquiluan/ResidualMaskingNetwork) per il riconoscimento di espressioni facciali. È possibile addestrare il modello utilizzando la Residual Masking Network o altre architetture, utilizzando il dataset fer2013. Il modello addestrato può essere testato utilizzando lo stesso fer2013, oppure un dataset di frame ricavati da video. Inoltre è possibile decidere se applicare una k-fold cross validation e se far stampare, in fase di test, una matrice di confusione normalizzata o meno.

## Requisiti:

1. *Python 3.6+ (è stato usato in particolare python 3.6.9)*
2. *PyTorch 1.3+*
3. *Torchvision 0.4.0+*

È neccesario installare i seguenti pacchetti:
1. torch
2. torchvision
3. tqdm

## 1. Training:
 
Prima di avviare il training:
1. Assicurarsi di sistemare i file .csv train, val, e test corrispondenti al dataset [fer2013](https://drive.google.com/drive/folders/18ovcnZBsPvwXXFVAqczACe9zciO_1q6J) nella cartella saved/data/fer2013/fold_1/. Se si vuole applicare una k-fold cross validation, creare i .csv relativi ai k modi di assegnare i k gruppi in cui il dataset vuole essere diviso (possono essere utilizzati degli script brevemente descritti alla sezione .3) e sistemarli nelle cartelle /saved/data/fer2013/fold_k/.
2. Impostare i corretti parametri di training nel file configs/fer2013config.json. In particolare, indicare l'architettura con la quale si vuole addestrare il modello (nel nostro caso sono state scelte resmasking_dropout1, resnet50 e vgg19) e indicare il numero di fold per la k-fold cross validation, dove 1 significa non utilizzare la k-fold cross validation.

A questo punto si può avviare il training con lo script main_train.py. Il training salva i file di log nella cartella saved/logs/ e il modello o modelli addestrati nella cartella saved/checkpoints/.

## 2. Test:

Prima di avviare il test:
1. Impostare i corretti parametri nel file configs/fer2013config.json nel caso si voglia testare il modello sul datset fer2013, o nel file configs/videoconfig.json nel caso si voglia testare il modello sul dataset di frame estratti da video. Impostare il numero di k-fold in maniera coerente ai modelli addestrati se si vuole utilizzare la k-fold cross validation.
2. Impostare i parametri nei file test_resmasking.py, test_resnet.py o test_vgg.py a seconda dells'architettura con cui il modello o i modelli da testare sono stati addestrati. Se si vuole utilizzare la k-fold cross validation impostare a 0 la variabile best_checkpoint_selection e inserire i nomi dei checkpoint corentemente come indicato. Specificare il nome del dataset sul quale si vuole testare il modello, e infine specificare se si vuole ottenere una matrice di confusione normalizzata o meno.

A questo punto avviare il test con gli script sopra citati. Il test salva i risultati (classification report di sklearn) nella cartella saved/results/ e le matrici di confusione nella cartella saved/cm/.
Se si è utilizzata la k-fold cross validation, si deve eseguire un ulteriore step per mediare i risultati ottenuti. Avviare lo script average_results.py specificando il file di risultati da prendere in input e se le matrici di confusione che lo script si troverà a mediare sono normalizzate o meno. I riusulati e la matrice di confusione saranno salvati nelle cartelle sopra citate.

## 3. Altre funzionalità:

Il repository contiene inoltre nella cartella utils/scv_manager/ degli script che permettono la suddivisone del dataset in set di test, train, e validation applicando una sampling stratification, per generare k-fold che rispettino la distribuzione originale delle classi.
Infine nella cartella utils/preprocess and label/ sono presenti degli script che consentono di estrarre volti da frame video e di labellarli, per creare un set di immagini personalizzato.

