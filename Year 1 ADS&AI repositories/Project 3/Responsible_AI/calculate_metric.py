import numpy as np

def load_confusion_matrices():
    cm_priv = np.load('./Responsible_AI/confusion_matrix_priv_female.npy')
    tn_priv = cm_priv[0][0]
    fp_priv = cm_priv[0][1]
    fn_priv = cm_priv[1][0]
    tp_priv = cm_priv[1][1]
    cm_unpriv = np.load('./Responsible_AI/confusion_matrix_unpriv_male.npy')
    tn_unpriv = cm_unpriv[0][0]
    fp_unpriv = cm_unpriv[0][1]
    fn_unpriv = cm_unpriv[1][0]
    tp_unpriv = cm_unpriv[1][1]
    return [[tn_priv, fp_priv, fn_priv, tp_priv], [tn_unpriv, fp_unpriv, fn_unpriv, tp_unpriv]]

load_confusion_matrices()

def demographic_parity():

    matrix = load_confusion_matrices()

    # Demographic parity privileged group,
    global DP_PG
    DP_PG = (matrix[0][1]+matrix[0][3])/np.sum(matrix[0])
    # Demographic parity unprivileged group
    global DP_UG
    DP_UG = (matrix[1][1]+matrix[1][3])/np.sum(matrix[1])
    # Absolute difference between the two groups
    global AD_DP
    AD_DP = abs(DP_PG - DP_UG)
    return [DP_PG, DP_UG, AD_DP]

demographic_parity()

def predictive_parity():

    matrix = load_confusion_matrices()

    #Positive predictive value for privileged group
    global PPV_PG
    PPV_PG = matrix[0][3]/(matrix[0][1]+matrix[0][3])
    #Positive predictive value for unprivileged group
    global PPV_UG
    PPV_UG = matrix[1][3]/(matrix[1][1]+matrix[1][3])
    #Absolute difference between the two groups
    global AD_PPV
    AD_PPV = abs(PPV_PG - PPV_UG)
    return [PPV_UG, PPV_PG, AD_PPV]

predictive_parity()

def equalized_odds():

    matrix = load_confusion_matrices()

    #True positive rate for privileged group
    global TPR_PG
    TPR_PG = matrix[0][3]/(matrix[0][3]+matrix[0][2])
    #True positive rate for unprivileged group
    global TPR_UG
    TPR_UG = matrix[1][3]/(matrix[1][3]+matrix[1][2])
    #True negative rate for privileged group
    global TNR_PG
    TNR_PG = matrix[0][0]/(matrix[0][0]+matrix[0][1])
    #True negative rate for unprivileged group
    global TNR_UG
    TNR_UG = matrix[1][0]/(matrix[1][0]+matrix[1][1])
    #Absolute difference between the two groups
    global AD_TPR
    AD_TPR = abs(TPR_PG - TPR_UG)
    global AD_TNR
    AD_TNR = abs(TNR_PG - TNR_UG)
    return [AD_TPR, AD_TNR]

equalized_odds()

def conditional_use_accuracy_equality():

    matrix = load_confusion_matrices()

    #Negative predictive value for privileged group
    global NPV_PG
    NPV_PG = matrix[0][0]/(matrix[0][0]+matrix[0][2])
    #Negative predictive value for unprivileged group
    global NPV_UG
    NPV_UG = matrix[1][0]/(matrix[1][0]+matrix[1][2])
    #Absolute difference between the two groups
    global AD_NPV
    AD_NPV = abs(NPV_PG - NPV_UG)
    AD_PPV = abs(PPV_PG - PPV_UG)
    return [AD_PPV, AD_NPV]

conditional_use_accuracy_equality()

def equal_selection_parity():

    matrix = load_confusion_matrices()

    #Equal selection parity unprivileged group
    global ESP_UG
    ESP_UG = matrix[1][1]+matrix[1][3]
    #Equal selection parity privileged group
    global ESP_PG
    ESP_PG = matrix[0][1]+matrix[0][3]
    #Absolute difference between the two groups
    global AD_ESP
    AD_ESP = abs(ESP_PG - ESP_UG)
    return [ESP_UG, ESP_PG, AD_ESP]

equal_selection_parity()

def equal_opportunity():

    matrix = load_confusion_matrices()

    #Equal opportunity unprivileged group
    global EO_UG
    EO_UG = matrix[1][3]/(matrix[1][3]+matrix[1][2])
    #Equal opportunity privileged group
    global EO_PG
    EO_PG = matrix[0][3]/(matrix[0][3]+matrix[0][2])
    #Absolute difference between the two groups
    global AD_EO
    AD_EO = abs(EO_PG - EO_UG)
    return [EO_UG, EO_PG, AD_EO]

equal_opportunity()

def predictive_equality():

    matrix = load_confusion_matrices()

    #Predictive equality unprivileged group
    global PE_UG
    PE_UG = matrix[1][0]/(matrix[1][0]+matrix[1][1])
    #Predictive equality privileged group
    global PE_PG
    PE_PG = matrix[0][0]/(matrix[0][0]+matrix[0][1])
    #Absolute difference between the two groups
    global AD_PE
    AD_PE = abs(PE_PG - PE_UG)
    return [PE_UG, PE_PG, AD_PE]

predictive_equality()