import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '0.5 * math.log((1 - p) / p)'

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.52752523
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'no'

    # type: explain_string
    answers['Explain'] = 'classifiers must each have some ability to make better-than-random predictions based on the data. Since coin flipping lacks any predictive power or analysis, it does not offer a viable method for stock market prediction'
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 'p'

    # type: eval_float
    answers['(a) C2-TPR'] = '2p'

    # type: eval_float
    answers['(a) C1-FPR'] = 'p'

    # type: eval_float
    answers['(a) C2-FPR'] = '2p'

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "both C1 and C2 lie on the random guess line, neither classifier is better than the other in terms of discriminative ability. They are both essentially random guessers"

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = "if the goal is to identify as many true positives as possible without concern for the number of false positives (which seems reasonable given the precision of 1/10), then the evaluation metric pair of {precision and recall} is correctly indicating the relative performance of C2 over C1."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 has a recall of 50%, which is much better than C1s recall of 10%. A higher recall is generally desirable, especially in scenarios where identifying positive instances is crucial"

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "It provides a more comprehensive assessment compared to the {TPR, FPR} pair, which only considers true positive and false positive rates without accounting for the trade-off between precision and recall or the class distribution."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C2'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "the classifier with the highest Recall would generally be considered the best option among the three, subject to further validation and clinical judgment. C2 would be the preferred choice for the initial screening tool to detect cancer."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = 0.1

    # type: eval_float
    answers['(a) recall for C0'] = 'p'

    # type: eval_float
    answers['(b) F-measure of C0'] = '0.2p / (0.1 + p)'

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'unknown'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
        'recall': 0.533333333,
        'precision': 0.615384615,
        'F-measure': 0.57142857,
        'accuracy': 0.88
        }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "accuracy might be a poor indicator of the overall performance of the algorithm in this case if the class distribution is imbalanced, because it does not take into account the false positives and false negatives. F-measure could be the best indicator of the overall performance as it provides a balance between precision and recall. It is especially useful in cases where there is an uneven class distribution, like in this case where days of rain are significantly more than days of sunshine."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The TPR/FPR ratio directly captures this trade-off between true positive rate (TPR) and false positive rate (FPR). A higher TPR/FPR ratio indicates that the test is better at correctly identifying positive (cancer) cases while minimizing the number of false positives (healthy individuals diagnosed as having cancer)."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "Spam email detection: In the context of building a spam email detection system, the priorities and consequences of false positives (legitimate emails misclassified as spam) and false negatives (spam emails misclassified as legitimate) are more balanced. False positives (legitimate emails classified as spam) can lead to important emails being missed or lost, which can be frustrating for users. At the same time, false negatives (spam emails classified as legitimate) can result in users receiving unwanted and potentially malicious spam emails."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
