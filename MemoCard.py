from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QRadioButton
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from random import shuffle

curParams = {
    'numbQuestion': -1,
    'trueAnswText': '',
    'trueAnswCount': 0,
    'questionCount': 0 
}

def escapeFunc():
    exit()

def showResult():
    resLBL.setText('Результат:\n' + str(curParams['trueAnswCount']) + ' из ' + str(curParams['questionCount']))
    gbQuestion.hide()
    gbAnswer.hide()
    gbResult.show()

def showAnswer():
    userAnswer = ''
    if rbtn1.isChecked():
        userAnswer = rbtn1.text()
    elif rbtn2.isChecked():
        userAnswer = rbtn2.text()
    elif rbtn3.isChecked():
        userAnswer = rbtn3.text()
    elif rbtn4.isChecked():
        userAnswer = rbtn4.text()
    if userAnswer != '':
        _lbl.setText(lbl.text())
        global curParams
        if userAnswer == curParams['trueAnswText']:
            _gb.setTitle('Верно!')
            curParams['trueAnswCount'] += 1
        else:
            _gb.setTitle('Неверно!')
        _gblbl.setText('Правильный ответ:\n' + curParams['trueAnswText'])
        gbQuestion.hide()
        gbAnswer.show()

def showQuestion():
    global curParams
    curParams['numbQuestion'] += 1
    if curParams['numbQuestion'] < len(qList):
        curParams['questionCount'] += 1
        lbl.setText(qList[curParams['numbQuestion']]['question'])
        curParams['trueAnswText'] = qList[curParams['numbQuestion']]['answers'][0]
        answList = qList[curParams['numbQuestion']]['answers']
        shuffle(answList)
        rbtn1.setText(answList[0])
        rbtn2.setText(answList[1])
        rbtn3.setText(answList[2])
        rbtn4.setText(answList[3])
        gbAnswer.hide()
        gbQuestion.show()
    else:
        showResult()
qList = [
    {
        'question': 'Вычислите: 2*2=',
        'answers': [
            '4',
            '6',
            '3',
            '5'
        ]
    },
    {
        'question': 'К какому царству относятся грибы:',
        'answers': [
            'Грибы',
            'Плесень',
            'Тридесятое',
            'Животные'
        ]
    },
    {
        'question': 'В каком городе расположен Та́уэрский мост',
        'answers': [
            'Лондон',
            'Тауэр',
            'Рыбинск',
            'Пекин'
        ]
    }
]
curQuest = 0

app = QApplication([])
mw = QWidget()
ml = QVBoxLayout()
gbQuestion = QGroupBox()
gbAnswer = QGroupBox()
gbResult = QGroupBox()#создаем панель результата
ml.addWidget(gbQuestion, alignment=Qt.AlignCenter)
ml.addWidget(gbAnswer, alignment=Qt.AlignCenter)
ml.addWidget(gbResult, alignment=Qt.AlignCenter)#
mw.setLayout(ml)

vlm = QVBoxLayout()
gbvl = QVBoxLayout()
gbhl1 = QHBoxLayout()
gbhl2 = QHBoxLayout()
lbl = QLabel('Вопрос')
gb = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Ответ1')
rbtn2 = QRadioButton('Ответ2')
rbtn3 = QRadioButton('Ответ3')
rbtn4 = QRadioButton('Ответ4')
btn = QPushButton('Ответить')
vlm.addWidget(lbl, alignment=Qt.AlignCenter)
vlm.addWidget(gb, alignment=Qt.AlignCenter)
vlm.addWidget(btn, alignment=Qt.AlignCenter)
gbvl.addLayout(gbhl1)
gbvl.addLayout(gbhl2)
gbhl1.addWidget(rbtn1, alignment=Qt.AlignCenter)
gbhl1.addWidget(rbtn2, alignment=Qt.AlignCenter)
gbhl2.addWidget(rbtn3, alignment=Qt.AlignCenter)
gbhl2.addWidget(rbtn4, alignment=Qt.AlignCenter)
gb.setLayout(gbvl)
#mw.setLayout(vlm)
gbQuestion.setLayout(vlm)

_vlm = QVBoxLayout()
_gbvl = QVBoxLayout()
_lbl = QLabel('Вопрос')
_gblbl = QLabel('Правильный ответ: aaa')
_gb = QGroupBox('Верно!')
_btn = QPushButton('Следующий вопрос')
_vlm.addWidget(_lbl, alignment=Qt.AlignCenter)
_vlm.addWidget(_gb, alignment=Qt.AlignCenter)
_vlm.addWidget(_btn, alignment=Qt.AlignCenter)
_gbvl.addWidget(_gblbl)
_gb.setLayout(_gbvl)
gbAnswer.setLayout(_vlm)
gbAnswer.hide()

resVL = QVBoxLayout()
resLBL = QLabel()
resBTN = QPushButton('Выйти')
resVL.addWidget(resLBL)
resVL.addWidget(resBTN)
gbResult.setLayout(resVL)
gbResult.hide()
showQuestion()

mw.show()
btn.clicked.connect(showAnswer)
_btn.clicked.connect(showQuestion)
resBTN.clicked.connect(escapeFunc)

app.exec_()