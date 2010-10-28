# -*- coding: utf-8 -*-

''' This module contains the tray icon's class'''

#import PyKDE4.kdeui     as KdeGui
import PyQt4.QtGui      as QtGui

import gui


class TrayIcon (QtGui.QSystemTrayIcon):
    '''A class that implements the tray icon  of emesene fot Qt4'''
    # pylint: disable=W0612
    NAME = 'TrayIcon'
    DESCRIPTION = 'Qt4 Tray Icon'
    AUTHOR = 'Gabriele Whisky Visconti'
    WEBSITE = ''
    # pylint: enable=W0612
    
    def __init__(self, handler, main_window=None):
        '''
        constructor

        handler -- a e3common.Handler.TrayIconHandler object
        '''
        QtGui.QSystemTrayIcon.__init__(self)
        
        self._handler = handler
        self._main_window = main_window
        self._conversations = None
        
        self._menu = QtGui.QMenu()
        exit_action = QtGui.QAction("Exit", self)
        self._menu.addAction( exit_action )
        self.setContextMenu(self._menu)
        self.setIcon(QtGui.QIcon(QtGui.QPixmap(gui.theme.logo)))
        
        self.activated.connect(self._on_tray_icon_clicked)
        exit_action.triggered.connect(
                              lambda *args: self._handler.on_quit_selected())
        self.show()
        
        
    def set_login(self):    # emesene's
        '''Do nothin'''
        pass
        
    def set_main(self, session):
        '''Called when the main window is shown. Stores the contact list
        and registers the callback for the status_change_succeed event'''
        self._handler.session = session
        self._handler.session.signals.status_change_succeed.subscribe(
                                                    self._on_status_changed)
                                                    
    def set_conversations(self, conversations):     # emesene's
        '''Store a reference to the conversation page'''
        self._conversations = conversations
    
    # emesene's
    def set_visible(self, visible):
        '''Changes icon's visibility'''
        self.setVisible(visible)
        
#    def _on_exit_clicked(self, boh):
#        '''Slot called when the user clicks exit in the context menu'''
#        QtGui.QApplication.instance().exit()
        
    def _on_status_changed(self, status):
        '''This slot is called when the status changes. Update the tray
        icon'''
        self.setIcon(QtGui.QIcon(QtGui.QPixmap(
                                        gui.theme.status_icons_panel[status])))
        
        
    def _on_tray_icon_clicked(self, reason):
        '''This slot is called when the user clicks the tray icon.
        Toggles main window's visibility'''
        
        if not self._main_window:
            return 
        
        if reason == QtGui.QSystemTrayIcon.Trigger:
            if not self._main_window.isVisible():
                self._main_window.show()
                self._main_window.activateWindow()
                self._main_window.raise_()
            else: # visible
                if self._main_window.isActiveWindow():
                    self._main_window.hide()
                else:
                    self._main_window.activateWindow()
                    self._main_window.raise_()
                    
        elif reason == QtGui.QSystemTrayIcon.Context:
            self._menu.show()
        
            

#class TrayIcon (KdeGui.KStatusNotifierItem):
#    '''A class that implements the tray icon of emesene for KDE4'''
#    # pylint: disable=W0612
#    NAME = 'TrayIcon'
#    DESCRIPTION = 'KDE4 Tray Icon'
#    AUTHOR = 'Gabriele Whisky Visconti'
#    WEBSITE = ''
#    # pylint: enable=W0612
#
#    def __init__(self, handler, main_window=None):
#        '''
#        constructor
#
#        handler -- a e3common.Handler.TrayIconHandler object
#        '''
#        KdeGui.KStatusNotifierItem.__init__(self)
#        print ciao_cls
#        
#        self._handler = handler
#        self._main_window = main_window
#        self._conversations = None
#        
#        self.setStatus(KdeGui.KStatusNotifierItem.Active)
#        self.setIconByPixmap(QtGui.QIcon(
#                             QtGui.QPixmap(
#                             gui.theme.logo).scaled(QtCore.QSize(40, 40))))
#                             
#        self.activateRequested.connect(self._on_tray_icon_clicked)
#                            
#                            
#    def set_login(self):
#        '''does nothing'''
#        pass
#
#    def set_main(self, session):
#        '''does nothing'''
#        self._handler.session = session
#        self._handler.session.signals.status_change_succeed.subscribe(
#                                            self._on_status_changed)
#        
#    
#    def set_conversations(self, conversations): # emesene's
#        '''Stores a reference to the conversation page'''
#        self._conversations = conversations 
#        
#        
#        
#    def _on_status_changed(self, status):
#        self.setIconByPixmap(QtGui.QIcon(QtGui.QPixmap(
#                                        gui.theme.status_icons_panel[status])))
#        
#        
#    def _on_tray_icon_clicked(self, active, pos):
#        if not self._main_window:
#            return 
#            
#        if not self._main_window.isVisible():
#            self._main_window.show()
#            self._main_window.activateWindow()
#            self._main_window.raise_()
#        else: # visible
#            if self._main_window.isActiveWindow():
#                self._main_window.hide()
#            else:
#                self._main_window.activateWindow()
#                self._main_window.raise_()
        
        
        
        
        