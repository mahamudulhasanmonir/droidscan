import sys

from PyQt6.QtWidgets import QApplication

from gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    # ✅ ADD DARK THEME HERE
    app.setStyleSheet(
        """
        QWidget {
            background: #0f172a;
            color: #e2e8f0;
            font-family: "Segoe UI";
            font-size: 13px;
        }
        #Sidebar {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #172554, stop:1 #0f172a);
            border: 1px solid #1e3a8a;
            border-radius: 22px;
            min-width: 210px;
            max-width: 230px;
        }
        #SidebarTitle {
            font-size: 24px;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 2px;
        }
        #SidebarSubtitle, #MutedLabel, #HeroSubtitle, #EmptyState {
            color: #94a3b8;
        }
        #SidebarButton {
            background: transparent;
            border: 1px solid transparent;
            border-radius: 14px;
            padding: 12px 14px;
            text-align: left;
            font-weight: 600;
        }
        #SidebarButton:hover {
            background: rgba(59, 130, 246, 0.16);
            border-color: rgba(96, 165, 250, 0.35);
        }
        #SidebarButton:checked {
            background: #eff6ff;
            color: #0f172a;
            border-color: #bfdbfe;
        }
        #TopBarCard, #ContentStack, #SummaryCard, #InfoCard, QTabWidget::pane, QTextEdit, QTableWidget {
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 20px;
        }
        #TopBarCard {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1d4ed8, stop:1 #0f172a);
        }
        #HeroTitle {
            font-size: 26px;
            font-weight: 700;
            color: #f8fafc;
        }
        #PageTitle {
            font-size: 22px;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 4px;
        }
        #StatusLabel {
            background: rgba(15, 23, 42, 0.45);
            border: 1px solid rgba(191, 219, 254, 0.35);
            border-radius: 999px;
            padding: 8px 14px;
            font-weight: 700;
        }
        QPushButton {
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px 16px;
            font-weight: 700;
        }
        QPushButton:hover {
            background: #3b82f6;
        }
        QPushButton:disabled {
            background: #334155;
            color: #94a3b8;
        }
        #GhostButton {
            background: #0f172a;
            border: 1px solid #334155;
        }
        #GhostButton:hover {
            background: #1e293b;
        }
        #CardTitle {
            color: #94a3b8;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
        }
        #CardValue {
            color: #f8fafc;
            font-size: 16px;
            font-weight: 600;
        }
        QTabBar::tab {
            background: #0f172a;
            color: #cbd5e1;
            padding: 10px 14px;
            margin-right: 6px;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
        }
        QTabBar::tab:selected {
            background: #1d4ed8;
            color: white;
        }
        QHeaderView::section {
            background: #172554;
            color: #e2e8f0;
            border: none;
            padding: 10px;
            font-weight: 700;
        }
        QTableWidget {
            gridline-color: #1f2937;
            alternate-background-color: #0f172a;
        }
        QTableWidget::item {
            padding: 8px;
        }
        QTextEdit {
            padding: 8px;
            selection-background-color: #2563eb;
        }
        QScrollBar:vertical {
            background: transparent;
            width: 12px;
            margin: 8px 2px 8px 2px;
        }
        QScrollBar::handle:vertical {
            background: #334155;
            border-radius: 6px;
            min-height: 30px;
        }
        """
    )

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

