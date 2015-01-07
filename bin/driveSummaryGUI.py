from os.path import isdir

__author__ = 'CAVPP'
#!/usr/bin/python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import gui
# import time
import os


from driveSummary.driveSummary import *

class main_window(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main_window, self).__init__(parent)
        self.selected_directory = ""
        self.other_files = []
        self.data = []
        self.stat_items = []

        self.setupUi(self)
        self.select_drive_button.clicked.connect(self.select_drive)
        self.export_report_text_button.clicked.connect(self.export_report_to_file)

    def populate_searched_for_files(self):
        if not self.stats_tree.isEnabled():
            self.stats_tree.setEnabled(True)
        if self.data["audio_counter"] != 0:

            if self.data["mp3_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "MPEG-2 Audio Layer III",
                                                        ".mp3",
                                                        str(self.data["mp3_counter"])]))
                # self.stats.addItem("mp3: " + str(self.data["mp3_counter"]))

            if self.data["m4a_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "",
                                                        ".m4a",
                                                        str(self.data["m4a_counter"])]))

            if self.data["mpc_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "Musepack",
                                                        ".mpc",
                                                        str(self.data["mpc_counter"])]))

            if self.data["wave_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "Waveform Audio File",
                                                        ".wav",
                                                        str(self.data["wave_counter"])]))

            if self.data["flac_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "Free Lossless Audio Codec",
                                                        ".flac",
                                                        str(self.data["flac_counter"])]))

            if self.data["ogg_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "Ogg",
                                                        ".ogg",
                                                        str(self.data["ogg_counter"])]))

            if self.data["wma_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Audio",
                                                        "Windows Media Audio",
                                                        ".wma",
                                                        str(self.data["wma_counter"])]))
        if self.data["video_counter"] != 0:
            if self.data["avi_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video",
                                                        "Audio Video Interleave",
                                                        ".avi",
                                                        str(self.data["avi_counter"])]))

            if self.data["dv_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video",
                                                        "DV",
                                                        ".dv",
                                                        str(self.data["dv_counter"])]))

            if self.data["mov_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video",
                                                        "QuickTime",
                                                        ".mov",
                                                        str(self.data["mov_counter"])]))

            if self.data["mp4_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video",
                                                        "MPEG-4 Part 14",
                                                        ".mp4",
                                                        str(self.data["mp4_counter"])]))

            if self.data["m4v_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Video",
                                                        "M4V",
                                                        ".m4v",
                                                        str(self.data["m4v_counter"])]))

        if self.data["image_counter"] != 0:
            if self.data["tiff_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image",
                                                        "Tagged Image File Format",
                                                        ".tif",
                                                        str(self.data["tiff_counter"])]))

            if self.data["jpeg_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image",
                                                        "JPEG",
                                                        ".jpg",
                                                        str(self.data["jpeg_counter"])]))

            if self.data["bmp_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image",
                                                        "BMP",
                                                        ".bmp",
                                                        str(self.data["bmp_counter"])]))

            if self.data["gif_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image",
                                                        "Graphics Interchange Format",
                                                        ".gif",
                                                        str(self.data["gif_counter"])]))

            if self.data["png_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Image",
                                                        "Portable Network Graphics",
                                                        ".png",
                                                        str(self.data["png_counter"])]))

        if self.data["document_counter"] != 0:
            if self.data["excel_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document",
                                                        "Excel",
                                                        ".xlsx or .xls",
                                                        str(self.data["excel_counter"])]))

            if self.data["rtf_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document",
                                                        "Rich Text Format",
                                                        ".rtf",
                                                        str(self.data["rtf_counter"])]))

            if self.data["txt_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document",
                                                        "Text",
                                                        ".txt",
                                                        str(self.data["txt_counter"])]))

            if self.data["doc_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document",
                                                        "Doc",
                                                        ".doc",
                                                        str(self.data["doc_counter"])]))

            if self.data["pdf_counter"] != 0:
                self.stat_items.append(QTreeWidgetItem(["Document",
                                                        "Portable Document Format",
                                                        ".pdf",
                                                        str(self.data["pdf_counter"])]))

    def clear_old_data(self):
        self.summary_tree.clear()
        self.stats_tree.clear()
        self.other_files_list.clear()

    def _populate_summary_stats(self):
        self.summary_item = QTreeWidgetItem([
            str(self.data["video_counter"]),
            str(self.data["audio_counter"]),
            str(self.data["image_counter"]),
            str(self.data["document_counter"]),
            str(self.data["md5_counter"]),
            str(self.data["other_counter"]),
            str(self.data["total_counter"]),
            str(size_of_human(self.data["total_file_size"])),
        ])
        self.summary_tree.addTopLevelItem(self.summary_item)
        # for item in self.stat_items:
        #     self.stats_tree.addTopLevelItems(item)
        self.stats_tree.addTopLevelItems(self.stat_items)

    def clear_old_data(self):
        self.summary_tree.clear()
        self.stats_tree.clear()
        self.other_files_list.clear()

    def _populate_summary_stats(self):
        if not self.summary_tree.isEnabled():
            self.summary_tree.setEnabled(True)
        self.summary_item = QTreeWidgetItem([
            str(self.data["video_counter"]),
            str(self.data["audio_counter"]),
            str(self.data["image_counter"]),
            str(self.data["document_counter"]),
            str(self.data["md5_counter"]),
            str(self.data["other_counter"]),
            str(self.data["total_counter"]),
            str(size_of_human(self.data["total_file_size"])),
        ])
        self.summary_tree.addTopLevelItem(self.summary_item)
        self.stats_tree.addTopLevelItems(self.stat_items)

    def _populate_other_files(self):
        if not self.other_files_list.isEnabled():
            self.other_files_list.setEnabled(True)
        self.other_files_list.addItems(self.other_files)

    def _populate_data(self):
        self.populate_searched_for_files()
        self._populate_summary_stats()
        self._populate_other_files()
        if not self.export_report_text_button.isEnabled():
            self.export_report_text_button.setEnabled(True)

    def select_drive(self):

        new_directory = QFileDialog.getExistingDirectory()
        if isdir(new_directory):
            self.selected_directory = new_directory
            self.clear_old_data()
            self.other_files, self.data = get_data(self.selected_directory)
            self._populate_data()

        pass

    def export_report_to_file(self):
        # TODO create method to export report to file
        # print report(self.data, self.other_files)
        fileName, filter = QFileDialog.getSaveFileName(self, "Save Hard Drive Report", '',
                "Text File(*.txt);;All Files (*)")
        print fileName
        if fileName:
            try:
                print "opening"
                f = open(fileName, 'w')
                print f.closed
                print "writing"
                f.write(str(report(self.data, self.other_files)))
                f.close()
                print "done"
            except IOError:
                print "IO Error"
        pass


def main():

    app = QApplication(sys.argv)
    main_win = main_window()
    main_win.show()
    app.exec_()


if __name__ == "__main__":
    main()