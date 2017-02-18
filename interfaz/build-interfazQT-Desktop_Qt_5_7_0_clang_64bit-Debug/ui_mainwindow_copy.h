/********************************************************************************
** Form generated from reading UI file 'mainwindow_copy.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_COPY_H
#define UI_MAINWINDOW_COPY_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *label;
    QLabel *label_3;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_18;
    QLabel *label_19;
    QLabel *label_20;
    QLabel *label_21;
    QLabel *label_23;
    QLabel *label_24;
    QLabel *label_25;
    QLabel *label_26;
    QLabel *label_27;
    QLabel *label_28;
    QLabel *label_29;
    QLabel *label_30;
    QLabel *label_31;
    QLabel *label_32;
    QLabel *label_33;
    QLabel *label_34;
    QLabel *label_35;
    QLabel *label_36;
    QLabel *label_37;
    QLabel *label_38;
    QLabel *label_39;
    QLabel *label_40;
    QLabel *label_41;
    QLabel *label_44;
    QLabel *label_47;
    QLabel *label_50;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QLabel *label_51;
    QLabel *label_52;
    QLabel *label_58;
    QLabel *label_59;
    QLabel *label_60;
    QLabel *label_61;
    QLabel *label_62;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QPushButton *pushButton_7;
    QPushButton *pushButton_6;
    QPushButton *pushButton_8;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(800, 480);
        QPalette palette;
        QBrush brush(QColor(255, 255, 255, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        QBrush brush1(QColor(81, 82, 83, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Button, brush1);
        QBrush brush2(QColor(121, 123, 125, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Light, brush2);
        QBrush brush3(QColor(101, 102, 104, 255));
        brush3.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Midlight, brush3);
        QBrush brush4(QColor(40, 41, 41, 255));
        brush4.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Dark, brush4);
        QBrush brush5(QColor(54, 54, 55, 255));
        brush5.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Mid, brush5);
        palette.setBrush(QPalette::Active, QPalette::Text, brush);
        palette.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        QBrush brush6(QColor(0, 0, 0, 255));
        brush6.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Base, brush6);
        palette.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette.setBrush(QPalette::Active, QPalette::Shadow, brush6);
        palette.setBrush(QPalette::Active, QPalette::AlternateBase, brush4);
        QBrush brush7(QColor(255, 255, 220, 255));
        brush7.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::ToolTipBase, brush7);
        palette.setBrush(QPalette::Active, QPalette::ToolTipText, brush6);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush2);
        palette.setBrush(QPalette::Inactive, QPalette::Midlight, brush3);
        palette.setBrush(QPalette::Inactive, QPalette::Dark, brush4);
        palette.setBrush(QPalette::Inactive, QPalette::Mid, brush5);
        palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush6);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Shadow, brush6);
        palette.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush4);
        palette.setBrush(QPalette::Inactive, QPalette::ToolTipBase, brush7);
        palette.setBrush(QPalette::Inactive, QPalette::ToolTipText, brush6);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Midlight, brush3);
        palette.setBrush(QPalette::Disabled, QPalette::Dark, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::Mid, brush5);
        palette.setBrush(QPalette::Disabled, QPalette::Text, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Disabled, QPalette::ButtonText, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Shadow, brush6);
        palette.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::ToolTipBase, brush7);
        palette.setBrush(QPalette::Disabled, QPalette::ToolTipText, brush6);
        MainWindow->setPalette(palette);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 801, 91));
        QFont font;
        font.setPointSize(21);
        label->setFont(font);
        label->setStyleSheet(QLatin1String("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(10, 100, 61, 81));
        label_3->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1controladorFlujo1.png")));
        label_3->setScaledContents(true);
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(10, 430, 61, 81));
        label_5->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1controladorFlujo1.png")));
        label_5->setScaledContents(true);
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(60, 150, 161, 21));
        label_6->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_6->setScaledContents(true);
        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(60, 480, 121, 16));
        label_8->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberia1.jpg")));
        label_8->setScaledContents(true);
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(220, 320, 41, 41));
        label_9->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1union4.png")));
        label_9->setScaledContents(true);
        label_10 = new QLabel(centralWidget);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(220, 150, 31, 31));
        label_10->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion2.png")));
        label_10->setScaledContents(true);
        label_11 = new QLabel(centralWidget);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(230, 180, 21, 141));
        label_11->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_11->setScaledContents(true);
        label_12 = new QLabel(centralWidget);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(60, 480, 121, 21));
        label_12->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_12->setScaledContents(true);
        label_13 = new QLabel(centralWidget);
        label_13->setObjectName(QStringLiteral("label_13"));
        label_13->setGeometry(QRect(180, 480, 31, 31));
        label_13->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion2.png")));
        label_13->setScaledContents(true);
        label_14 = new QLabel(centralWidget);
        label_14->setObjectName(QStringLiteral("label_14"));
        label_14->setGeometry(QRect(230, 360, 21, 181));
        label_14->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_14->setScaledContents(true);
        label_15 = new QLabel(centralWidget);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setGeometry(QRect(190, 510, 21, 31));
        label_15->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_15->setScaledContents(true);
        label_16 = new QLabel(centralWidget);
        label_16->setObjectName(QStringLiteral("label_16"));
        label_16->setGeometry(QRect(260, 330, 71, 21));
        label_16->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_16->setScaledContents(true);
        label_18 = new QLabel(centralWidget);
        label_18->setObjectName(QStringLiteral("label_18"));
        label_18->setGeometry(QRect(340, 160, 21, 161));
        label_18->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_18->setScaledContents(true);
        label_19 = new QLabel(centralWidget);
        label_19->setObjectName(QStringLiteral("label_19"));
        label_19->setGeometry(QRect(340, 130, 31, 31));
        label_19->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion2 copy.png")));
        label_19->setScaledContents(true);
        label_20 = new QLabel(centralWidget);
        label_20->setObjectName(QStringLiteral("label_20"));
        label_20->setGeometry(QRect(370, 130, 221, 21));
        label_20->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_20->setScaledContents(true);
        label_21 = new QLabel(centralWidget);
        label_21->setObjectName(QStringLiteral("label_21"));
        label_21->setGeometry(QRect(590, 130, 41, 31));
        label_21->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion4 copy.png")));
        label_21->setScaledContents(true);
        label_23 = new QLabel(centralWidget);
        label_23->setObjectName(QStringLiteral("label_23"));
        label_23->setGeometry(QRect(590, 390, 41, 31));
        label_23->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion4.png")));
        label_23->setScaledContents(true);
        label_24 = new QLabel(centralWidget);
        label_24->setObjectName(QStringLiteral("label_24"));
        label_24->setGeometry(QRect(440, 400, 151, 21));
        label_24->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_24->setScaledContents(true);
        label_25 = new QLabel(centralWidget);
        label_25->setObjectName(QStringLiteral("label_25"));
        label_25->setGeometry(QRect(630, 130, 51, 21));
        label_25->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_25->setScaledContents(true);
        label_26 = new QLabel(centralWidget);
        label_26->setObjectName(QStringLiteral("label_26"));
        label_26->setGeometry(QRect(680, 130, 41, 31));
        label_26->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion2.png")));
        label_26->setScaledContents(true);
        label_27 = new QLabel(centralWidget);
        label_27->setObjectName(QStringLiteral("label_27"));
        label_27->setGeometry(QRect(690, 390, 31, 41));
        label_27->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion4 copy 2.png")));
        label_27->setScaledContents(true);
        label_28 = new QLabel(centralWidget);
        label_28->setObjectName(QStringLiteral("label_28"));
        label_28->setGeometry(QRect(630, 400, 61, 21));
        label_28->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_28->setScaledContents(true);
        label_29 = new QLabel(centralWidget);
        label_29->setObjectName(QStringLiteral("label_29"));
        label_29->setGeometry(QRect(690, 460, 31, 31));
        label_29->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion3.png")));
        label_29->setScaledContents(true);
        label_30 = new QLabel(centralWidget);
        label_30->setObjectName(QStringLiteral("label_30"));
        label_30->setGeometry(QRect(700, 430, 21, 31));
        label_30->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_30->setScaledContents(true);
        label_31 = new QLabel(centralWidget);
        label_31->setObjectName(QStringLiteral("label_31"));
        label_31->setGeometry(QRect(560, 470, 131, 21));
        label_31->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_31->setScaledContents(true);
        label_32 = new QLabel(centralWidget);
        label_32->setObjectName(QStringLiteral("label_32"));
        label_32->setGeometry(QRect(530, 470, 31, 31));
        label_32->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaUnion2 copy.png")));
        label_32->setScaledContents(true);
        label_33 = new QLabel(centralWidget);
        label_33->setObjectName(QStringLiteral("label_33"));
        label_33->setGeometry(QRect(690, 180, 41, 181));
        label_33->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1horno.png")));
        label_33->setScaledContents(true);
        label_34 = new QLabel(centralWidget);
        label_34->setObjectName(QStringLiteral("label_34"));
        label_34->setGeometry(QRect(520, 520, 41, 51));
        label_34->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1cilindro.png")));
        label_34->setScaledContents(true);
        label_35 = new QLabel(centralWidget);
        label_35->setObjectName(QStringLiteral("label_35"));
        label_35->setGeometry(QRect(530, 500, 21, 31));
        label_35->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_35->setScaledContents(true);
        label_36 = new QLabel(centralWidget);
        label_36->setObjectName(QStringLiteral("label_36"));
        label_36->setGeometry(QRect(520, 580, 41, 51));
        label_36->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1cilindro.png")));
        label_36->setScaledContents(true);
        label_37 = new QLabel(centralWidget);
        label_37->setObjectName(QStringLiteral("label_37"));
        label_37->setGeometry(QRect(530, 560, 21, 31));
        label_37->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_37->setScaledContents(true);
        label_38 = new QLabel(centralWidget);
        label_38->setObjectName(QStringLiteral("label_38"));
        label_38->setGeometry(QRect(160, 540, 111, 91));
        label_38->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1saturador.png")));
        label_38->setScaledContents(true);
        label_39 = new QLabel(centralWidget);
        label_39->setObjectName(QStringLiteral("label_39"));
        label_39->setGeometry(QRect(380, 380, 61, 51));
        label_39->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1battery.png")));
        label_39->setScaledContents(true);
        label_40 = new QLabel(centralWidget);
        label_40->setObjectName(QStringLiteral("label_40"));
        label_40->setGeometry(QRect(340, 400, 41, 21));
        label_40->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaHorizontal.jpg")));
        label_40->setScaledContents(true);
        label_41 = new QLabel(centralWidget);
        label_41->setObjectName(QStringLiteral("label_41"));
        label_41->setGeometry(QRect(290, 370, 51, 51));
        label_41->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1valve.png")));
        label_41->setScaledContents(true);
        label_44 = new QLabel(centralWidget);
        label_44->setObjectName(QStringLiteral("label_44"));
        label_44->setGeometry(QRect(80, 460, 60, 16));
        label_47 = new QLabel(centralWidget);
        label_47->setObjectName(QStringLiteral("label_47"));
        label_47->setGeometry(QRect(80, 430, 21, 16));
        label_50 = new QLabel(centralWidget);
        label_50->setObjectName(QStringLiteral("label_50"));
        label_50->setGeometry(QRect(20, 530, 21, 16));
        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(100, 100, 271, 111));
        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(40, 520, 101, 32));
        label_51 = new QLabel(centralWidget);
        label_51->setObjectName(QStringLiteral("label_51"));
        label_51->setGeometry(QRect(700, 160, 21, 31));
        label_51->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_51->setScaledContents(true);
        label_52 = new QLabel(centralWidget);
        label_52->setObjectName(QStringLiteral("label_52"));
        label_52->setGeometry(QRect(700, 360, 21, 31));
        label_52->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1tuberiaVertical.jpg")));
        label_52->setScaledContents(true);
        label_58 = new QLabel(centralWidget);
        label_58->setObjectName(QStringLiteral("label_58"));
        label_58->setGeometry(QRect(470, 340, 31, 51));
        label_58->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1line.png")));
        label_58->setScaledContents(true);
        label_59 = new QLabel(centralWidget);
        label_59->setObjectName(QStringLiteral("label_59"));
        label_59->setGeometry(QRect(470, 300, 31, 21));
        label_59->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1line.png")));
        label_59->setScaledContents(true);
        label_60 = new QLabel(centralWidget);
        label_60->setObjectName(QStringLiteral("label_60"));
        label_60->setGeometry(QRect(430, 290, 16, 21));
        label_60->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1line copy.png")));
        label_60->setScaledContents(true);
        label_61 = new QLabel(centralWidget);
        label_61->setObjectName(QStringLiteral("label_61"));
        label_61->setGeometry(QRect(450, 290, 16, 21));
        label_61->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1line copy.png")));
        label_61->setScaledContents(true);
        label_62 = new QLabel(centralWidget);
        label_62->setObjectName(QStringLiteral("label_62"));
        label_62->setGeometry(QRect(470, 290, 16, 21));
        label_62->setPixmap(QPixmap(QString::fromUtf8("../../images/imagenes1line copy.png")));
        label_62->setScaledContents(true);
        pushButton_4 = new QPushButton(centralWidget);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(410, 100, 281, 111));
        pushButton_5 = new QPushButton(centralWidget);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(100, 210, 271, 111));
        pushButton_7 = new QPushButton(centralWidget);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));
        pushButton_7->setGeometry(QRect(100, 320, 271, 111));
        pushButton_6 = new QPushButton(centralWidget);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));
        pushButton_6->setGeometry(QRect(410, 210, 281, 111));
        pushButton_8 = new QPushButton(centralWidget);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));
        pushButton_8->setGeometry(QRect(410, 320, 281, 111));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 800, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Quirema", 0));
        label->setText(QApplication::translate("MainWindow", "  Quirema                                               Reactor", 0));
        label_3->setText(QString());
        label_5->setText(QString());
        label_6->setText(QString());
        label_8->setText(QString());
        label_9->setText(QString());
        label_10->setText(QString());
        label_11->setText(QString());
        label_12->setText(QString());
        label_13->setText(QString());
        label_14->setText(QString());
        label_15->setText(QString());
        label_16->setText(QString());
        label_18->setText(QString());
        label_19->setText(QString());
        label_20->setText(QString());
        label_21->setText(QString());
        label_23->setText(QString());
        label_24->setText(QString());
        label_25->setText(QString());
        label_26->setText(QString());
        label_27->setText(QString());
        label_28->setText(QString());
        label_29->setText(QString());
        label_30->setText(QString());
        label_31->setText(QString());
        label_32->setText(QString());
        label_33->setText(QString());
        label_34->setText(QString());
        label_35->setText(QString());
        label_36->setText(QString());
        label_37->setText(QString());
        label_38->setText(QString());
        label_39->setText(QString());
        label_40->setText(QString());
        label_41->setText(QString());
        label_44->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        label_47->setText(QApplication::translate("MainWindow", "O2", 0));
        label_50->setText(QApplication::translate("MainWindow", "SV:", 0));
        pushButton_2->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        pushButton_3->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        label_51->setText(QString());
        label_52->setText(QString());
        label_58->setText(QString());
        label_59->setText(QString());
        label_60->setText(QString());
        label_61->setText(QString());
        label_62->setText(QString());
        pushButton_4->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        pushButton_5->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        pushButton_7->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        pushButton_6->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
        pushButton_8->setText(QApplication::translate("MainWindow", "0.0 mL/s", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_COPY_H
